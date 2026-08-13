# windows_manage_hosts_file

Manage the Windows hosts file with header, self-entry, custom entries, and IPv4/IPv6 filtering.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_hosts_file_header` | str | *(default Windows header)* | Header content for the hosts file |
| `windows_manage_hosts_file_self_add` | bool | `false` | Add host self-entry from Ansible facts |
| `windows_manage_hosts_file_self_domain` | str | `null` | Override domain for self-entry |
| `windows_manage_hosts_file_entries` | list(str) | `[]` | Custom host entries (IP HOSTNAME format) |
| `windows_manage_hosts_file_omit_entries` | str | `none` | Filter: `none`, `ipv4`, or `ipv6` |

## Example Playbook

```yaml
- name: Configure hosts file
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_hosts_file
      vars:
        windows_manage_hosts_file_entries:
          - "192.168.1.10    app.example.com app"
          - "192.168.1.20    db.example.com db"
        windows_manage_hosts_file_self_add: true
```

## License

GPL-3.0-or-later
