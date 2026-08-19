# windows_manage_network

Configure Windows network settings including IPv6, NetBIOS, LMHOSTS lookup, and static routes.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_network_ipv6_enable` | bool | `true` | Enable or disable IPv6 on all interfaces |
| `windows_manage_network_lmhosts_enable` | bool | `true` | Enable or disable LMHOSTS lookup |
| `windows_manage_network_netbios_enable` | bool | `true` | Enable or disable NetBIOS on all interfaces |
| `windows_manage_network_reboot` | bool | `true` | Reboot when a change requires it (false = DNS flush only) |
| `windows_manage_network_routes` | list(dict) | `[]` | Static route configurations |

> **Note:** IPv6, LMHOSTS, and NetBIOS are enforced to their configured values
> on every run (full-state), so running the role only to manage routes still
> applies those settings. Static routes are additive — only the routes listed
> in `windows_manage_network_routes` are managed; any others are left untouched.

Each route item supports:

| Key | Type | Required | Description |
|---|---|---|---|
| `destination` | str | yes | Network destination in CIDR format |
| `gateway` | str | no | Gateway IP address (defaults to `0.0.0.0`) |
| `metric` | int | no | Route metric value (defaults to `1`) |
| `state` | str | yes | `present` or `absent` |

## Example Playbook

```yaml
- name: Configure network settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_network
      vars:
        windows_manage_network_ipv6_enable: false
        windows_manage_network_netbios_enable: false
        windows_manage_network_lmhosts_enable: false
        windows_manage_network_reboot: false
        windows_manage_network_routes:
          - destination: 192.168.100.0/24
            gateway: 10.0.0.1
            metric: 1
            state: present
```

## License

GPL-3.0-or-later
