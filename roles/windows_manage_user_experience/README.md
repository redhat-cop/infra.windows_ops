# windows_manage_user_experience

Configure Windows user experience settings such as Server Manager auto-launch, network location wizard, and Welcome Screen behavior.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_user_experience_server_manager_at_logon` | bool | `true` | Open Server Manager automatically at logon |
| `windows_manage_user_experience_network_location_wizard` | bool | `false` | Enable or disable the new network location wizard |
| `windows_manage_user_experience_show_last_user_name` | bool | `true` | Show or hide the last user name on the Welcome Screen |

## Example Playbook

```yaml
- name: Configure user experience
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_user_experience
      vars:
        windows_manage_user_experience_server_manager_at_logon: false
        windows_manage_user_experience_network_location_wizard: false
        windows_manage_user_experience_show_last_user_name: false
```

## License

GPL-3.0-or-later
