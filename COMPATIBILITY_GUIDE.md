# HP Pavilion Desktop 590-p0066 — Compatibility & Upgrade Guide

## Your Current System Specs

| Component       | Current Spec                              |
|-----------------|-------------------------------------------|
| **Model**       | HP Pavilion Desktop 590-p0066             |
| **Motherboard** | HP Lincs (Intel H370 chipset)             |
| **CPU**         | Intel Core i5-8400 (6 cores, 2.8GHz)     |
| **RAM**         | 12GB DDR4-2666 (1x4GB + 1x8GB)           |
| **Storage**     | 1TB 7200RPM HDD (no SSD)                 |
| **GPU**         | Intel UHD Graphics 630 (integrated)       |
| **Form Factor** | Micro-ATX (24.9 x 26.7 cm)               |
| **CPU Socket**  | LGA1151 (Coffee Lake)                     |
| **Age**         | ~6 years old                              |

## Why Your PC Is Freezing and Crashing

1. **No SSD**: Your system boots from a slow 7200RPM HDD — this is the #1 bottleneck
2. **Only 12GB RAM**: AI/vibe coding tools (Cursor, Claude Code, Antigravity) are RAM-hungry. 12GB is insufficient
3. **Mismatched RAM**: 4GB + 8GB sticks means single-channel mode for 8GB, reducing bandwidth
4. **Aging CPU**: The i5-8400 is 6+ generations old and struggles with modern multi-threaded workloads

## Compatible Upgrade Specs

### NVMe SSD Slot
| Spec              | Requirement                                |
|-------------------|--------------------------------------------|
| **Form Factor**   | M.2 2280 (80mm length)                    |
| **Interface**     | PCIe 3.0 x4 NVMe (M-Key)                 |
| **Max Slots**     | 1 (located under DVD drive)               |
| **SATA M.2?**     | NO — SATA M.2 drives will NOT work        |
| **PCIe Gen 4/5?** | Yes — backwards compatible at Gen 3 speeds |
| **Max Speed**     | ~3,500 MB/s (PCIe 3.0 x4 limit)           |

> **Important**: If your system has a 16GB Intel Optane M.2 cache drive, you must disable Optane in Intel RST before replacing it with an NVMe SSD.

### RAM Slots
| Spec              | Requirement                                |
|-------------------|--------------------------------------------|
| **Type**          | DDR4 UDIMM, 288-pin, Non-ECC              |
| **Speed**         | DDR4-2666 (PC4-21300)                     |
| **Max Capacity**  | 32GB (2 x 16GB)                           |
| **Slots**         | 2                                          |
| **Voltage**       | 1.2V                                       |
| **Channels**      | Dual-channel (use matching pair)           |

> **Note**: DDR4-3200 sticks will work but will downclock to 2666MHz. Buy DDR4-2666 to save money.

### Sources
- [HP Support — Lincs Motherboard Specs](https://support.hp.com/za-en/product/hp-pavilion-590-p0000-desktop-pc-series/19390500/model/23205939/document/c05991291)
- [Crucial Compatibility Page](https://www.crucial.com/compatible-upgrade-for/hp/pavilion-590-p0066)
- [HP Community — SSD Compatibility](https://h30434.www3.hp.com/t5/Desktop-Hardware-and-Upgrade-Questions/What-type-of-SSD-does-HP-590-p0066-support/td-p/6913311)
- [HP Community — RAM Upgrade](https://h30434.www3.hp.com/t5/Desktop-Hardware-and-Upgrade-Questions/Upgrade-RAM-on-Pavilion-590-p0066/td-p/8214580)
