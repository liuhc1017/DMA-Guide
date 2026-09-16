# Windows 11 Pro, MIMS, and DMA enrolment

[Guide home](../README.md) · Related: [Windows installation](windows.md)

**Get the Windows edition your school specifies, then sign in with your MIMS-linked school account through the school's prescribed enrolment flow.** Windows 11 Pro may be appropriate because it supports organisational join features unavailable in Home. However, “install Pro and sign in with MIMS” is not a verified universal DMA installation recipe.

MIMS (MOE Identity Management System) provides identity/account access. Windows activation, Microsoft Entra device join, device management enrolment, and deployment of DMA software/policies are separate steps. Signing in to a website or Office application alone does not demonstrate that those steps happened.

Microsoft documents that organisational join can trigger automatic MDM enrolment **when the organisation has configured it**. This explains a possible mechanism, not proof of any particular MOE school's setup. See [Microsoft's Windows MDM enrolment documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm-enrollment-of-windows-devices).

## School-directed setup

1. Ask ICT whether the second installation should be enrolled at all, whether a second enrolment on the same physical device is supported, and which Windows edition/licence and school image they require. Keep the original installation's account and enrolment intact.
2. Obtain the current school setup instructions and any official installation package or enrolment link directly from ICT. This repository does not distribute DMA packages, tenant identifiers, certificates, or enrolment tokens.
3. Install and activate the approved Windows edition as directed. If the school uses Windows Pro organisational setup, select **Set up for work or school** when offered, and sign in with the exact school account/username format and MIMS credentials supplied by the school. Complete required authentication.
4. If Windows is already set up, ICT may instead direct you through **Settings → Accounts → Access work or school → Connect**, including a specific organisation-join option. Merely connecting an account can have a different result from joining a device; follow the school's exact steps rather than guessing.
5. Allow the school's provisioning and required restarts to finish. Install a DMA component manually only if the school's instructions supply and require it. Do not use third-party “DMA installers”.
6. Have ICT confirm enrolment, required DMA components/policies, encryption, and device compliance. Verify school Wi-Fi, assigned learning applications, MIMS/iCON access, SLS as applicable, and any assessment requirements. Successful account sign-in alone is insufficient.
7. Reboot the original Windows and check that its DMA and school access still work. Resolve duplicate-device or compliance issues with ICT; do not disconnect school accounts or delete device registrations to fix them yourself.

School account or enrolment policies may also manage a newly enrolled installation. Do not assume enrolling the second OS preserves an unrestricted personal environment. Keep the purpose and configuration agreed with the school clear before setup.

## What remains unverified

As of the source review on 16 September 2026, this project has not established a public, nationwide procedure guaranteeing automatic DMA deployment from a Pro installation and MIMS sign-in. Schools may require their own image, provisioning, or ICT intervention. Submit current public official instructions through a [documentation issue](https://github.com/liuhc1017/DMA-Guide/issues/new/choose); never share credentials or private enrolment links.
