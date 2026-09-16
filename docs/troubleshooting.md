# Troubleshooting

[Guide home](../README.md) · If school Windows will not start: [Recovery](recovery.md)

Stop repeated installation attempts when the disk layout or encryption state is uncertain. Record the exact error privately before making changes.

| Symptom | Safe next step |
| --- | --- |
| Administrator approval, USB boot, or firmware settings are blocked | Ask school ICT for an approved route. Do not reset passwords or firmware locks. |
| Shrink offers little or no space | Unmovable files can limit shrinking. Keep school data backed up and discuss capacity with ICT; do not force a resize with another OS. |
| BitLocker asks for a recovery key | Match the on-screen key ID with the correct recovery key or contact ICT. Do not clear TPM, format, or reset. See recovery below. |
| USB is missing from the boot menu | Verify it was written successfully for the correct architecture/UEFI mode; use the manufacturer's one-time menu. Try a working port/media. If policy blocks boot, contact ICT. |
| Secure Boot rejects the installer | Check official media and device guidance with ICT. A change may be needed; first prepare for [BitLocker recovery on school Windows](secure-boot.md). |
| Installer cannot see the SSD / requests RST changes | Obtain exact-model storage drivers or ICT assistance. Do not switch RST/VMD/RAID to AHCI casually. |
| Windows says it cannot install on the selected disk | Recheck UEFI boot, GPT, and the prepared space. Cancel if anything differs. Do not use `diskpart clean`, convert the disk, or delete partitions. |
| Windows installer has no network | Use approved exact-model OEM network drivers or a supported wired adapter. Do not use account-requirement workarounds. |
| Installer keeps restarting from the USB | Choose the internal boot entry for the installation already in progress; remove the USB when Setup no longer needs it. Do not start a second install. |
| Ubuntu requests BitLocker decryption | Stop; ICT must assess encryption policy. Suspension is not decryption. |
| Linux cannot see Windows in its boot menu | Try firmware → Windows Boot Manager. A missing menu entry does not prove Windows was deleted. |
| Two identical Windows menu entries | Boot and identify each by accounts/files; record the mapping. Never delete the one you merely suspect is old. |
| Pro is missing or Windows will not activate | Check the installed edition and genuine licence with Microsoft/ICT. A firmware key may select another edition; MIMS is not a guaranteed Pro entitlement. |
| School apps have not arrived after first login | Keep the managed OS online and on AC; inspect Company Portal statuses. The maintainer reports roughly 30 minutes–2 hours, with wide variation. Persistent errors or stalled progress need ICT, not a reinstall. See [provisioning](school-enrolment.md#first-boot-allow-time-for-apps-to-arrive). |
| MIMS sign-in works but DMA is missing | Ask ICT to verify the intended enrolment and deployment. See [school enrolment](school-enrolment.md). |
| School Wi-Fi/apps fail in the second OS | Use original school Windows. Certificates, management, drivers, or compliance may be required; do not copy school certificates/private keys. |
| Update changes boot order | Use the permitted one-time boot menu to choose school Windows, then have the default corrected. Keep recovery keys available. |
| Linux reports Windows is hibernated or read-only | Leave the school volume unmounted. Return to Windows and fully shut down. Do not force-mount or delete hibernation files. |
| Personal OS asks to initialise or format an unfamiliar volume | Cancel. It may be an encrypted school or recovery partition. |

For urgent school access, contact ICT first. For a guide correction, use an [issue template](https://github.com/liuhc1017/DMA-Guide/issues/new/choose). Share only model (not serial number), OS/installer version, guide step, sanitised error text, and what still boots. Review every screenshot for personal data first.
