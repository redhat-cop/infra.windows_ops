# windows_manage_audit

Manage Windows audit policies and audit rules.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| **windows_manage_audit_system_policies** | System-wide audit policy settings | list(dict) | `[]` |
| **windows_manage_audit_ignore_missing** | Ignore errors for missing rules on remove | bool | `false` |
| **windows_manage_audit_rules_remove** | Audit rules to remove | list(dict) | `[]` |
| **windows_manage_audit_rules_create** | Audit rules to create | list(dict) | `[]` |

### System Policy Items

Each item in `windows_manage_audit_system_policies` should include:
- `audit_type`: List of audit types (`success`, `failure`)
- `category` or `subcategory`: The audit category or subcategory name

### Audit Rule Items

Each item in `windows_manage_audit_rules_create` and `windows_manage_audit_rules_remove` should include:
- `path`: Filesystem path or registry key (e.g., `C:\Windows\Temp`, `HKLM:\SOFTWARE`)
- `user`: User or group (e.g., `BUILTIN\Users`)
- `rights` (create only): List of access rights (e.g., `delete`, `readdata`)
- `audit_flags` (create only): List of audit flags (`success`, `failure`)

Rules scheduled for removal are skipped when a matching create rule exists for the same path and user.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_audit
      vars:
        windows_manage_audit_system_policies:
          - category: Account Logon
            audit_type:
              - success
              - failure
          - subcategory: File System
            audit_type:
              - failure
        windows_manage_audit_rules_create:
          - path: HKLM:\SOFTWARE
            user: BUILTIN\Users
            rights:
              - delete
            audit_flags:
              - success
```

## License

GPL-3.0-or-later

## Author

Ansible Ecosystem Engineering team (@eco-ansible-content)
