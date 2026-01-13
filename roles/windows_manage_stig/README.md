windows_manage_stig
===================

A role to enforce DISA STIG (Security Technical Implementation Guide) Windows Server 2022 V1R3 compliance controls with automated hardening, security validation, and comprehensive audit reporting.

Requirements
------------

* Windows Server 2019 or 2022
* PowerShell 5.1 or higher
* Administrative privileges on target systems
* Collection dependencies (see `galaxy.yml` and `meta/runtime.yml` for version requirements)

Role Variables
--------------

### Execution Controls

* **windows_manage_stig_generate_report**: Enable/disable compliance report generation. Default: **true**
* **windows_manage_stig_report_format**: Report output format. Valid values: **json**, **html**, **yaml**. Default: **json**
* **windows_manage_stig_report_path**: Directory path for report output. Default: **C:\temp\stig_compliance_report.json**
* **windows_manage_stig_fail_on_non_compliance**: Fail playbook if compliance threshold not met. Default: **false**
* **windows_manage_stig_compliance_threshold**: Minimum compliance percentage required. Default: **95**

### Benchmark Configuration

* **windows_manage_stig_benchmark_version**: DISA STIG version. Default: **V1R3**
* **windows_manage_stig_profile**: STIG compliance profile. Default: **STIG**
* **windows_manage_stig_skip_rules**: List of STIG rule IDs to skip (e.g., ["V-254238", "V-254292"]). Default: **[]**
* **windows_manage_stig_only_rules**: List of specific STIG rule IDs to run (empty = run all). Default: **[]**

### Policy Controls (STIG Defaults)

* **windows_manage_stig_password_history_size**: Enforce password history. Default: **24**
* **windows_manage_stig_maximum_password_age**: Maximum password age in days. Default: **60**
* **windows_manage_stig_minimum_password_age**: Minimum password age in days. Default: **1**
* **windows_manage_stig_minimum_password_length**: Minimum password length. Default: **14**
* **windows_manage_stig_password_complexity**: Require complex passwords. Default: **true**
* **windows_manage_stig_account_lockout_threshold**: Failed login attempts before lockout. Default: **3**
* **windows_manage_stig_account_lockout_duration**: Account lockout duration in minutes. Default: **15**

### Category Controls

* **windows_manage_stig_categories**: List of STIG control categories to execute. Default includes:
  - account_policies (Password and lockout policies)
  - audit_policies (Audit configuration)
  - user_rights_assignment (User rights and privileges)
  - security_options (Security policy settings)
  - registry_settings (Registry-based controls)
  - system_services (Windows service hardening)

### STIG Control Metadata

* **windows_manage_stig_classification**: Security classification level. Default: **Unclassified**
* **windows_manage_stig_organization**: Organization name for audit trails. Default: **Organization Name**

Tags
----

This role supports granular execution control through Ansible tags:

### Category Tags

* **account_policies**: Password and account lockout policies
* **audit_policies**: Audit policy configuration
* **user_rights_assignment**: User rights and privilege assignment
* **security_options**: Security policy settings
* **registry_settings**: Registry-based security controls
* **system_services**: Windows service configuration

### Execution Control Tags

* **setup**: Variable and configuration initialization
* **audit**: Audit-only tasks (no changes)
* **hardened**: Apply hardening changes
* **compliance**: Compliance validation tasks

### STIG Rule ID Tags

Individual STIG controls can be targeted using tags like **stig_V-254238**, **stig_V-254292**, etc.

### Severity Tags

* **cat_i**: CAT I (High severity) controls
* **cat_ii**: CAT II (Medium severity) controls
* **cat_iii**: CAT III (Low severity) controls

### Example Tag Usage

Run only account policies:
```bash
ansible-playbook playbook.yml --tags account_policies
```

Run only CAT I (high severity) controls:
```bash
ansible-playbook playbook.yml --tags cat_i
```

Skip registry settings:
```bash
ansible-playbook playbook.yml --skip-tags registry_settings
```

Run specific STIG control:
```bash
ansible-playbook playbook.yml --tags stig_V-254238
```

Dependencies
------------

- NA

Example Playbook
----------------

### Basic STIG Hardening

```yaml
- hosts: windows_servers
  tasks:
    - name: Apply DISA STIG hardening
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_stig
      vars:
        windows_manage_stig_generate_report: true
        windows_manage_stig_report_format: "html"
        windows_manage_stig_organization: "My Organization"
```

### STIG Compliance Validation (Check Mode)

```yaml
- hosts: windows_servers
  tasks:
    - name: Validate STIG compliance
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_stig
      vars:
        windows_manage_stig_generate_report: true
        windows_manage_stig_report_format: "json"
        windows_manage_stig_fail_on_non_compliance: true
        windows_manage_stig_compliance_threshold: 95
      check_mode: true
```

### High Severity Controls Only

```yaml
- hosts: windows_servers
  tasks:
    - name: Apply CAT I controls
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_stig
      tags:
        - cat_i
```

### Selective Control Application

```yaml
- hosts: windows_servers
  tasks:
    - name: Apply specific STIG controls
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_stig
      vars:
        windows_manage_stig_only_rules:
          - "V-254238"
          - "V-254239"
          - "V-254240"
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
