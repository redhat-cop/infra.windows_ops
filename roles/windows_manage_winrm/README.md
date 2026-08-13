# windows_manage_winrm

Configure Windows Remote Management (WinRM) service, listeners, and firewall rules.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_winrm_enable` | bool | `true` | Enable or disable WinRM service |
| `windows_manage_winrm_start_mode` | str | `auto` | Service start mode (`auto` or `delayed`) |
| `windows_manage_winrm_http_block` | bool | `false` | Block HTTP port 5985 in firewall |
| `windows_manage_winrm_https_enable` | bool | `false` | Enable HTTPS listener with self-signed cert |
| `windows_manage_winrm_service_config` | dict | *(see defaults)* | WinRM service configuration |
| `windows_manage_winrm_firewall_profiles` | list(str) | `[domain, private]` | Firewall profiles for rules |
| `windows_manage_winrm_display_config` | bool | `false` | Display current configuration |

## Example Playbook

```yaml
- name: Configure WinRM
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_winrm
      vars:
        windows_manage_winrm_enable: true
        windows_manage_winrm_https_enable: true
        windows_manage_winrm_service_config:
          AllowUnencrypted: false
          Auth:
            Basic: false
            Kerberos: true
            Negotiate: true
            Certificate: false
            CredSSP: false
            CbtHardeningLevel: Strict
```

## Safety

The role refuses to disable WinRM when connected via WinRM or PSRP to prevent self-lockout.

## License

GPL-3.0-or-later
