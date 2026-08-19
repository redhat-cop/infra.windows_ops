# windows_manage_dns_client

Configure Windows DNS client settings including DNS servers and suffix search lists per network adapter.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection (>= 3.1.0 required to set `suffix_search_list`)

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_dns_client_configurations` | list(dict) | `[]` | List of DNS client configurations to apply |

Each configuration item supports:

| Key | Type | Required | Description |
|---|---|---|---|
| `adapter_names` | str/list | yes | Adapter name(s) to configure (`'*'` for all) |
| `dns_servers` | list(str) | yes | Ordered list of DNS server IP addresses |
| `suffix_search_list` | list(str) | no | DNS suffix search list for name resolution (requires `ansible.windows` >= 3.1.0) |

## Example Playbook

```yaml
- name: Configure DNS client
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_dns_client
      vars:
        windows_manage_dns_client_configurations:
          - adapter_names: '*'
            dns_servers:
              - 10.0.0.1
              - 10.0.0.2
            suffix_search_list:
              - example.com
              - corp.example.com
```

## License

GPL-3.0-or-later
