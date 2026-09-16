# Windows 11 Pro / Pro Education, MIMS, and DMA enrolment

[Guide home](../README.md) · Related: [Windows installation](windows.md)

**Get the Windows edition your school specifies, then sign in with your MIMS-linked school account through the school's prescribed enrolment flow.** For the maintainer-reported route, use **Windows 11 Pro or Windows 11 Pro Education** and sign in with your **MIMS-linked school account when prompted during school setup**. These editions support organisational deployment features; confirm the exact edition and entitlement with ICT. The media must actually include that edition.

MIMS (MOE Identity Management System) provides identity/account access. Windows activation, Microsoft Entra device join, device management enrolment, and deployment of DMA software/policies are separate steps. Signing in to a website or Office application alone does not demonstrate that those steps happened.

Microsoft documents that organisational join can trigger automatic MDM enrolment **when the organisation has configured it**. This explains a possible mechanism, not proof of any particular MOE school's setup. See [Microsoft's Windows MDM enrolment documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm-enrollment-of-windows-devices).

## School-directed setup

1. Ask ICT whether the second installation should be enrolled at all, whether a second enrolment on the same physical device is supported, and which Windows edition/licence and school image they require. Keep the original installation's account and enrolment intact.
2. Obtain the current school setup instructions and any official installation package or enrolment link directly from ICT. This repository does not distribute DMA packages, tenant identifiers, certificates, or enrolment tokens.
3. Install and activate the approved Windows edition as directed. If the school uses Windows Pro/Pro Education organisational setup, select **Set up for work or school** when offered, and sign in with the exact school account/username format and MIMS credentials supplied by the school. Complete required authentication.
4. If Windows is already set up, ICT may instead direct you through **Settings → Accounts → Access work or school → Connect**, including a specific organisation-join option. Merely connecting an account can have a different result from joining a device; follow the school's exact steps rather than guessing.
5. Allow the school's provisioning and required restarts to finish. After reaching the desktop for the first time, keep this installation running on AC power and a reliable internet connection while school apps arrive; see the timing and Company Portal checks below. Install a DMA component manually only if the school's instructions supply and require it. Do not use third-party “DMA installers”.
6. Have ICT confirm enrolment, required DMA components/policies, encryption, and device compliance. Verify school Wi-Fi, assigned learning applications, MIMS/iCON access, SLS as applicable, and any assessment requirements. Successful account sign-in alone is insufficient.
7. Reboot the original Windows and check that its DMA and school access still work. Resolve duplicate-device or compliance issues with ICT; do not disconnect school accounts or delete device registrations to fix them yourself.

School account or enrolment policies may also manage a newly enrolled installation. Do not assume enrolling the second OS preserves an unrestricted personal environment. Keep the purpose and configuration agreed with the school clear before setup.

## First boot: allow time for apps to arrive

The maintainer reports **around 30 minutes to 2 hours after first boot** for school apps such as **Chrome, Zoom, and Adobe applications** to arrive after MIMS setup. Actual time varies a lot; this is an experience report, **not an MOE service target or a guaranteed maximum**. The particular Adobe product and other assigned apps depend on the school. Hardware, downloads, updates, assignments, and enrolment state can all affect provisioning.

Keep the laptop connected to power and the internet and allow required restarts. Avoid booting into the personal OS while this installation is still provisioning. Reaching the desktop does not mean DMA or all required apps are ready.

## Check Company Portal

Where the school uses Microsoft Intune Company Portal:

1. Open **Company Portal** from Start and sign in with the school account if prompted. If it has not appeared, follow the school's provisioning instructions; do not assume installing the Portal alone enrols the device.
2. Open **Apps** to inspect app statuses; **Downloads & updates** lists installed apps and whether they are required. Names may vary by Portal version.
3. Distinguish **Available**, **Installing**, **Installed**, and **Install failed**. Required apps deploy automatically; optional apps may need an Install action. Status can lag behind installation.
4. If an app fails, record the sanitised error and use **Retry** if offered. For an enrolment check-in problem, use the school's instructions or [Microsoft's sync guidance](https://learn.microsoft.com/en-us/intune/user-help/device-actions/sync-device-windows); repeated syncs do not fix a missing assignment.
5. If provisioning appears stalled, school use is imminent, or an error persists, contact ICT with the elapsed time and app/error details. Two hours passing is a reason to check progress, not a reason to wipe or re-enrol the partition.

See [Microsoft's Company Portal app guidance](https://learn.microsoft.com/en-us/intune/user-help/apps/install-apps-windows). Apps appearing successfully is useful evidence, but ICT must still confirm DMA and school compliance. Complete the [verification checklist](everyday-use.md).

## Evidence and limits

The Pro/Pro Education → MIMS → app-provisioning sequence and 30-minute-to-2-hour estimate above are supplied by this project's maintainer. Device model, installer build, and school deployment details were not supplied, so the report is not an end-to-end compatibility certification. Microsoft lists these editions in its [Autopilot requirements](https://learn.microsoft.com/en-us/autopilot/requirements); that does not establish which provisioning system your school uses.

This project has not established a public, nationwide procedure guaranteeing automatic DMA deployment from edition choice and MIMS sign-in. Schools may require their own image, provisioning, or ICT intervention. Submit public official instructions or sanitised observations through a [documentation issue](https://github.com/liuhc1017/DMA-Guide/issues/new/choose); never share credentials or private enrolment links.
