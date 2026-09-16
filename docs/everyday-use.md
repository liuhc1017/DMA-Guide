# Verify both systems and use them responsibly

[Guide home](../README.md) · Help: [Troubleshooting](troubleshooting.md)

## Acceptance checklist

Do this before considering installation complete, and repeat school-access checks after major OS or boot updates:

- [ ] The original school Windows starts from the boot menu, including after a full shutdown.
- [ ] Existing school files open and the off-device backup is still accessible.
- [ ] MIMS/iCON sign-in, school Wi-Fi, required apps, and applicable SLS/assessment access work in the original installation.
- [ ] DMA is functioning as expected; ICT has checked compliance where needed.
- [ ] BitLocker protection is active according to school policy, recovery-key access is confirmed, and WinRE/recovery options remain available. If ICT suspended protection, have it confirm protection has resumed.
- [ ] The original EFI, MSR, recovery, and OEM partitions remain present. Ask ICT about recovery health if the layout or WinRE status changed.
- [ ] The second OS starts and its keyboard, network, audio, updates, and sleep/wake work.
- [ ] Each OS has its own file backup and, where applicable, its own securely stored encryption recovery information.
- [ ] You can identify each boot choice reliably and have recorded how to return to school Windows.

Partition presence alone does not prove recovery will succeed. Do not test a destructive factory reset merely to complete this list.

## Make school Windows easy to reach

Keep school Windows the default boot choice. For two Windows installations, use System Configuration (`msconfig`) → **Boot** only after identifying the entries by booting them. Set the original as default and allow a visible selection timeout; do not delete entries. For Linux, use the manufacturer's permitted firmware boot-order controls to prefer Windows Boot Manager if appropriate. If menus are locked or ambiguous, ask ICT.

## Personal time and maintenance

Use the second OS for agreed personal activities such as programming, app installation, and projects outside school use. Agree times with your parent/guardian and follow school rules; a second OS is not permission to ignore them. Return to school Windows before lessons or assessments and allow time for its updates and DMA check-in.

Install applications from trusted publishers and keep both systems updated. Do not treat another OS as a place to store the only copy of important work. Avoid accessing school partitions from the personal OS, and do not change the original installation's management services, accounts, certificates, or security settings.

Before a school service appointment, back up **both** environments. Explain the dual-boot layout to ICT. A whole-disk school reimage may remove the second OS and all its data, even if an ordinary Windows repair would not.
