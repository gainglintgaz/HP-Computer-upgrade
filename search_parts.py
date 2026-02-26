#!/usr/bin/env python3
"""
Computer Parts & PC Search Tool
================================
Generates direct search URLs for computer parts and prebuilt PCs
from reputable retailers. Run this script to get up-to-date links
for shopping across all major retailers including warehouse clubs.

Usage:
    python3 search_parts.py                    # Show all categories
    python3 search_parts.py --ssd              # NVMe SSD deals only
    python3 search_parts.py --ram              # DDR4 RAM deals only
    python3 search_parts.py --pc               # Prebuilt PC deals only
    python3 search_parts.py --all              # Everything
    python3 search_parts.py --custom "RTX 5070 Ti"  # Custom search term
"""

import argparse
import urllib.parse
from datetime import datetime

# ==============================================================================
# CONFIGURATION — Edit these to change your search parameters
# ==============================================================================

# Your HP Pavilion 590-p0066 compatibility
COMPATIBLE_SSD_SPECS = {
    "form_factor": "M.2 2280",
    "interface": "PCIe NVMe (Gen 3/4/5 all work, runs at Gen 3 speed)",
    "min_capacity": "1TB",
    "key_type": "M-Key",
}

COMPATIBLE_RAM_SPECS = {
    "type": "DDR4 UDIMM 288-pin",
    "speed": "DDR4-2666 (PC4-21300)",
    "max_capacity": "32GB (2x16GB)",
    "slots": 2,
    "voltage": "1.2V",
    "ecc": "Non-ECC",
}

NEW_PC_MIN_SPECS = {
    "cpu": "Intel Core i7 / AMD Ryzen 7 or better",
    "gpu": "NVIDIA RTX 5060 (8GB VRAM) minimum, RTX 5070+ preferred",
    "ram": "32GB DDR5 minimum",
    "storage": "1TB NVMe SSD minimum, 2TB preferred",
    "use_case": "AI Vibe Coding (Claude Code, Cursor, Antigravity)",
}

# ==============================================================================
# RETAILER SEARCH URL TEMPLATES
# ==============================================================================

RETAILERS = {
    # --- Major Retailers ---
    "Amazon": {
        "search": "https://www.amazon.com/s?k={query}",
        "trust_rank": 1,
        "return_policy": "30 days",
    },
    "Best Buy": {
        "search": "https://www.bestbuy.com/site/searchpage.jsp?st={query}",
        "trust_rank": 2,
        "return_policy": "15 days (60 for members)",
    },
    "Newegg": {
        "search": "https://www.newegg.com/p/pl?d={query}",
        "trust_rank": 3,
        "return_policy": "30 days",
    },
    "Micro Center": {
        "search": "https://www.microcenter.com/search/search_results.aspx?Ntt={query}",
        "trust_rank": 4,
        "return_policy": "30 days",
    },
    "B&H Photo": {
        "search": "https://www.bhphotovideo.com/c/search?q={query}",
        "trust_rank": 5,
        "return_policy": "30 days",
    },
    "Walmart": {
        "search": "https://www.walmart.com/search?q={query}",
        "trust_rank": 6,
        "return_policy": "30 days",
    },
    # --- Warehouse Clubs ---
    "Costco": {
        "search": "https://www.costco.com/CatalogSearch?dept=All&keyword={query}",
        "trust_rank": 7,
        "return_policy": "90 days electronics",
        "note": "Membership required ($60/yr). Best electronics return policy.",
    },
    "Sam's Club": {
        "search": "https://www.samsclub.com/s/{query}",
        "trust_rank": 8,
        "return_policy": "90 days electronics",
        "note": "Membership required ($50/yr). Plus = free shipping.",
    },
    "BJ's Wholesale": {
        "search": "https://www.bjs.com/search/{query}",
        "trust_rank": 9,
        "return_policy": "Varies",
        "note": "Membership required. Limited PC parts selection.",
    },
    # --- Deal Aggregators ---
    "Slickdeals": {
        "search": "https://slickdeals.net/newsearch.php?q={query}&searcharea=deals",
        "trust_rank": 10,
        "return_policy": "N/A (deal aggregator)",
    },
    "PCPartPicker": {
        "search": "https://pcpartpicker.com/search/?q={query}",
        "trust_rank": 10,
        "return_policy": "N/A (price comparison)",
    },
}

# ==============================================================================
# SEARCH QUERIES
# ==============================================================================

SSD_SEARCHES = [
    "1TB NVMe M.2 2280 SSD",
    "2TB NVMe M.2 2280 SSD",
    "Samsung 990 EVO 1TB",
    "Samsung 990 Pro 1TB",
    "WD Blue SN580 1TB",
    "Crucial P3 1TB NVMe",
    "Crucial P3 Plus 1TB",
    "WD Black SN850X 2TB",
]

RAM_SEARCHES = [
    "32GB DDR4-2666 UDIMM desktop",
    "Crucial CT2K16G4DFRA266",
    "Corsair Vengeance LPX 32GB DDR4 2666",
    "G.SKILL Aegis 32GB DDR4 2666",
    "16GB DDR4-2666 UDIMM",
]

PC_SEARCHES = [
    "RTX 5070 32GB desktop PC",
    "RTX 5060 32GB desktop",
    "gaming desktop 32GB DDR5 RTX 5070",
    "CyberPowerPC RTX 5070",
    "prebuilt desktop RTX 5070 Ti 32GB",
    "AI workstation desktop 32GB",
]

