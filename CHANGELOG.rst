================================
Infra.Windows\_ops Release Notes
================================

.. contents:: Topics

v2.0.0
======

Major Changes
-------------

- windows_manage_cis - Added Windows Server 2025 support with CIS Benchmark v1.0.0 (210 controls). Implements version-specific controls including Azure Arc integration (18.10.89.1), Zero Trust network access (19.7.1), and AD 32k page support (18.10.90.1). Maintains backward compatibility with Windows Server 2019 and 2022 through automatic version detection.
- windows_manage_stig - Added Windows Server 2025 support with DISA STIG V1R1 (295 controls). Implements automatic OS version detection with dual method (ProductName + build number fallback). Includes 2025-specific features (Hotpatching with Azure Arc, Next-Gen Credential Guard, AD 32k pages) and 2022+ features (DNS-over-HTTPS, SMB over QUIC, TLS 1.3). Supports unified role architecture across Windows Server 2019 (V3R7), 2022 (V2R7), and 2025 (V1R1) with version-conditional logic.
- windows_manage_stig - Updated to DISA STIG Version 2 Release 7 (V2R7) released January 23, 2026. This major update adds 79 new security controls and removes 1 deprecated rule (V-254411) (total 283 rules, up from 205), and significantly expands audit policies coverage with 34 new audit configuration rules. The update maintains backward compatibility with existing variables while introducing enhanced compliance coverage across all STIG categories.

Minor Changes
-------------

- windows_manage_cis - Added version-specific feature detection for DNS-over-HTTPS and TLS 1.3 on Windows Server 2022+.
- windows_manage_stig - Added integration tests for ``windows_manage_stig_only_rules`` filtering functionality.
- windows_manage_stig - Created integration tests for version detection validation and Windows Server 2025 feature verification.
- windows_manage_stig - Enhanced compliance reporting with version detection metadata including detected_version, benchmark_version, and version_features in JSON reports.
- windows_manage_stig - Updated security_options.yml with version-aware LAPS implementation (MSI for 2019, native for 2022/2025) and SMB signing behavior (enforce for 2019/2022, verify-only for 2025 with default enabled).

Bugfixes
--------

- windows_manage_stig - Fixed 6 STIG controls that were incorrectly classified as CAT II instead of CAT I per official DISA documentation.
- windows_manage_stig - Fixed ``windows_manage_stig_only_rules`` filtering to properly restrict rule execution to only specified STIG IDs.
- windows_manage_stig - Fixed audit policy remediation to preserve paired success/failure controls, preventing "whack-a-mole" effect where fixing one control inadvertently breaks its paired control.
- windows_manage_stig - Fixed critical V-ID to registry mapping errors affecting 33 controls in registry_settings.yml. Controls were mapping to completely wrong registry paths and value names, causing remediation to appear successful while DISA SCC scans continued to fail. All mappings verified against official DISA STIG V2R7 XCCDF (https://github.com/redhat-cop/infra.windows_ops/issues/41).

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
