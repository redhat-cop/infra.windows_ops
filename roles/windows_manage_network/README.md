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
| `windows_manage_network_reboot` | bool | `true` | Reboot after changes (false = DNS flush only) |
| `windows_manage_network_routes` | list(dict) | `[]` | Static route configurations |

Each route item supports:

| Key | Type | Required | Description |
|---|---|---|---|
| `destination` | str | yes | Network destination in CIDR format |
| `gateway` | str | when present | Gateway IP address |
| `metric` | int | no | Route metric value |
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
