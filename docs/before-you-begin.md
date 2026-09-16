# Before you begin

[Guide home](../README.md) · Next: [Preparation](preparation.md)

## Decide with your school and parent/guardian

Explain the specific need: for example, a compiler, editor, local development server, or personal application that is unavailable in the managed environment. Ask whether an approved app installation, browser-based development environment, school-approved WSL/VM, or current after-school DMA option meets that need with less disk risk. These alternatives still depend on school policy and device capability.

School parent-option guides describe after-school arrangements, but they do not establish permission to dual boot. Do not assume one school's hours, vendor, or settings apply nationally. See the [official school examples](sources.md).

If this is your only computer, plan for downtime and arrange another way to access schoolwork. Do not repartition on the night before an assessment. A school-owned or loaned device may have different conditions from a family-purchased PLD.

## Go / no-go checklist

Proceed only when every applicable item is complete:

- [ ] The school permits the proposed second OS and disk/boot changes; a parent/guardian understands the plan.
- [ ] You have authorised administrator access for the required steps and permitted access to the one-time boot menu. If either is blocked, ask ICT.
- [ ] School Windows starts normally, DMA is functioning, and school applications and sign-in work.
- [ ] Important local files are backed up **off this physical disk**, and several backed-up files have been opened successfully.
- [ ] Cloud files have finished syncing. Confirm that online-only files are actually available in the backup or cloud account; a sync icon alone is not a restore test.
- [ ] The correct BitLocker recovery key is available, or ICT has confirmed it can supply it when needed. Do not assume MIMS sign-in will reveal it.
- [ ] ICT has explained how to restore the original school image, drivers, DMA, and school access if recovery fails.
- [ ] You have AC power, time for multiple restarts, installation media, and offline network/storage drivers for your exact model where needed.
- [ ] There is sufficient space for both systems, their updates, and your files.

**Stop if any of these conditions cannot be met.** The guide cannot provide missing permissions, encryption keys, or a school recovery image.

## Record the starting state privately

In Windows, open `msinfo32` and record the model, System Type, BIOS Mode, and Secure Boot State. This guide expects x64, UEFI, and Secure Boot enabled. In Disk Management, check the disk's Properties → Volumes → Partition style (GPT). Record the disk capacity, partition order, sizes, labels, and which volume contains the running school Windows. Do not identify a partition from its drive letter alone: letters and disk numbering may change in an installer.

Record the Windows edition and activation status in Settings → System → Activation. Check encryption status using the available BitLocker/Device encryption settings or ask ICT. If permitted, `manage-bde -status` and `reagentc /info` in an administrator terminal report encryption and Windows Recovery Environment (WinRE) status; they do not create backups. If WinRE is disabled or unavailable, ask ICT before continuing.

Keep a full partition-map screenshot privately, including partitions off the right edge of the window. Store recovery information separately from the laptop. Never post passwords, 48-digit recovery keys, product keys, student email addresses, device IDs, or school enrolment tokens in an issue.

## Backups and recovery are different

A file backup protects documents, not necessarily installed applications, DMA configuration, or the boot environment. An approved full-disk image can preserve more, but its restore procedure and encryption-key handling must be understood with ICT. Neither a recovery partition nor a second partition protects against physical disk failure.

A Microsoft installer can repair or install Windows; it is **not** the school's managed image. A Windows recovery drive does not back up personal files. Obtain the school's recovery procedure before making changes, and keep backup media disconnected during installation.
