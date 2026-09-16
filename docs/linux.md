# Add Linux alongside school Windows

[Guide home](../README.md) · Prerequisite: [Preparation](preparation.md)

Ubuntu Desktop LTS is the example used here; use a currently supported release from [Ubuntu](https://ubuntu.com/download/desktop). Other distributions have different installers and hardware support. Check the release's requirements and the [official installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop). This project does not claim a tested PLD/distribution combination.

## Try the hardware first

Create the USB using the distribution's instructions. Boot it in UEFI mode and choose **Try Ubuntu** before installing. Test Wi-Fi, keyboard, touchpad, display, audio, and sleep/wake. A live session is a useful compatibility check, not proof that installation will work. Keep the school Windows volume unmounted and do not unlock it from Linux.

Start with Secure Boot enabled. Some firmware/driver combinations need trust-setting changes or MOK enrolment; others are incompatible with the school’s required configuration. Before changing anything, read [Secure Boot and BitLocker](secure-boot.md): changes can trigger recovery on the original managed Windows partition. Use current device-specific guidance with ICT.

## Resolve installer blockers before writing anything

Ubuntu documents that BitLocker can prevent safe alongside installation. **If an installer asks to turn off BitLocker, do not proceed independently.** Ask ICT whether an approved decryption/re-encryption plan is possible; suspension alone does not decrypt Windows. If preserving school encryption rules makes installation impossible, use an approved alternative.

Similarly, an Intel RST/VMD/storage-controller warning or an invisible SSD requires device-specific help. Switching to AHCI can leave the original Windows unable to boot. Do not experiment with firmware storage settings.

## Use only the space you prepared

1. Confirm the original Windows still starts, your backup is verified, and the post-shrink partition map is available. Disconnect backup drives.
2. Start the installer from the live session. Follow the interactive setup to its storage page.
3. Use an **alongside Windows** option only if its proposed layout clearly uses the already-prepared unallocated space and preserves all existing partitions. If it proposes another Windows resize or does not show enough detail, cancel and ask for help.
4. If manual partitioning is necessary, have an experienced, school-approved helper review it. The intended change is a Linux filesystem (typically ext4 mounted at `/`) in the prepared free space. The existing EFI partition may be mounted at `/boot/efi` **without formatting it**. Windows, MSR, recovery, and OEM partitions must have no format/delete operations. Do not guess partition names such as `/dev/nvme0n1p3` from a tutorial.
5. Review the final write summary against the saved map. **Never select “Erase disk”, “Replace Windows”, “Use entire disk”, or a whole-disk encryption layout.** If it is unclear what will be formatted, go back or cancel.
6. Install, restart, and remove the USB when prompted. Test Linux and then school Windows. Windows might be reachable through the firmware's Windows Boot Manager even if it is absent from Linux's boot menu.

The shared EFI partition can receive Linux boot files; this is a real boot change even when Windows files remain intact. Use the [recovery guide](recovery.md) if the original system does not start.

## Keep personal work separate

Store code and personal applications in Linux's own filesystem and back them up separately. Do not write to the school Windows volume from Linux, especially when Windows is hibernated or Fast Startup is active. Do not force-mount it or remove its hibernation file. Use a full Windows shutdown before switching (for example, hold Shift while selecting Shut down); ask ICT before changing managed power settings.

A browser opening a school site in Linux does not mean Linux has DMA or school compliance. Use the original managed Windows for school lessons, assessments, and required software. Finish the [verification checklist](everyday-use.md).
