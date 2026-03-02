# HP Computer Upgrade & Replacement — Shopping Guide

Structured shopping guide for upgrading an HP Pavilion Desktop 590-p0066 and finding a new AI-capable desktop PC for vibe coding with Claude Code, Cursor, and Antigravity.

## Upgrade Progress

| Part | Status | Price | Notes |
|------|--------|-------|-------|
| **NVMe SSD** | BOUGHT | $140 | MSI SPATIUM M480 PRO 1TB (Walmart) |
| **RAM** | SHOPPING | ~$139–$243 | 32GB DDR4-3200 (downclocks to 2666). CL22 ~$139, CL16 ~$230-$243. See [PARTS_DEALS.md](PARTS_DEALS.md) |

## Files

| File | Description |
|------|-------------|
| [SSD_INSTALL_GUIDE.md](SSD_INSTALL_GUIDE.md) | Step-by-step SSD installation and Windows/app migration guide |
| [COMPATIBILITY_GUIDE.md](COMPATIBILITY_GUIDE.md) | Your HP's specs, compatible parts, and upgrade constraints |
| [PARTS_DEALS.md](PARTS_DEALS.md) | NVMe SSD and DDR4 RAM deals sorted by price, reputation, and rating |
| [NEW_COMPUTER_DEALS.md](NEW_COMPUTER_DEALS.md) | Prebuilt desktop PCs from Costco, Sam's Club, BJ's, Best Buy, Newegg, and more |
| [PROJECT_HISTORY.md](PROJECT_HISTORY.md) | Full build story, architecture decisions, and price accuracy notes |
| [search_parts.py](search_parts.py) | Reusable search tool — generates live retailer URLs for parts and PCs |

## Quick Start

```bash
# Show all search links across all retailers
python3 search_parts.py

# Search specific categories
python3 search_parts.py --ssd          # NVMe SSD deals
python3 search_parts.py --ram          # DDR4 RAM deals
python3 search_parts.py --pc           # Prebuilt PCs for AI coding
python3 search_parts.py --deals        # Price tracker links
python3 search_parts.py --specs        # Your HP's compatibility info

# Custom search across all retailers
python3 search_parts.py --custom "RTX 5070 Ti 32GB"
```

## Top Recommendations

### Upgrade Your HP Now (~$279-$383 total)
1. **MSI M480 PRO 1TB NVMe** — $140 (BOUGHT)
2. **Budget RAM: Crucial 32GB DDR4-3200 CL22** — ~$139 (CL22 is fine for your HP)
3. **Premium RAM: Corsair Vengeance LPX 32GB DDR4-3200 CL16** — ~$230-$243 (faster, better for reuse)

### Best New PC for AI Vibe Coding
- **Budget ($849–$1,100)**: CyberPowerPC Gamer Xtreme at Costco
- **Mid-range ($1,599–$1,649)**: MSI Aegis Z2 (RTX 5070 or 5070 Ti) on Newegg — $500+ off
- **High-end ($1,899–$1,999)**: iBUYPOWER 7800X3D + RTX 5070 Ti on Newegg

## Market Warning (March 2026)
NAND and DRAM prices have surged due to AI datacenter demand. CL16 DDR4 32GB kits now cost $230-$300+ (was $45-65 in 2025). CL22 kits are ~$139. Prebuilts offer significantly better value than DIY builds. Buy sooner rather than later.
