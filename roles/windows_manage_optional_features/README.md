# windows_manage_optional_features

Install and remove Windows optional features via DISM, with optional automatic reboot.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_optional_features_remove` | list(str) | `[]` | Optional feature names to remove. Features also in the install list are skipped. |
| `windows_manage_optional_features_remove_ignore_unknown` | bool | `true` | Ignore failures when removing features that are not present. |
| `windows_manage_optional_features_install` | list(raw) | `[]` | Features to install. Each item is a name (string) or a mapping with `name` (required), `source`, `include_parent`. |
| `windows_manage_optional_features_reboot` | bool | `true` | Reboot automatically when a change requires it. |

## Example Playbook

```yaml
- name: Manage Windows optional features
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_optional_features
      vars:
        windows_manage_optional_features_remove:
          - WindowsMediaPlayer
        windows_manage_optional_features_install:
          - TelnetClient
          - name: IIS-WebServer
            source: D:\Sources
            include_parent: true
        windows_manage_optional_features_reboot: true
```

## License

GPL-3.0-or-later
