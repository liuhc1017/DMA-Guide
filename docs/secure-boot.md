# Secure Boot changes and the original school Windows

[Guide home](../README.md) · [Preparation](preparation.md) · [Recovery](recovery.md)

> [!WARNING]
> Changing Secure Boot, its trust keys, or the boot path can trigger **BitLocker recovery on the original DMA-managed Windows partition**, even if you never changed its files. Have its matching recovery key available before making boot changes. A key for your personal Windows partition will not unlock a different encrypted volume.

Secure Boot verifies trusted boot software. BitLocker protects encrypted Windows data and may use TPM measurements of the boot environment to unlock it. A changed measurement can require the recovery key. Firmware settings are shared by the laptop: they are not private settings of the new partition. See [Microsoft's BitLocker FAQ](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq).

## Does Secure Boot need changing?

**Sometimes, depending on the firmware, installation media, distribution, and drivers.** Start with it enabled. Supported Windows media and Ubuntu's signed boot chain are designed to work with Secure Boot. Ubuntu third-party drivers may require Machine Owner Key (MOK) enrolment; that is different from turning Secure Boot off. See [Ubuntu's Secure Boot documentation](https://wiki.ubuntu.com/UEFI/SecureBoot).

A firmware trust setting, signed driver/key enrolment, or firmware update may need attention. Some unsupported/unsigned configurations require disabling Secure Boot, which may conflict with school requirements. This guide does not assume that is necessary or acceptable for your PLD. If the configuration cannot keep the school environment compliant, use a compatible alternative.

## Before any authorised change

1. Record the original settings and exact boot error privately. Use current OEM and distribution instructions for the device; do not copy another laptop's firmware menu steps.
2. Confirm access to the **school partition's** recovery key with ICT, and verify the backup. Have keys for any other encrypted installations ready too.
3. Ask ICT which specific change is acceptable and whether to suspend BitLocker protection temporarily. Suspension does not decrypt data; decryption is a different operation.
4. Make only the agreed change. Do not clear the TPM, delete/reset Secure Boot keys, switch to Legacy/CSM, or change storage-controller mode as a troubleshooting experiment.
5. Boot the original school Windows immediately afterwards. If it requests a key, follow [BitLocker recovery](recovery.md#2-handle-a-bitlocker-prompt). Stop if the matching key is unavailable.
6. Have ICT confirm the required Secure Boot configuration and active BitLocker protection after completion. Recheck DMA and school access before using the second OS again.

Restoring a previous firmware setting is not guaranteed to remove a recovery prompt. Repeatedly toggling Secure Boot when switching systems is not a sustainable setup: both environments need a compatible, agreed boot configuration. Never erase the managed partition because a boot-security change made it ask for a key.
