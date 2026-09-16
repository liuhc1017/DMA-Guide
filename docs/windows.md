# Add a second Windows 11 installation

[Guide home](../README.md) · Prerequisite: [Preparation](preparation.md)

## Choose Home for personal use or Pro for school enrolment

| Intended installation | Edition to discuss with ICT | Setup route |
| --- | --- | --- |
| Approved personal Windows environment for coding and apps | Windows 11 Home | Personal setup using a valid Home licence |
| Additional school-managed environment | Windows 11 Pro or Pro Education, as specified by school | School setup and MIMS sign-in; see [enrolment](school-enrolment.md) |

Home is an option for the personal partition, **not a guarantee of “no DMA”**. Edition selection does not remove device registration or school policy, and management software may still be installed. Preserve the original managed installation and follow the agreed use of the second OS. Pro Education is a distinct edition from both Pro and Education; obtain the appropriate media and entitlement from ICT.

## Get official installation media

Windows 11 **Pro** is the edition commonly called “Professional”. Download official installation media from [Microsoft](https://www.microsoft.com/en-us/software-download/windows11). The x64 multi-edition ISO can install Pro; the downloaded ISO itself does not grant a licence. Use the media creation tool or ISO route, not Installation Assistant, which upgrades the currently running installation.

![Microsoft's Windows 11 ISO download section](../assets/screenshots/windows-iso-download.png)
*February 2026 example: locate the ISO section on the current official page.*

![The x64 multi-edition Windows 11 ISO selected in Microsoft's download menu](../assets/screenshots/windows-iso-selection.png)
*This guide covers Intel/AMD x64 hardware. The separate Arm64 download is not interchangeable.*

Obtain a genuine licence for the chosen edition from Microsoft/an authorised seller or ask ICT whether your school provides an entitlement for this particular installation. Do not assume the original OEM licence covers an additional installed copy, or that activation proves entitlement. Check the terms of the licence you are actually using. MIMS access and Microsoft 365/Office access do not establish a Windows Pro licence.

When Setup offers an edition list, select the edition matching your licence and intended use. A firmware key can select an edition automatically. See [Microsoft activation guidance](https://support.microsoft.com/en-gb/windows/activate-windows-c39005d4-95ee-b91e-b399-2820fda32227); selecting an edition and activating it are separate steps.

## Select Home using ei.cfg and PID.txt

For an approved personal installation, the Home edition ID is `Core` (often written “CORE”). First create the USB from official multi-edition media that includes Home. These files affect **new installations from that USB**, not the existing school Windows.

Save this retail, non-volume Home example as `ei.cfg` in the USB's `sources` folder:

```ini
[EditionID]
Core
[Channel]
Retail
[VL]
0
```

Use `Retail` only for matching retail media/licensing; ask ICT or the supplier about another channel. If you also want Setup to read the installation key from a file, save `PID.txt` beside it:

```ini
[PID]
Value=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
```

**Replace the placeholder with your valid Home installation key; the Xs are not a working key.** `PID.txt` is optional if you enter the key in Setup. It does not activate Windows or grant a licence. The key must match an edition in the image. An unattended answer file takes precedence over these files. [Microsoft documents these formats and behaviour](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-edition-configuration-and-product-id-files--eicfg-and-pidtxt?view=windows-11).

In Notepad, select **All files** when saving. Enable filename extensions in File Explorer and check that the files are not accidentally named `ei.cfg.txt` or `PID.txt.txt`.

```text
Installer USB/
└── sources/
    ├── ei.cfg
    └── PID.txt    ← optional; contains a private key when completed
```

Check the edition shown by Setup before continuing. If it disagrees or rejects the key, cancel and check the media, edition, channel, and key. Do not alter partitions to fix an edition error. Delete a completed `PID.txt` before sharing/reusing the USB, and remove the Home configuration before using it to install school Pro/Pro Education. Never commit or screenshot a real key.

## Install only into the new space

1. Disconnect backup and nonessential external disks. Boot the installer USB using the one-time **UEFI** boot menu.
2. Choose language and keyboard settings. Follow the new-installation path; on installers offering **Custom: Install Windows only**, choose it. UI wording varies by release.
3. At the disk selection screen, identify the internal SSD using the recorded capacity and partition layout. Select **only the unallocated space created in preparation**. Do not select the original Windows volume or any existing “Primary”, EFI/System, MSR/Reserved, Recovery, or OEM partition.
4. **Stop before confirming:** the unallocated capacity must match the plan, all original partitions must remain, and no instruction should require deleting them. A general clean-install tutorial may tell you to delete every partition; that is incompatible with this guide. If the intended space is missing or ambiguous, cancel.
5. Allow Setup to create what it needs in the selected space. It may also update shared EFI boot files. If it cannot proceed without changing/deleting existing partitions, stop for ICT support.
6. Keep AC power connected. After Setup's first restart, let it continue from the internal drive instead of starting the USB installer again. Remove the USB when appropriate.
7. Complete the supported Windows setup flow. If school branding or a mandatory organisational setup appears, follow school instructions or contact ICT; do not try to remove the device's registration. For an approved personal installation, use the agreed personal-account setup. For a school-enrolled installation, follow [MIMS and DMA enrolment](school-enrolment.md).
8. Install Windows updates and exact-model OEM drivers from official sources. Check activation. If network/storage drivers are missing, use the manufacturer's package or ask ICT; do not change RAID/RST/VMD settings as a shortcut.

Two Windows installations may both display “Windows 11” and each may call its own system volume `C:`. Identify them by actually booting and checking their files and accounts, then record the mapping. Never rename or delete an entry by guessing.

**Before installing personal apps, boot the original Windows and complete the [verification checklist](everyday-use.md).**
