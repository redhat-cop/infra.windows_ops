# windows_manage_user_settings

Apply per-user registry settings across existing and logged-in Windows user profiles.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_user_settings_apply_to_logged_in_users` | bool | `true` | Apply settings to currently logged-in users via `become` |
| `windows_manage_user_settings_registry` | list(dict) | `[]` | Registry settings to apply per user profile |

Each `windows_manage_user_settings_registry` item supports:

| Key | Required | Description |
|---|---|---|
| `setting` | yes | Human-readable label for the setting |
| `path` | yes | Registry path (typically under `HKCU:`) |
| `name` | no | Value name |
| `type` | no | Value type (e.g. `DWord`, `String`) |
| `data` | no | Value data |
| `state` | no | `present` (default) or `absent` |

## Example Playbook

```yaml
- name: Apply user settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_user_settings
      vars:
        windows_manage_user_settings_apply_to_logged_in_users: true
        windows_manage_user_settings_registry:
          - setting: Minimize Visual Effects for Performance
            path: HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects
            name: VisualFXSetting
            type: DWord
            data: 2
          - setting: Disable Taskbar Animations
            path: HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
            name: TaskbarAnimations
            type: DWord
            data: 0
```

## How it works

Each `HKCU:` setting is applied to every existing user profile by loading that
profile's `NTUSER.DAT` hive. For users who are currently logged in the hive is
locked; when `windows_manage_user_settings_apply_to_logged_in_users` is `true`
those settings are re-applied via `become` in the user's own context. The
connecting Ansible user's own profile is intentionally excluded.

## License

GPL-3.0-or-later
