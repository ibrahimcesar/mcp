#!/usr/bin/env python3
"""Ingest a new Well-Architected Lens from AWS docs into the local data format.

This script:
1. Fetches the lens TOC from AWS docs
2. Discovers all best practice pages (matching *-bp*.html pattern)
3. Extracts structured content from each page
4. Outputs per-pillar JSON files matching the existing schema

Usage:
    python scripts/ingest_lens.py <lens-slug> [--lens-name NAME]

Examples:
    python scripts/ingest_lens.py generative-ai-lens --lens-name GENERATIVE_AI
    python scripts/ingest_lens.py saas-lens --lens-name SAAS
    python scripts/ingest_lens.py serverless-applications-lens --lens-name SERVERLESS
    python scripts/ingest_lens.py data-analytics-lens --lens-name DATA_ANALYTICS

The lens-slug is the path segment in the AWS docs URL:
    https://docs.aws.amazon.com/wellarchitected/latest/<lens-slug>/

Output is written to: data/lens/<lens-slug>/<pillar>.json
"""

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "src" / "well_architected_bp_mcp_server" / "data"
BASE_URL = "https://docs.aws.amazon.com/wellarchitected/latest"


def fetch_url(url: str) -> str:
    """Fetch a URL and return its content as string."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_toc(lens_slug: str) -> dict:
    """Fetch the table of contents JSON for a lens."""
    url = f"{BASE_URL}/{lens_slug}/toc-contents.json"
    try:
        content = fetch_url(url)
        return json.loads(content)
    except Exception as e:
        print(f"ERROR: Could not fetch TOC from {url}: {e}", file=sys.stderr)
        sys.exit(1)


def find_bp_pages(toc: dict, lens_slug: str) -> list[dict]:
    """Walk the TOC tree and find all best practice pages.

    Strategy 1: Look for pages with -bp\\d+ in the href (newer lenses like generative-ai, ML).
    Strategy 2: If none found, look for leaf pages under "Best practices" sections (older lenses).

    Returns list of dicts with: href, title, parent_titles (for area context).
    """
    results = []

    def walk_bp_pattern(contents: list, parents: list[str] | None = None):
        if parents is None:
            parents = []
        for item in contents:
            title = item.get("title", "")
            href = item.get("href", "")

            if re.search(r"-bp\d+", href, re.IGNORECASE):
                results.append({
                    "href": f"{BASE_URL}/{lens_slug}/{href}",
                    "title_from_toc": title,
                    "area": list(parents),
                })

            if "contents" in item:
                walk_bp_pattern(item["contents"], parents + [title])

    walk_bp_pattern(toc.get("contents", []))

    if results:
        return results

    # Fallback: find leaf pages nested under pillar/best-practices sections
    def walk_leaf_pages(contents: list, parents: list[str] | None = None, in_bp_section: bool = False):
        if parents is None:
            parents = []
        for item in contents:
            title = item.get("title", "")
            href = item.get("href", "")
            is_bp_header = "best practice" in title.lower()

            if "contents" in item:
                walk_leaf_pages(
                    item["contents"],
                    parents + [title],
                    in_bp_section or is_bp_header,
                )
            elif in_bp_section and href:
                results.append({
                    "href": f"{BASE_URL}/{lens_slug}/{href}",
                    "title_from_toc": title,
                    "area": [p for p in parents if "best practice" not in p.lower()],
                })

    walk_leaf_pages(toc.get("contents", []))
    return results


def strip_tags(html: str) -> str:
    """Remove HTML tags and normalize whitespace."""
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_list_items(html: str) -> list[str]:
    """Extract text from <li> elements."""
    items = re.findall(r"<li[^>]*>(.*?)</li>", html, re.DOTALL)
    return [strip_tags(item) for item in items if strip_tags(item)]


def extract_section_after_bold(html: str, label: str) -> list[str]:
    """Extract content following a <b>label:</b> pattern."""
    pattern = rf"<b>{re.escape(label)}[^<]*</b>(.*?)(?=<p>\s*<b>|<h2|</div>\s*<awsdocs|\Z)"
    match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
    if not match:
        escaped = re.escape(label).replace(r"\ ", r"\s+")
        pattern = rf"<b>{escaped}[^<]*</b>(.*?)(?=<p>\s*<b>|<h2|</div>\s*<awsdocs|\Z)"
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
    if not match:
        return []

    content = match.group(1)
    if "<li" in content:
        return extract_list_items(content)
    text = strip_tags(content)
    return [text] if text else []


def extract_implementation(html: str) -> list[str]:
    """Extract implementation guidance/steps section."""
    for pattern in [
        r'<h2[^>]*id="implementation-guidance"[^>]*>.*?</h2>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)',
        r'<h2[^>]*id="implementation-steps"[^>]*>.*?</h2>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)',
        r'<b>Implementation steps</b>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)',
        r'<b>Implementation guidance</b>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)',
    ]:
        match = re.search(pattern, html, re.DOTALL)
        if match:
            break
    else:
        return []

    content = match.group(1)
    if "<li" in content:
        items = extract_list_items(content)
        if items:
            return items

    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", content, re.DOTALL)
    results = []
    for p in paragraphs:
        text = strip_tags(p)
        if text and len(text) > 10:
            results.append(text)
    return results


def extract_resources(html: str) -> list[str]:
    """Extract related resources/links from the Resources section."""
    pattern = r'<h2[^>]*id="resources"[^>]*>.*?</h2>(.*?)(?=<awsdocs-copyright|\Z)'
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        return []

    content = match.group(1)
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', content, re.DOTALL)
    results = []
    for href, text in links:
        label = strip_tags(text)
        if label and "javascript" not in href.lower():
            results.append(f"{label}: {href}")
    return results


def extract_description(html: str) -> str:
    """Extract the main description paragraph (first <p> in content body)."""
    match = re.search(
        r'</awsdocs-filter-selector></div><p[^>]*>(.*?)</p>',
        html,
        re.DOTALL,
    )
    if match:
        return strip_tags(match.group(1))
    return ""


def extract_risk(html: str) -> str:
    """Extract risk level from the page."""
    match = re.search(
        r"Level of risk exposed if this best practice\s*is not established[^<]*</b>\s*(\w+)",
        html,
        re.DOTALL,
    )
    if match:
        risk = match.group(1).strip().upper()
        if risk in ("HIGH", "MEDIUM", "LOW"):
            return risk
    return "MEDIUM"


def parse_bp_id(title: str) -> str:
    """Extract BP ID from title like 'GENOPS01-BP01 Some title'."""
    match = re.match(r"([A-Z]+\d+-BP\d+)", title)
    if match:
        return match.group(1)
    return ""


def infer_pillar(bp_id: str, area: list[str]) -> str:
    """Infer the pillar from the BP ID prefix or area context."""
    id_lower = bp_id.lower()

    pillar_keywords = {
        "OPERATIONAL_EXCELLENCE": ["ops", "opex", "operate", "operational excellence"],
        "SECURITY": ["sec", "security"],
        "RELIABILITY": ["rel", "reliability"],
        "PERFORMANCE_EFFICIENCY": ["perf", "performance"],
        "COST_OPTIMIZATION": ["cost"],
        "SUSTAINABILITY": ["sus", "sustainability"],
    }

    for pillar, keywords in pillar_keywords.items():
        for kw in keywords:
            if kw in id_lower:
                return pillar

    area_lower = " ".join(area).lower()
    for pillar, keywords in pillar_keywords.items():
        for kw in keywords:
            if kw in area_lower:
                return pillar

    return "UNKNOWN"


def ingest_bp_page(page_info: dict, lens_name: str) -> dict | None:
    """Fetch and parse a single best practice page into our schema format."""
    href = page_info["href"]
    title_from_toc = page_info["title_from_toc"]
    area = page_info["area"]

    try:
        html = fetch_url(href)
    except Exception as e:
        print(f"  WARNING: Failed to fetch {href}: {e}", file=sys.stderr)
        return None

    bp_id = parse_bp_id(title_from_toc)
    if not bp_id:
        match = re.search(r"([A-Z]+\d+-BP\d+)", html)
        if match:
            bp_id = match.group(1)
        else:
            return None

    title_match = re.match(r"[A-Z]+\d+-BP\d+\s+(.+)", title_from_toc)
    title = title_match.group(1) if title_match else title_from_toc

    description = extract_description(html)
    risk = extract_risk(html)
    desired_outcome = extract_section_after_bold(html, "Desired outcome")
    anti_patterns = extract_section_after_bold(html, "Common anti-patterns")
    benefits = extract_section_after_bold(html, "Benefits of establishing this best practice")
    implementation = extract_implementation(html)
    resources = extract_resources(html)

    bp = {
        "area": area if area else ["General"],
        "description": description,
        "href": href,
        "id": bp_id,
        "lens": lens_name,
        "outcome": "",
        "pillar": infer_pillar(bp_id, area),
        "relatedIds": [],
        "risk": risk,
        "title": title,
        "title_full": f"{bp_id} {title}",
    }

    if desired_outcome:
        bp["desired_outcome"] = desired_outcome
    if anti_patterns:
        bp["anti_patterns"] = anti_patterns
    if benefits:
        bp["benefits"] = benefits[0] if len(benefits) == 1 else benefits
    if implementation:
        bp["implementation_guidance"] = implementation
    if resources:
        bp["resources"] = resources

    return bp


PILLAR_TO_FILENAME = {
    "OPERATIONAL_EXCELLENCE": "operational_excellence",
    "SECURITY": "security",
    "RELIABILITY": "reliability",
    "PERFORMANCE_EFFICIENCY": "performance_efficiency",
    "COST_OPTIMIZATION": "cost_optimization",
    "SUSTAINABILITY": "sustainability",
    "UNKNOWN": "general",
}


def main():
    parser = argparse.ArgumentParser(
        description="Ingest a Well-Architected Lens from AWS docs"
    )
    parser.add_argument(
        "lens_slug",
        help="Lens slug from the AWS docs URL (e.g., 'saas-lens', 'serverless-applications-lens')",
    )
    parser.add_argument(
        "--lens-name",
        help="Lens identifier for the 'lens' field (e.g., 'SAAS', 'SERVERLESS'). "
             "Defaults to uppercase slug with hyphens replaced by underscores.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.3,
        help="Delay between HTTP requests in seconds (default: 0.3)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only discover pages, don't fetch or write",
    )

    args = parser.parse_args()
    lens_slug = args.lens_slug
    lens_name = args.lens_name or lens_slug.upper().replace("-", "_").replace("_LENS", "")
    delay = args.delay

    print(f"Lens slug: {lens_slug}")
    print(f"Lens name: {lens_name}")
    print(f"Base URL: {BASE_URL}/{lens_slug}/")
    print()

    # Step 1: Fetch TOC
    print("Fetching table of contents...")
    toc = fetch_toc(lens_slug)

    # Step 2: Discover BP pages
    bp_pages = find_bp_pages(toc, lens_slug)
    print(f"Found {len(bp_pages)} best practice pages")
    print()

    if not bp_pages:
        print("ERROR: No best practice pages found. This lens may use a different structure.")
        print("Check the TOC manually:")
        print(f"  {BASE_URL}/{lens_slug}/toc-contents.json")
        sys.exit(1)

    if args.dry_run:
        print("Dry run — pages discovered:")
        for p in bp_pages:
            print(f"  {p['title_from_toc']}")
            print(f"    -> {p['href']}")
            print(f"    area: {p['area']}")
        return

    # Step 3: Fetch and parse each page
    all_bps: list[dict] = []
    for i, page in enumerate(bp_pages):
        print(f"  [{i + 1}/{len(bp_pages)}] {page['title_from_toc']}")
        bp = ingest_bp_page(page, lens_name)
        if bp:
            all_bps.append(bp)
        time.sleep(delay)

    print(f"\nParsed {len(all_bps)}/{len(bp_pages)} best practices")

    # Step 4: Group by pillar and write files
    output_dir = DATA_DIR / "lens" / lens_slug.replace("-lens", "")
    output_dir.mkdir(parents=True, exist_ok=True)

    by_pillar: dict[str, list[dict]] = {}
    for bp in all_bps:
        pillar = bp["pillar"]
        filename = PILLAR_TO_FILENAME.get(pillar, "general")
        by_pillar.setdefault(filename, []).append(bp)

    print(f"\nWriting to {output_dir}/")
    for filename, practices in sorted(by_pillar.items()):
        output_file = output_dir / f"{filename}.json"
        with open(output_file, "w") as f:
            json.dump(practices, f, indent=2, ensure_ascii=False)
        print(f"  {filename}.json: {len(practices)} best practices")

    # Step 5: Summary
    print(f"\nDone! Ingested {len(all_bps)} best practices into {len(by_pillar)} files.")
    print(f"Output: {output_dir}/")

    enriched = sum(1 for bp in all_bps if "implementation_guidance" in bp)
    print(f"With implementation guidance: {enriched}/{len(all_bps)}")

    # Remind about server.py registration
    print(f"\nNOTE: To enable this lens in the MCP server, add it to the load_data()")
    print(f"function in server.py:")
    print(f"    lens_dir = DATA_DIR / 'lens' / '{lens_slug.replace('-lens', '')}'")


if __name__ == "__main__":
    main()
