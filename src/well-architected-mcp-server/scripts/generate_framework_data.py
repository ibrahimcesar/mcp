#!/usr/bin/env python3
"""Generate framework/ markdown files by fetching content from AWS docs.

Fetches all best practice pages from docs.aws.amazon.com, converts to markdown,
and writes them into data/framework/ with proper frontmatter.

Usage:
    python scripts/generate_framework_data.py [--delay 0.3] [--dry-run] [--ids SEC01-BP01,OPS01-BP01]
"""

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path


DATA_DIR = (
    Path(__file__).resolve().parent.parent
    / "awslabs"
    / "well_architected_mcp_server"
    / "data"
)
FRAMEWORK_DIR = DATA_DIR / "framework"

PILLAR_DISPLAY = {
    "OPERATIONAL_EXCELLENCE": "Operational Excellence",
    "SECURITY": "Security",
    "RELIABILITY": "Reliability",
    "PERFORMANCE_EFFICIENCY": "Performance Efficiency",
    "COST_OPTIMIZATION": "Cost Optimization",
    "SUSTAINABILITY": "Sustainability",
}



def load_all_bps():
    """Load all best practices from JSON files."""
    all_bps = {}
    for f in [
        "cost_optimization",
        "operational_excellence",
        "performance_efficiency",
        "reliability",
        "security",
        "sustainability",
    ]:
        with open(DATA_DIR / f"{f}.json") as fp:
            for bp in json.load(fp):
                all_bps[bp["id"]] = bp
    return all_bps


def load_existing_metadata():
    """Load capability (question) metadata from existing framework frontmatter."""
    metadata = {}
    if not FRAMEWORK_DIR.exists():
        return metadata
    for md_file in FRAMEWORK_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                meta = {}
                for line in parts[1].strip().splitlines():
                    if ":" in line:
                        key, val = line.split(":", 1)
                        meta[key.strip()] = val.strip().strip('"')
                metadata[md_file.stem] = meta
    return metadata


