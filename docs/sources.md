# Sources and verification limits

[Guide home](../README.md)

Source review date: **16 September 2026**. Prefer the current original documents over screenshots or search snippets. School-specific publications are examples, not nationwide instructions or approval for dual boot.

| Source | What it supports |
| --- | --- |
| [Peirce Secondary: Windows 11 DMA Parent Option A guide](https://www.peircesec.moe.edu.sg/files/Windows_DMA_Windows_11__Parent_Option_A_V1_2.pdf) | An official school-hosted example of Windows DMA parent guidance; confirm your own school's current arrangements. |
| [Shuqun Primary: MIMS student end-user guide](https://www.shuqunpri.moe.edu.sg/files/2024_MIMS_Students_EndUser_Guide.pdf) | MIMS identity terminology; not evidence of Windows Pro entitlement or automatic DMA installation. |
| [Microsoft: Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) | Official media and architecture choices. |
| [Microsoft: create installation media](https://support.microsoft.com/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d) | Media creation, USB requirements, and firmware edition selection. |
| [Microsoft: activate Windows](https://support.microsoft.com/en-gb/windows/activate-windows-c39005d4-95ee-b91e-b399-2820fda32227) | Activation requirements; obtain applicable licence terms separately. |
| [Microsoft: MDM enrolment of Windows devices](https://learn.microsoft.com/en-us/windows/client-management/mdm-enrollment-of-windows-devices) | Organisational join and conditional automatic MDM enrolment; not an MOE-specific procedure. |
| [Microsoft: shrink a basic volume](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/shrink-a-basic-volume) | Disk Management shrinking and unmovable-file limitations. |
| [Microsoft: find your BitLocker recovery key](https://support.microsoft.com/en-us/windows/finding-your-bitlocker-recovery-key-in-windows-6b71ad27-0b89-ea08-f143-056f5ab347d6) | Recovery-key identification and retrieval routes. |
| [Microsoft: recovery options](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows) | Windows repair, reset, and reinstall options. |
| [Ubuntu: install Ubuntu Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop) | Live testing, installer storage choices, and BitLocker incompatibility warnings. |
| [Ubuntu Desktop documentation](https://ubuntu.com/desktop/docs/en/latest/) | Current USB, installation, BitLocker, and RST guidance. |
| [Rufus official site](https://rufus.ie/en/) | Authentic downloads and executable usage. |

## Additional technical references

- [Windows Setup EI.cfg and PID.txt](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-edition-configuration-and-product-id-files--eicfg-and-pidtxt?view=windows-11): optional edition/key configuration, not activation.
- [Windows Autopilot requirements](https://learn.microsoft.com/en-us/autopilot/requirements): supported editions, including Pro and Pro Education; not proof of school deployment settings.
- [Company Portal app status](https://learn.microsoft.com/en-us/intune/user-help/apps/install-apps-windows): required/optional apps and installation progress.
- [BitLocker FAQ](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq): boot changes and recovery triggers.
- [Ubuntu Secure Boot](https://wiki.ubuntu.com/UEFI/SecureBoot): signed boot chain and driver key enrolment.

The maintainer supplied the [MIMS provisioning experience](school-enrolment.md), including the approximate 30-minute-to-2-hour wait. This timing is not independently measured or an official MOE guarantee.

## Evidence boundaries

This revision is a documentation review, not a successful installation report. The inherited screenshots show individual UI screens; they do not prove preservation of DMA, school access, recovery, or any complete dual-boot workflow. The storage budgets and stop conditions are this project's conservative planning guidance, not MOE requirements.

A universal MIMS-to-DMA enrolment procedure, school approval for dual boot, model-specific Linux support, and additional Windows licence entitlement remain unverified. Do not present assumptions about them as facts. Contributions should state the exact device model, OS/installer version, date, and scope actually tested, with personal information removed.
