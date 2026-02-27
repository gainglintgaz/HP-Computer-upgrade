# MSI M480 PRO 1TB NVMe SSD — Installation & Migration Guide

> **For**: HP Pavilion Desktop 590-p0066
> **SSD Purchased**: MSI SPATIUM M480 PRO PCIe 4.0 NVMe M.2 1TB ($140, Walmart)
> **Goal**: Install SSD, migrate Windows + all apps (Claude Desktop, Cursor, Antigravity), boot from SSD

---

## Before You Start — What You'll Need

| Item | Why |
|------|-----|
| **Phillips #1 screwdriver** | Open the HP case and remove M.2 screw |
| **Anti-static wrist strap** (or touch the metal case before handling parts) | Prevent static damage to the SSD |
| **USB flash drive (8GB+)** | Only needed if doing a clean Windows install |
| **Your Windows product key** (check Settings > System > Activation) | Needed for clean install; not needed for cloning |
| **Cloning software** (free options below) | To copy everything from HDD to SSD |

---

## OPTION A: Clone Your Entire HDD to SSD (Recommended)

This copies **everything** — Windows, all apps (Claude Desktop, Cursor, Antigravity), files, settings — to the new SSD. No reinstalling anything.

### Step 1: Download Cloning Software (Free)

Pick ONE of these (all work well):

