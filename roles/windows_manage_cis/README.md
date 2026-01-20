windows_manage_cis
==================

A role to enforce CIS Microsoft Windows Server 2022 Benchmark v1.0.0 compliance controls with automated hardening, drift detection, and comprehensive audit reporting.

Requirements
------------

* Windows Server 2019 or 2022
* PowerShell 5.1 or higher
* Administrative privileges on target systems
* Collection dependencies (see `galaxy.yml` and `meta/runtime.yml` for version requirements)

Role Variables
--------------

### Execution Controls

* **windows_manage_cis_generate_report**: Enable/disable compliance report generation. Default: **true**
* **windows_manage_cis_report_format**: Report output format. Valid values: **json**, **html**, **yaml**. Default: **json**
* **windows_manage_cis_report_path**: Directory path for report output. Default: **/tmp/cis_compliance_report**
* **windows_manage_cis_fail_on_non_compliance**: Fail playbook if compliance threshold not met. Default: **false**

### Benchmark Configuration

* **windows_manage_cis_benchmark_version**: CIS Benchmark version. Default: **v1.0.0**
* **windows_manage_cis_profile**: CIS compliance profile. Valid values: **Level 1**, **Level 2**. Default: **Level 1**
* **windows_manage_cis_skip_rules**: List of CIS rule IDs to skip. Default: **[]**
* **windows_manage_cis_only_rules**: List of specific CIS rule IDs to run (empty = run all). Default: **[]**

### Policy Controls (Level 1 Defaults)

* **windows_manage_cis_password_history_size**: Enforce password history. Default: **24**
* **windows_manage_cis_maximum_password_age**: Maximum password age in days. Default: **365**
* **windows_manage_cis_minimum_password_age**: Minimum password age in days. Default: **1**
* **windows_manage_cis_minimum_password_length**: Minimum password length. Default: **14**
* **windows_manage_cis_password_complexity**: Require complex passwords. Default: **true**
* **windows_manage_cis_account_lockout_threshold**: Failed login attempts before lockout. Default: **5**
* **windows_manage_cis_account_lockout_duration**: Account lockout duration in minutes. Default: **15**
* **windows_manage_cis_windows_firewall_domain_firewall_state**: Domain profile firewall state. Default: **On**

### Category Controls

* **windows_manage_cis_categories**: List of CIS control categories to execute. Default includes:
  - password_policies (CIS 1.1.x)
  - account_lockout (CIS 1.2.x)
  - user_rights_assignment (CIS 2.2.x)
  - security_options (CIS 2.3.x)
  - system_services (CIS 5.x)
  - audit_policies (CIS 17.x)
  - advanced_audit_policies (CIS 18.x)
  - administrative_templates (CIS 18.x)
  - windows_firewall (CIS 9.x)
  - registry_settings (CIS Various)

Tags
----

This role supports granular execution control through Ansible tags:

### Category Tags

* **password_policies**: Password policy controls (CIS 1.1.x)
* **account_lockout**: Account lockout policy (CIS 1.2.x)
* **user_rights_assignment**: User rights assignment (CIS 2.2.x)
* **security_options**: Security option settings (CIS 2.3.x)
* **system_services**: Windows service configuration (CIS 5.x)
* **audit_policies**: Audit policy configuration (CIS 17.x)
* **advanced_audit_policies**: Advanced audit policies (CIS 18.x)
* **administrative_templates**: Administrative template settings (CIS 18.x)
* **windows_firewall**: Windows Firewall configuration (CIS 9.x)
* **registry_settings**: Registry-based controls

### Execution Control Tags

* **setup**: Variable and configuration initialization
* **audit**: Audit-only tasks (no changes)
* **hardened**: Apply hardening changes
* **scored**: Scored CIS controls only
* **compliance**: Compliance validation tasks

### CIS Rule ID Tags

Individual controls can be targeted using tags like **cis_1.1.1**, **cis_2.2.5**, etc.

### Example Tag Usage

Run only password policies:
```bash
ansible-playbook playbook.yml --tags password_policies
```

Skip Windows Firewall configuration:
```bash
ansible-playbook playbook.yml --skip-tags windows_firewall
```

Run specific CIS control:
```bash
ansible-playbook playbook.yml --tags cis_1.1.1
```

Dependencies
------------

- NA

Example Playbook
----------------

### Basic CIS Level 1 Hardening

```yaml
- hosts: windows_servers
  tasks:
    - name: Apply CIS Level 1 hardening
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_cis
      vars:
        windows_manage_cis_profile: "Level 1"
        windows_manage_cis_generate_report: true
        windows_manage_cis_report_format: "html"
```

### Drift Detection (Check Mode)

```yaml
- hosts: windows_servers
  tasks:
    - name: Detect CIS compliance drift
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_cis
      vars:
        windows_manage_cis_generate_report: true
        windows_manage_cis_report_format: "json"
      check_mode: true
```

### Selective Control Application

```yaml
- hosts: windows_servers
  tasks:
    - name: Apply only password policies
      ansible.builtin.include_role:
        name: infra.windows_ops.windows_manage_cis
      vars:
        windows_manage_cis_only_rules:
          - "1.1.1"
          - "1.1.2"
          - "1.1.3"
          - "1.1.4"
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
