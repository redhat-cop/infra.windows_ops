# windows_manage_firewall

Manage Windows firewall profiles and rules.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| **windows_manage_firewall_profiles_disable** | Firewall profiles to disable | list(dict) | `[]` |
| **windows_manage_firewall_profiles_enable** | Firewall profiles to enable | list(dict) | `[]` |
| **windows_manage_firewall_rules_disable** | Firewall rules to disable | list(dict) | `[]` |
| **windows_manage_firewall_rules_enable** | Firewall rules to enable | list(dict) | `[]` |

Each profile item should have a `profiles` key with a list of profile names (`domain`, `private`, `public`). Optional keys `inbound_action` and `outbound_action` set default actions.

Each rule item uses `community.windows.win_firewall_rule` parameters (`name`, `localport`, `protocol`, `action`, `direction`, `profiles`, etc.).

Items present in both disable and enable lists are skipped from the disable operation.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_firewall
      vars:
        windows_manage_firewall_profiles_enable:
          - profiles:
              - domain
              - private
              - public
        windows_manage_firewall_rules_enable:
          - name: OpenSSH SSH Server (sshd)
            localport: 22
            action: allow
            direction: in
            protocol: tcp
            profiles:
              - domain
              - private
              - public
```

## License

GPL-3.0-or-later

## Author

Ansible Ecosystem Engineering team (@eco-ansible-content)