# Price tracking and deal sites
DEAL_TRACKING = {
    "Tom's Hardware SSD Tracker": "https://www.tomshardware.com/pc-components/ssds/ssd-price-tracking-2026-lowest-price-on-every-m-2-ssd",
    "Tom's Hardware Gaming PC Deals": "https://www.tomshardware.com/desktops/gaming-pcs/best-gaming-pc-deals",
    "Slickdeals SSD": "https://slickdeals.net/deals/ssd/",
    "Slickdeals RAM": "https://slickdeals.net/newsearch.php?q=32gb+ddr4+2666&searcharea=deals",
    "PCPartPicker DDR4-2666": "https://pcpartpicker.com/products/memory/#S=2666&Z=32768002",
    "Newegg RTX 50 Series PCs": "https://www.newegg.com/p/pl?N=100897449+601468988",
    "Best Buy RTX 5070 Desktops": "https://www.bestbuy.com/site/searchpage.jsp?browsedCategory=pcmcat287600050002&qp=graphicscardsv_facet%3DVideo+Card~NVIDIA+GeForce+RTX+5070",
    "Costco Gaming Desktops": "https://www.costco.com/desktops-servers.html?brand=cyberpowerpc&computer-type=gaming",
    "Sam's Club Gaming Desktops": "https://www.samsclub.com/b/gaming-desktops/14490102",
    "BJ's Desktop Deals": "https://www.bjs.com/category/wow-deals/tvs-and-tech-deals/computers-and-tablets-deals/",
}


def generate_urls(query: str) -> list[dict]:
    """Generate search URLs for all retailers for a given query."""
    results = []
    encoded = urllib.parse.quote_plus(query)
    for name, info in RETAILERS.items():
        url = info["search"].format(query=encoded)
        results.append({
            "retailer": name,
            "url": url,
            "trust_rank": info["trust_rank"],
            "return_policy": info["return_policy"],
            "note": info.get("note", ""),
        })
    return sorted(results, key=lambda x: x["trust_rank"])


def print_header(title: str):
    """Print a formatted header."""
    width = 80
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)


def print_search_results(category: str, searches: list[str], retailers_to_use: list[str] | None = None):
    """Print formatted search URLs for a category."""
    print_header(f"{category} — Search Links")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    for query in searches:
        print(f"  >> {query}")
        print(f"  {'─' * 60}")
        urls = generate_urls(query)
        for r in urls:
            if retailers_to_use and r["retailer"] not in retailers_to_use:
                continue
            note = f"  ({r['note']})" if r["note"] else ""
            print(f"     {r['retailer']:15s} {r['url']}{note}")
        print()


def print_deal_trackers():
    """Print links to deal tracking sites."""
    print_header("DEAL TRACKING & PRICE COMPARISON SITES")
    print("  Check these daily for flash sales and price drops:\n")
    for name, url in DEAL_TRACKING.items():
        print(f"  {name:40s} {url}")
    print()


def print_compatibility_info():
    """Print your HP's compatibility specs."""
    print_header("YOUR HP PAVILION 590-p0066 — COMPATIBILITY SPECS")
    print("\n  NVMe SSD Requirements:")
    for key, val in COMPATIBLE_SSD_SPECS.items():
        print(f"    {key:20s}: {val}")
    print("\n  RAM Requirements:")
    for key, val in COMPATIBLE_RAM_SPECS.items():
        print(f"    {key:20s}: {val}")
    print("\n  New PC Minimum Specs (for AI Vibe Coding):")
    for key, val in NEW_PC_MIN_SPECS.items():
        print(f"    {key:20s}: {val}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Computer Parts & PC Search Tool for HP Pavilion 590-p0066 Upgrade"
    )
    parser.add_argument("--ssd", action="store_true", help="Show NVMe SSD search links")
    parser.add_argument("--ram", action="store_true", help="Show DDR4 RAM search links")
    parser.add_argument("--pc", action="store_true", help="Show prebuilt PC search links")
    parser.add_argument("--deals", action="store_true", help="Show deal tracking links")
    parser.add_argument("--specs", action="store_true", help="Show compatibility specs")
    parser.add_argument("--all", action="store_true", help="Show everything")
    parser.add_argument("--custom", type=str, help="Custom search query across all retailers")

    args = parser.parse_args()

    # Default to showing everything if no flags
    show_all = args.all or not any([args.ssd, args.ram, args.pc, args.deals, args.specs, args.custom])

    print("\n" + "+" * 80)
    print("+  COMPUTER PARTS & PC SEARCH TOOL")
    print(f"+  Date: {datetime.now().strftime('%Y-%m-%d')}")
    print("+  Target: HP Pavilion 590-p0066 Upgrade + New AI Coding PC")
    print("+" * 80)

    if show_all or args.specs:
        print_compatibility_info()

    if show_all or args.ssd:
        print_search_results("NVMe SSDs (1TB+ M.2 2280)", SSD_SEARCHES)

    if show_all or args.ram:
        print_search_results("DDR4-2666 RAM (32GB Kits)", RAM_SEARCHES)

    if show_all or args.pc:
        print_search_results(
            "Prebuilt Desktops for AI Coding",
            PC_SEARCHES,
        )

    if show_all or args.deals:
        print_deal_trackers()

    if args.custom:
        print_search_results(f"Custom Search: '{args.custom}'", [args.custom])

    print("\n" + "-" * 80)
    print("  TIP: Prices change daily. Check Tom's Hardware SSD Tracker and Slickdeals")
    print("  for the latest flash sales. Newegg's 25th Anniversary Sale is active now!")
    print("-" * 80 + "\n")


if __name__ == "__main__":
    main()