def fetch_url(url):
    """Fetch a URL and return its content."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def decode_entities(text):
    """Decode HTML entities."""
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&#39;", "'", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#x27;", "'", text)
    text = re.sub(r"&#x2F;", "/", text)
    text = re.sub(r"&#\d+;", "", text)
    return text


def strip_tags(html):
    """Remove HTML tags and decode entities."""
    text = re.sub(r"<[^>]+>", "", html)
    return decode_entities(text)


def extract_bp_content(html):
    """Extract the best practice content from the AWS docs page HTML."""
    h1_match = re.search(r"(<h1[^>]*>.*?</h1>)", html, re.DOTALL)
    if not h1_match:
        return None

    h1_start = h1_match.start()

    end_match = re.search(r"<awsdocs-copyright", html[h1_start:])
    if end_match:
        content = html[h1_start : h1_start + end_match.start()]
    else:
        end_match = re.search(r"<footer", html[h1_start:])
        if end_match:
            content = html[h1_start : h1_start + end_match.start()]
        else:
            content = html[h1_start:]

    return content


def html_to_markdown(html):
    """Convert HTML content to clean markdown."""
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
    text = re.sub(r"<nav[^>]*>.*?</nav>", "", text, flags=re.DOTALL)
    text = re.sub(r"<awsdocs-[^>]*>.*?</awsdocs-[^>]*>", "", text, flags=re.DOTALL)
    text = re.sub(r"<awsdocs-[^>]*/>", "", text)

    # Headers
    text = re.sub(
        r"<h1[^>]*>(.*?)</h1>",
        lambda m: f"# {strip_tags(m.group(1)).strip()}\n\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<h2[^>]*>(.*?)</h2>",
        lambda m: f"\n## {strip_tags(m.group(1)).strip()}\n\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<h3[^>]*>(.*?)</h3>",
        lambda m: f"\n### {strip_tags(m.group(1)).strip()}\n\n",
        text,
        flags=re.DOTALL,
    )

    # Links
    def fix_link(m):
        href = m.group(1)
        link_text = strip_tags(m.group(2)).strip()
        if not link_text:
            return ""
        if href.startswith("/"):
            href = f"https://docs.aws.amazon.com{href}"
        return f"[{link_text}]({href})"

    text = re.sub(
        r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', fix_link, text, flags=re.DOTALL
    )

    # Bold
    text = re.sub(
        r"<b>(.*?)</b>",
        lambda m: f"**{strip_tags(m.group(1)).strip()}**",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<strong>(.*?)</strong>",
        lambda m: f"**{strip_tags(m.group(1)).strip()}**",
        text,
        flags=re.DOTALL,
    )

    # Italic
    text = re.sub(
        r"<em>(.*?)</em>",
        lambda m: f"*{strip_tags(m.group(1)).strip()}*",
        text,
        flags=re.DOTALL,
    )

    # Lists
    text = re.sub(r"<[ou]l[^>]*>", "\n", text)
    text = re.sub(r"</[ou]l>", "\n", text)
    text = re.sub(
        r"<li[^>]*>(.*?)</li>",
        lambda m: f"- {strip_tags(m.group(1)).strip()}\n",
        text,
        flags=re.DOTALL,
    )

    # Paragraphs
    text = re.sub(
        r"<p[^>]*>(.*?)</p>",
        lambda m: f"\n{strip_tags(m.group(1)).strip()}\n",
        text,
        flags=re.DOTALL,
    )

    # Code
    text = re.sub(
        r"<code[^>]*>(.*?)</code>",
        lambda m: f"`{strip_tags(m.group(1)).strip()}`",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<pre[^>]*>(.*?)</pre>",
        lambda m: f"\n```\n{strip_tags(m.group(1)).strip()}\n```\n",
        text,
        flags=re.DOTALL,
    )

    # Remove remaining tags
    text = strip_tags(text)

    # Clean up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def process_bp(bp_id, bp_json, existing_meta, delay=0.3):
    """Fetch and generate a framework markdown file for a single BP."""
    url = bp_json.get("href", "")
    if not url:
        return None

    try:
        html = fetch_url(url)
    except Exception as e:
        print(f"  ERROR fetching {bp_id}: {e}", file=sys.stderr)
        return None

    content_html = extract_bp_content(html)
    if not content_html:
        print(f"  ERROR: No content found for {bp_id}", file=sys.stderr)
        return None

    md_body = html_to_markdown(content_html)

    # Remove the h1 title line (we'll add it in the file structure)
    lines = md_body.split("\n")
    start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            start = i + 1
            break
    body = "\n".join(lines[start:]).strip()

    # Build frontmatter
    title = bp_json.get("title", "")
    pillar = PILLAR_DISPLAY.get(bp_json.get("pillar", ""), bp_json.get("pillar", ""))
    risk = bp_json.get("risk", "MEDIUM")
    capability = existing_meta.get("capability", "") if existing_meta else ""

    frontmatter_lines = [
        "---",
        f'id: "{bp_id}"',
        f'title: "{title}"',
        f'pillar: "{pillar}"',
        f'risk_level: "{risk}"',
    ]
    if capability:
        frontmatter_lines.append(f'capability: "{capability}"')
    frontmatter_lines.append(f'url: "{url}"')
    frontmatter_lines.append("---")

    full_content = "\n".join(frontmatter_lines) + f"\n\n# {bp_id} {title}\n\n{body}\n"
    return full_content


def main():
    parser = argparse.ArgumentParser(description="Generate framework data from AWS docs")
    parser.add_argument(
        "--delay",
        type=float,
        default=0.3,
        help="Delay between HTTP requests (default: 0.3s)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Only show what would be fetched")
    parser.add_argument(
        "--ids",
        type=str,
        default="",
        help="Comma-separated list of BP IDs to process (default: all)",
    )
    args = parser.parse_args()

    print(f"Output directory: {FRAMEWORK_DIR}")
    FRAMEWORK_DIR.mkdir(parents=True, exist_ok=True)

    all_bps = load_all_bps()
    existing_metadata = load_existing_metadata()

    if args.ids:
        bp_ids = [x.strip() for x in args.ids.split(",")]
    else:
        bp_ids = sorted(all_bps.keys())

    print(f"Processing {len(bp_ids)} best practices...")

    if args.dry_run:
        for bp_id in bp_ids:
            bp = all_bps.get(bp_id)
            if bp:
                print(f"  {bp_id}: {bp.get('href', 'NO URL')}")
        return

    success = 0
    failed = 0
    for i, bp_id in enumerate(bp_ids):
        bp = all_bps.get(bp_id)
        if not bp:
            print(f"  SKIP: {bp_id} not found in JSON data")
            continue

        existing_meta = existing_metadata.get(bp_id, {})
        print(f"  [{i + 1}/{len(bp_ids)}] {bp_id}...", end=" ", flush=True)

        content = process_bp(bp_id, bp, existing_meta, args.delay)
        if content:
            out_file = FRAMEWORK_DIR / f"{bp_id}.md"
            out_file.write_text(content, encoding="utf-8")
            print("OK")
            success += 1
        else:
            print("FAILED")
            failed += 1

        if i < len(bp_ids) - 1:
            time.sleep(args.delay)

    print(f"\nDone! {success} generated, {failed} failed.")


if __name__ == "__main__":
    main()