| Software | Download | Notes |
|----------|----------|-------|
| **Macrium Reflect Free** | [macrium.com/reflectfree](https://www.macrium.com/reflectfree) | Best free option, very reliable |
| **Clonezilla** | [clonezilla.org](https://clonezilla.org) | Open-source, boot from USB |
| **Samsung Data Migration** | Won't work — MSI drive, not Samsung | N/A |

> **Recommended**: Macrium Reflect Free — easiest for beginners, works with any brand SSD.

### Step 2: Install the SSD (Hardware)

**Power off your PC completely and unplug the power cable.**

1. **Open the case**: Remove the side panel (1 thumb screw on the back)
2. **Locate the M.2 slot**: It's **under the DVD drive** on the HP Lincs motherboard
   - You may need to remove the DVD drive cage (2 screws) to access it
   - The M.2 slot is a small horizontal connector near the bottom of the motherboard
3. **Check for Intel Optane**: If there's a small M.2 drive already installed (16GB Optane cache):
   - **STOP** — You must disable Optane first (see "Optane Removal" section below)
4. **Insert the M480 PRO**:
   - Hold the SSD by its edges (don't touch the gold contacts or chips)
   - Insert at a ~30° angle into the M-Key slot
   - Press down flat and secure with the M.2 mounting screw
5. **Reassemble**: Put the DVD cage back (if removed), close the case
6. **Plug in and power on** — The BIOS should detect the new drive

### Step 3: Clone HDD → SSD

1. **Boot into Windows** normally (still booting from HDD)
2. **Open Disk Management** (Win+X → Disk Management)
   - Verify the M480 PRO shows up as "Unallocated" — this confirms it's detected
   - **Do NOT format it** — the cloning software handles this
3. **Open Macrium Reflect Free**
4. **Select your HDD** (the 1TB source drive with Windows on it)
5. Click **"Clone this disk"**
6. **Select the M480 PRO** as the destination
7. **Resize partitions** if prompted:
   - Drag the main Windows partition to fill the full 1TB of the SSD
   - Keep the small recovery/EFI partitions as-is
8. Click **"Finish"** → **"OK"** to start cloning
9. **Wait** — This takes 30-90 minutes depending on how much data you have

### Step 4: Set SSD as Boot Drive

1. **Restart** the PC
2. **Enter BIOS**: Press **F10** repeatedly as the HP logo appears
3. Go to **Boot Options** or **Boot Order**
4. **Move the MSI M480 PRO to #1** in the boot order (above the HDD)
5. **Save & Exit** (F10 → Yes)
6. Windows should now boot from the SSD — it will be **dramatically faster**

### Step 5: Verify Everything Works

- [ ] Windows boots from SSD (check: Settings → System → Storage → shows NVMe as C: drive)
- [ ] Claude Desktop opens and works
- [ ] Cursor opens and works
- [ ] Antigravity opens and works
- [ ] All your files are intact
- [ ] Internet/WiFi works

### Step 6: Repurpose the Old HDD

Once you've confirmed everything works on the SSD for a few days:

1. Open Disk Management (Win+X → Disk Management)
2. Right-click the old HDD partitions → **Delete Volume** (one at a time)
3. Right-click the unallocated space → **New Simple Volume**
4. Assign it drive letter **D:**
5. Format as **NTFS**, label it "Storage"
6. Use it for: large files, game installs, downloads, backups

---

## OPTION B: Clean Windows Install (Advanced)

Only do this if you want a completely fresh start. You'll need to reinstall all apps.

### Step 1: Create Windows Installation USB

1. On your current PC, download the [Windows Media Creation Tool](https://www.microsoft.com/software-download/windows11)
2. Insert a USB flash drive (8GB+)
3. Run the tool → Create installation media → Select USB flash drive
4. Wait for it to finish

### Step 2: Install the SSD (Same as Option A, Step 2)

### Step 3: Boot from USB & Install Windows

1. Restart → Press **F9** for boot menu
2. Select the **USB drive**
3. Follow the Windows installer
4. When asked "Where do you want to install Windows?": select the **MSI M480 PRO** (the NVMe drive)
5. Complete the installation

### Step 4: Reinstall Your Apps

After clean install, you'll need to reinstall:

| App | Download Link |
|-----|--------------|
| **Claude Desktop** | [claude.ai/download](https://claude.ai/download) |
| **Cursor** | [cursor.com](https://www.cursor.com) |
| **Antigravity** | Reinstall from wherever you originally got it |
| **Chrome/Firefox** | [google.com/chrome](https://www.google.com/chrome) |
| **Your other apps** | Reinstall as needed |

### Step 5: Copy Files from Old HDD

1. Your old HDD will show up as D: drive
2. Copy over: Documents, Pictures, Downloads, Desktop files, etc.

---

## If You Have Intel Optane (16GB M.2 Cache) Installed

Your HP **may** have a 16GB Intel Optane cache drive in the M.2 slot. If so:

1. **Before removing it**, open **Intel Rapid Storage Technology** (search in Start menu)
2. Click **"Disable"** on the Optane acceleration
3. Wait for it to fully disable
4. **Then** shut down and physically swap the Optane for the M480 PRO
5. If Intel RST isn't installed, enter BIOS (F10) → look for Optane settings → Disable

> **Warning**: Removing Optane without disabling it first can make Windows unbootable.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| SSD not detected in BIOS | Re-seat the M.2 drive. Make sure it's fully inserted and screwed down |
| SSD not detected in Windows | Update BIOS from [HP Support](https://support.hp.com/us-en/drivers/hp-pavilion-590-p0000-desktop-pc-series/19390500/model/23205939) |
| Clone fails | Make sure source HDD isn't larger than 1TB used space. Delete temp files first |
| Windows won't boot from SSD | Enter BIOS (F10), set SSD as first boot device |
| "Boot device not found" | Re-clone, making sure EFI partition was included |
| Slow speeds | Expected — your PCIe 3.0 slot caps at ~3,500 MB/s (the M480 PRO's 7,000 MB/s rating is for Gen 4) |

---

## Expected Performance Improvement

| Metric | HDD (Before) | NVMe SSD (After) |
|--------|--------------|-------------------|
| **Windows Boot** | 60-90 seconds | 10-15 seconds |
| **App Launch** (Cursor, Claude) | 15-30 seconds | 2-5 seconds |
| **File Copy Speed** | ~150 MB/s | ~3,500 MB/s |
| **Random Read/Write** | ~1 MB/s | ~500+ MB/s |
| **Overall Responsiveness** | Frequent freezes | Smooth and snappy |

> The SSD upgrade alone should eliminate most of your freezing and crashing issues.
