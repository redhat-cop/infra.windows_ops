# windows_manage_sshd

Manage OpenSSH Server on Windows.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| **windows_manage_sshd_enable** | Enable or disable sshd | bool | `true` |
| **windows_manage_sshd_start_mode** | Service start mode | str | `auto` |
| **windows_manage_sshd_shell** | Default shell for SSH sessions | str | |
| **windows_manage_sshd_admins_keys** | Administrators SSH keys (present/absent) | dict | `{}` |
| **windows_manage_sshd_firewall_profiles** | Firewall profiles for SSH rule | list | `[domain, private, public]` |
| **windows_manage_sshd_config_validate** | Validate config before applying | bool | `true` |
| **windows_manage_sshd_config_file** | Template file for sshd_config | str | |
| **windows_manage_sshd_options** | Dictionary of sshd_config directives | dict | `{}` |

### Configuration Methods

The role supports two mutually exclusive methods for configuring sshd:

1. **Template file** (`windows_manage_sshd_config_file`): Path to a Jinja2 template. The role provides a `default_config` template matching OpenSSH.Server 0.0.1.0 defaults.

2. **Options dictionary** (`windows_manage_sshd_options`): Key-value pairs rendered into sshd_config. Supports Match blocks with indented sub-options.

### Administrators SSH Keys

```yaml
windows_manage_sshd_admins_keys:
  present:
    - ssh-ed25519 AAAA... admin@host
  absent:
    - ssh-rsa AAAA... old-key@host
```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_sshd
      vars:
        windows_manage_sshd_shell: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
        windows_manage_sshd_options:
          AuthorizedKeysFile: .ssh/authorized_keys
          GSSAPIAuthentication: "yes"
          Subsystem: sftp sftp-server.exe
          AllowGroups: administrators "openssh users"
          Match Group administrators:
            - AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
```

## License

GPL-3.0-or-later

## Author

Red Hat Ansible Content Team
