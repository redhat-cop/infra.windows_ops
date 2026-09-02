# windows_manage_features

Install and remove Windows Server roles and features.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_features_remove` | list(str) | `[]` | Windows feature names to remove (skipped if also in the install list) |
| `windows_manage_features_remove_ignore_unknown` | bool | `true` | Ignore errors when removing features that are not valid on the host |
| `windows_manage_features_install` | list(raw) | `[]` | Features to install; each item is a name string or a dict with `name` and optional `source`, `include_sub_features`, `include_management_tools` |
| `windows_manage_features_reboot` | bool | `true` | Reboot automatically when a feature change requires it |

## Example Playbook

```yaml
- name: Manage Windows features
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_features
      vars:
        windows_manage_features_remove:
          - Telnet-Client
        windows_manage_features_install:
          - WoW64-Support
          - name: Web-Server
            source: D:\Sources
            include_sub_features: true
            include_management_tools: true
        windows_manage_features_reboot: true
```

## License

GPL-3.0-or-later
