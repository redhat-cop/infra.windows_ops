# windows_manage_rdp

Enable or disable Remote Desktop Protocol (RDP) with firewall and authentication settings.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_rdp_enable` | bool | `true` | Enable or disable RDP connections |
| `windows_manage_rdp_firewall_profiles` | list(str) | `[domain, private]` | Firewall profiles for RDP rules |
| `windows_manage_rdp_authenticate` | bool | `true` | Require Network Level Authentication (NLA) |

## Example Playbook

```yaml
- name: Configure RDP
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_rdp
      vars:
        windows_manage_rdp_enable: true
        windows_manage_rdp_authenticate: true
        windows_manage_rdp_firewall_profiles:
          - domain
          - private
          - public
```

## License

GPL-3.0-or-later
