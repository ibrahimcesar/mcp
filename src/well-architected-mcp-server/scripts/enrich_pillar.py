#!/usr/bin/env python3
"""Enrich a pillar JSON file by fetching additional content from AWS docs.

Usage:
    python scripts/enrich_pillar.py operational_excellence
"""

import json
import re
import sys
import time
import urllib.request
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "src" / "well_architected_bp_mcp_server" / "data"


def fetch_html(url: str) -> str:
    """Fetch raw HTML from a URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8", errors="replace")


def strip_tags(html: str) -> str:
    """Remove HTML tags and normalize whitespace."""
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_list_items(html: str) -> list[str]:
    """Extract text from <li> elements in an HTML fragment."""
    items = re.findall(r"<li[^>]*>(.*?)</li>", html, re.DOTALL)
    return [strip_tags(item) for item in items if strip_tags(item)]


def extract_section_after_bold(html: str, label: str) -> list[str]:
    """Extract content following a <b>label:</b> pattern.

    If followed by a <ul>, extract list items.
    If inline text, return as single-item list.
    """
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
    """Extract implementation guidance section."""
    # Try h2 with id="implementation-guidance"
    pattern = r'<h2[^>]*id="implementation-guidance"[^>]*>.*?</h2>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)'
    match = re.search(pattern, html, re.DOTALL)

    # Try h2 with id="implementation-steps"
    if not match:
        pattern = r'<h2[^>]*id="implementation-steps"[^>]*>.*?</h2>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)'
        match = re.search(pattern, html, re.DOTALL)

    # Try bold "Implementation steps" label (no h2)
    if not match:
        pattern = r'<b>Implementation steps</b>(.*?)(?=<h2|<div\s+id="resources"|<awsdocs-copyright|\Z)'
        match = re.search(pattern, html, re.DOTALL)

    if not match:
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


def enrich_best_practice(bp: dict) -> dict:
    """Fetch the href and enrich the best practice with additional fields."""
    href = bp.get("href", "")
    if not href:
        return bp

    try:
        html = fetch_html(href)
    except Exception as e:
        print(f"  WARNING: Failed to fetch {bp['id']}: {e}", file=sys.stderr)
        return bp

    desired_outcome = extract_section_after_bold(html, "Desired outcome")
    anti_patterns = extract_section_after_bold(html, "Common anti-patterns")
    benefits = extract_section_after_bold(html, "Benefits of establishing this best practice")
    implementation = extract_implementation(html)
    resources = extract_resources(html)

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


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/enrich_pillar.py <pillar_name>")
        print("Example: python scripts/enrich_pillar.py operational_excellence")
        sys.exit(1)

    pillar = sys.argv[1]
    input_file = DATA_DIR / f"{pillar}.json"

    if not input_file.exists():
        print(f"ERROR: {input_file} not found", file=sys.stderr)
        sys.exit(1)

    with open(input_file) as f:
        data = json.load(f)

    print(f"Enriching {len(data)} best practices from {pillar}...")

    for i, bp in enumerate(data):
        print(f"  [{i + 1}/{len(data)}] {bp['id']} - {bp['title']}")
        enrich_best_practice(bp)
        time.sleep(0.3)

    output_file = DATA_DIR / f"{pillar}.json"
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone! Wrote enriched data to {output_file}")

    enriched = sum(1 for bp in data if "desired_outcome" in bp or "implementation_guidance" in bp)
    print(f"Successfully enriched: {enriched}/{len(data)} practices")


if __name__ == "__main__":
    main()
