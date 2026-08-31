# windows_manage_wsl

Install, configure, and remove the Windows Subsystem for Linux (WSL) and its distributions.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- Windows Server 2022 or later

## Notes

WSL is managed through the `wsl.exe` CLI, for which there is no native
`ansible.windows`/`community.windows` module. This role therefore uses
`ansible.windows.win_powershell` for the `wsl.exe` operations (a confirmed
native-module gap); each step reads current state first so the role stays
idempotent. Installing or uninstalling WSL requires a reboot to complete, and
installing distributions requires network access.

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_wsl_enable` | bool | `true` | Install (`true`) or uninstall (`false`) WSL |
| `windows_manage_wsl_update` | bool | `false` | Update WSL during configuration (no check-mode support) |
| `windows_manage_wsl_config_file` | str | `""` | Template to install as `%USERPROFILE%\.wslconfig` (empty = skip); the role ships `disable_cgroup_v1` |
| `windows_manage_wsl_reboot` | bool | `true` | Reboot after a WSL install or uninstall |
| `windows_manage_wsl_distributions` | list(str) | `[]` | Distributions to install |
| `windows_manage_wsl_distributions_exclusive` | bool | `false` | Remove installed distributions not in the list above |
| `windows_manage_wsl_distribution_default` | str | `""` | Distribution to set as default (empty = keep current) |
| `windows_manage_wsl_distributions_update` | list(str) | install list | Distributions to update in place (no check-mode support) |
| `windows_manage_wsl_distribution_update_commands` | dict | see `defaults/main.yml` | Per-variant update command mapping |

## Example Playbook

```yaml
- name: Configure WSL
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_wsl
      vars:
        windows_manage_wsl_enable: true
        windows_manage_wsl_reboot: true
        windows_manage_wsl_distributions:
          - FedoraLinux-42
        windows_manage_wsl_distribution_default: FedoraLinux-42
        windows_manage_wsl_config_file: disable_cgroup_v1
```

## License

GPL-3.0-or-later
