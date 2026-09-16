# Recovery and rollback

[Guide home](../README.md) · Save an offline copy before installation

**Priority: recover school access and preserve data.** Keep AC power connected. If you suspect a partition was deleted or overwritten, stop using the disk and contact ICT or a suitable data-recovery professional. Reinstalling, formatting, or repeatedly running repair tools can reduce the chance of recovery.

## 1. Try the existing school boot path

Remove the installer USB and unnecessary external devices. Use the manufacturer's permitted one-time boot menu and select **Windows Boot Manager** on the internal disk. With two Windows installations, choose the previously identified original entry. Do not delete other entries or reset firmware defaults.

If school Windows starts, back up new files immediately, check DMA and school access, and ask ICT to help restore the default boot choice. Avoid further partition work until the problem is understood.

## 2. Handle a BitLocker prompt

Record the recovery-key ID privately and obtain the matching key through the school's approved route. A school-managed key may be held by ICT; it may not be in your personal Microsoft account. See [Microsoft's recovery-key guidance](https://support.microsoft.com/en-us/windows/finding-your-bitlocker-recovery-key-in-windows-6b71ad27-0b89-ea08-f143-056f5ab347d6).

Do not post the 48-digit key, clear the TPM, or choose Reset because you cannot find the key. There is no recovery-key replacement in this repository. If prompts recur, ask ICT to review the boot/encryption configuration rather than repeatedly changing firmware settings.

## 3. Use Windows repair with ICT

If the correct Windows boot path fails, ask ICT about **Windows Recovery Environment → Troubleshoot → Advanced options → Startup Repair**. If local WinRE is unavailable, approved Windows installation media may offer **Repair your computer**. Select the original Windows installation carefully; a recovery key may be required.

Startup Repair changes boot configuration and may affect the second OS's menu. Have ICT review the result. This guide deliberately does not prescribe generic `bootrec`, `bcdboot`, GRUB repair, or partition commands: drive letters and boot layouts differ, and the wrong target can make matters worse. See [Microsoft's recovery options](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows).

## 4. Restore only with a known recovery plan

If repair fails, use the school/OEM procedure agreed before installation. Confirm exactly which partitions it erases and back up accessible data from both operating systems before proceeding. A school image may restore DMA but erase personal partitions; a generic Microsoft reinstall may restore Windows without restoring DMA or school access.

**“Reset this PC”, including “Keep my files”, is not a way to preserve installed apps, DMA, and all school configuration.** Do not assume it or an OEM factory recovery preserves either OS. After a reimage, complete school-directed enrolment and have ICT verify access and compliance before returning to normal school use.

## Remove the second OS later

The safest immediate rollback is to make the verified original Windows the default and leave the second OS's partitions alone until ICT can review them.

For permanent removal:

1. Back up personal work from the second OS off the device.
2. Prove the original Windows starts via Windows Boot Manager independently of the Linux menu, or via its identified Windows entry. Confirm recovery readiness.
3. Have ICT/an experienced authorised helper compare the before/after maps and identify **only** partitions created for the second OS. Never delete the shared EFI partition or an original recovery/OEM/MSR partition.
4. Remove second-OS data partitions only after that review. Remove obsolete boot entries/files only when their ownership and the original boot path are certain; do not format EFI to “clean it up”.
5. Reclaim space only if the layout permits it. [Windows extension requires adjacent unallocated space on the same disk](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/extend-a-basic-volume); if a recovery partition is in the way, leave the space unused or plan another use with ICT rather than moving/deleting recovery partitions.
6. Repeat the [school verification checklist](everyday-use.md), including encryption and recovery checks.

A second Windows installation can place shared boot files on an existing system partition. Deleting its volume or an entry without understanding that dependency can break the remaining installation. Do not use a generic “delete the other partition” recipe.
