# windows_manage_registry

Apply system-wide Windows registry settings with `ansible.windows.win_regedit`, with optional per-setting reboot handling.

For user-specific registry settings, see the `windows_manage_user_settings` role.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_registry_settings` | list(dict) | `[]` | List of registry settings to apply (see item keys below) |
| `windows_manage_registry_reboot` | bool | `true` | Allow reboot after changes; only reboots when a changed item has `reboot: true` |

Each item in `windows_manage_registry_settings` supports:

| Key | Required | Description |
|---|---|---|
| `setting` | yes | Human-readable label for the setting |
| `path` | yes | Full registry path, e.g. `HKLM:\SOFTWARE\...` |
| `name` | no | Value name (omit to act on the key itself) |
| `type` | no | `none`, `binary`, `dword`, `expandstring`, `multistring`, `string`, `qword` |
| `data` | no | Value data |
| `state` | no | `present` (default) or `absent` |
| `reboot` | no | Whether this setting requires a reboot (default `false`) |

## Example Playbook

```yaml
- name: Apply registry settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_registry
      vars:
        windows_manage_registry_reboot: true
        windows_manage_registry_settings:
          - setting: Allow full admin privileges for local admins over WinRM
            path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
            name: LocalAccountTokenFilterPolicy
            type: DWord
            data: 1
          - setting: Enable User Account Control (UAC)
            path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
            name: EnableLUA
            type: DWord
            data: 1
            reboot: true
          - setting: Enable new network location wizard
            path: HKLM:\SYSTEM\CurrentControlSet\Control\Network\NewNetworkWindowOff
            state: absent
```

## License

GPL-3.0-or-later
