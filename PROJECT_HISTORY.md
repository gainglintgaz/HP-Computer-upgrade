# Project History & Analysis

> **Created:** March 2, 2026
> **Site:** [gainglintgaz.github.io/HP-Computer-upgrade](https://gainglintgaz.github.io/HP-Computer-upgrade/)

---

## What Is This Project?

An interactive shopping guide and decision-support tool for:

1. **Upgrading** an HP Pavilion Desktop 590-p0066 (adding NVMe SSD + 32GB RAM)
2. **Replacing** it with a new AI-capable prebuilt desktop for vibe coding with Claude Code, Cursor, and Antigravity

It's a static GitHub Pages site — no frameworks, no backend, just vanilla HTML/CSS/JS.

---

## Why It Was Built

The HP Pavilion (i5-8400, 12GB DDR4, 1TB HDD, no SSD) was **freezing and crashing** under modern AI coding workloads. The project needed to answer:

- What parts are actually **compatible** with the HP's proprietary motherboard
- Whether to **upgrade** (~$170-230) or **buy new** (~$850-2,000)
- Where to find the **best deals** during the Feb/March 2026 DRAM/NAND price crisis
- Whether **DIY building** makes sense vs. prebuilts (prebuilts win in 2026)

The project turns messy shopping research into **structured, sortable, searchable data**.

---

## How It Was Built — Commit by Commit

### Commit 1: `5460ba7` — Foundation

**"Add computer parts search tool and structured shopping guides"**

Created in one commit:

| File | Purpose |
|------|---------|
| `README.md` | Project overview, quick-start, top recommendations |
| `COMPATIBILITY_GUIDE.md` | HP 590-p0066 full specs + upgrade constraints (M.2 2280 PCIe 3.0, DDR4-2666, 2 DIMM slots) |
| `PARTS_DEALS.md` | 8 SSDs + 7 RAM kits with prices, specs, ratings, buy links |
| `NEW_COMPUTER_DEALS.md` | 11+ prebuilt PCs across Costco, Sam's Club, Best Buy, Newegg, Amazon |
| `search_parts.py` | Python CLI tool that generates live search URLs for 11 retailers |

**Why:** Needed a single source of truth instead of 50 browser tabs. The Python tool generates instant search links for Amazon, Best Buy, Newegg, Micro Center, B&H, Walmart, Costco, Sam's Club, BJ's, Slickdeals, and PCPartPicker.

---

### Commit 2: `be11ba5` — The Website

**"Add interactive web page and GitHub Pages deployment"**

Built the entire `docs/index.html` (1,081 lines) and `.github/workflows/pages.yml`:

- **7 tabbed sections**: Overview, NVMe SSDs, DDR4 RAM, New PCs, Warehouse Clubs, Search Tool, HP Specs
- **Sortable/filterable tables** — click any column header to sort, type to filter
- **Live retailer search** — type a query, get instant buy links for 11+ stores
- **Quick search buttons** — pre-loaded searches for common queries
- **Dark theme** — GitHub Primer-inspired design, responsive down to mobile
- **GitHub Actions** — auto-deploys on push to the branch

**Tech choices:**
- Vanilla JS (79 lines) — no React/Vue needed for a shopping guide
- CSS variables for consistent theming
- Zero dependencies, zero build step
- Everything in a single self-contained HTML file

---

### Commit 3: `6f68f92` — SSD Install Guide + Price Updates

**"Add SSD install guide, update RAM pricing for Feb 2026"**

- Created `SSD_INSTALL_GUIDE.md` with step-by-step hardware installation
- Two migration paths: **Option A** (clone HDD to SSD) and **Option B** (clean Windows install)
- Intel Optane cache handling (must disable RST first)
- Troubleshooting table for common issues
- **Marked SSD as purchased** (MSI SPATIUM M480 PRO 1TB, $140 at Walmart)
- Updated RAM pricing — discovered AI-driven DRAM shortage spiked 32GB DDR4 from ~$60-80 to ~$240-260

---

### Commits 4-5: `c39e9e3` + `36332ff` — RAM Price Corrections

**"Fix RAM pricing to reflect real Feb 2026 costs, add DDR4-3200 strategy"**

- Corrected all 32GB DDR4 kits to real ~$240-260 range
- Key insight: **DDR4-3200 kits cost the same as DDR4-2666** but auto-downclock in the HP, giving better specs for free if the RAM moves to a new build later
- Recommended **Corsair Vengeance LPX DDR4-3200 CL16** as the best pick
- Added V-Color, KingSpec budget alternatives

---

## Architecture

```
GitHub Pages (static)
│
├── docs/index.html              ← The website (all-in-one HTML/CSS/JS)
│   ├── Tab navigation           ← 7 sections
│   ├── Sortable tables          ← SSDs, RAM, PCs with click-to-sort
│   ├── Filter inputs            ← Real-time text filtering
│   ├── Retailer search          ← Generates URLs for 11 stores
│   └── Dark theme               ← CSS variables, responsive
│
├── Markdown guides              ← Deep-dive content
│   ├── COMPATIBILITY_GUIDE.md   ← HP specs + constraints
│   ├── SSD_INSTALL_GUIDE.md     ← Hardware + software setup
│   ├── PARTS_DEALS.md           ← Component comparisons
│   └── NEW_COMPUTER_DEALS.md    ← Prebuilt PC comparisons
│
├── search_parts.py              ← CLI search tool (11 retailers)
│
└── .github/workflows/pages.yml  ← Auto-deploy on push
```

---

## File Inventory

| File | Lines | Size | Purpose |
|------|-------|------|---------|
| `docs/index.html` | 1,081 | ~58 KB | Interactive website with 7 tabs, sorting, filtering, search |
| `PARTS_DEALS.md` | ~350 | ~13 KB | SSD + RAM comparisons with specs, prices, buy links |
| `search_parts.py` | ~280 | ~10 KB | Python CLI for generating retailer search URLs |
| `NEW_COMPUTER_DEALS.md` | ~250 | ~9 KB | Prebuilt PC comparisons (11+ options) |
| `SSD_INSTALL_GUIDE.md` | ~200 | ~8 KB | Step-by-step hardware install + cloning guide |
| `COMPATIBILITY_GUIDE.md` | ~100 | ~3 KB | HP 590-p0066 specs + upgrade constraints |
| `README.md` | ~70 | ~2 KB | Quick-start and navigation |
| `.github/workflows/pages.yml` | 40 | ~1 KB | GitHub Actions deploy config |

---

## Key Design Decisions

| Decision | Reasoning |
|----------|-----------|
| **Single HTML file** | No build tools, no dependencies, instant load, easy to maintain |
| **Vanilla JS over React** | Shopping guide doesn't need a SPA framework — 79 lines does it all |
| **Dark theme** | Matches developer terminal aesthetic |
| **Markdown + HTML dual format** | Markdown for detailed reading on GitHub, HTML for interactive browsing |
| **Python search tool** | CLI alternative for power users; generates same retailer URLs as the website |
| **Embedded data over API calls** | No CORS issues, no API keys, works offline, loads instantly |
| **GitHub Actions deploy** | Push-to-deploy, zero config, free hosting |

---

## Key Findings

### DIY vs. Prebuilt (March 2026)

| Option | Cost | Verdict |
|--------|------|---------|
| DIY matching Skytech Crystal (Arc B580) | ~$1,337 | $237 MORE than the prebuilt |
| DIY matching CyberPowerPC (RTX 5060) | ~$1,497 | $397 MORE than the prebuilt |
| Skytech Crystal (Costco) | $1,100 | Decent, but weaker GPU |
| **CyberPowerPC Gamer Xtreme (Costco)** | **$1,100** | **Best value — RTX 5060, 32GB DDR5, 2TB SSD** |

**Prebuilts beat DIY in 2026** because manufacturers locked in bulk pricing before the AI-driven DRAM/NAND shortage. Individual buyers pay 3-4x more for RAM alone.

### Component Price Crisis (Feb/March 2026)

| Component | 2024 Price | 2026 Price | Change |
|-----------|-----------|-----------|--------|
| 32GB DDR5 | ~$80-93 | ~$330-500 | ~4x increase |
| 32GB DDR4 | ~$45-60 | ~$240-260 | ~4x increase |
| 1TB NVMe SSD | ~$55-66 | ~$110-120 | ~2x increase |
| 2TB NVMe SSD | ~$100-120 | ~$200-250 | ~2x increase |

### DDR4-3200 Strategy

DDR4-3200 kits cost the same as DDR4-2666 (~$240-260) but auto-downclock to 2666MHz in the HP. If the RAM moves to a newer PC later, it runs at its full 3200MHz speed — free future-proofing.

---

## Price Accuracy Warning

> **NOTE (March 2, 2026):** Many prices listed in `PARTS_DEALS.md`, `NEW_COMPUTER_DEALS.md`, and `docs/index.html` may be **inaccurate or outdated**. The component market in early 2026 is extremely volatile due to AI-driven demand. Prices change daily. Always verify current pricing using the retailer links and price trackers provided before purchasing.
>
> Known issues:
> - Some SSD prices may still reflect late-2024/early-2025 pricing
> - Some prebuilt PC prices may have changed since initial research
> - RAM prices are fluctuating weekly during the shortage
> - GPU availability and street prices vary significantly from MSRP
>
> **Always use the Search Tool tab or `search_parts.py` to check live retailer prices before buying.**

---

## Recommendations Summary

### Best Path: Upgrade + Buy New Later

1. **Now:** Upgrade the HP with SSD ($140, already purchased) + 32GB DDR4-3200 RAM (~$240-260) = **~$400 total**
2. **Later:** When DRAM/NAND prices normalize (late 2026?), buy a prebuilt or build custom

### If Buying New Now

- **Under $1,100:** CyberPowerPC Gamer Xtreme at Costco (RTX 5060, 32GB DDR5, 2TB SSD)
- **$1,500-1,700:** MSI Aegis Z2 on Newegg (RTX 5070, 32GB DDR5, 2TB)
- **$1,700-2,000:** iBUYPOWER with RTX 5070 Ti 16GB (best for local AI models)

### Do NOT Build Custom in 2026

DIY costs $200-400 more than equivalent prebuilts due to the component shortage. OEMs buy at bulk pricing that individual consumers cannot access.
