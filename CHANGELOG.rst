================================
Infra.Windows\_ops Release Notes
================================

.. contents:: Topics

v1.2.0
======

Major Changes
-------------

- windows_manage_cis - Added new role for CIS Microsoft Windows Server 2022 Benchmark v1.0.0 compliance automation.
  Supports Level 1 and Level 2 profiles with 96+ security controls across password policies, account lockout,
  user rights assignment, security options, audit policies, Windows Firewall, and system services.
  Includes check mode for drift detection and comprehensive JSON/HTML reporting.
- windows_manage_stig - Added new role for DISA STIG Windows Server 2022 V1R3 compliance automation.
  Implements government security standards with 60+ STIG controls covering password policies, account lockout,
  audit policies, user rights, registry settings, and system services, and enterprise metadata tracking with JSON/HTML reporting.

v1.0.2
======

Release Summary
---------------

This is release 1.0.2 of ``infra.windows_ops``, released on 2025-05-09.

Bugfixes
--------

- Added documentation in patterns

v1.0.1
======

Release Summary
---------------

Minor update to fix minimal dependency versions.

v1.0.0
======

Release Summary
---------------

This is the first release of the ``infra.windows_ops`` collection.

Bugfixes
--------

- Minor doc updates and spelling mistakes
- Switch to microsoft.iis collection for managing IIS.

New Roles
---------

- infra.windows_ops.windows_manage_iis - A role to Create/Delete an IIS Web server.
- infra.windows_ops.windows_manage_service - A role to Manage Windows Services.
- infra.windows_ops.windows_manage_updates - A role to Manage Windows Updates.
