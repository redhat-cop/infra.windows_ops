# windows_manage_performance

Apply common Windows performance tuning settings: NTFS last access time updates, page file configuration, the active power scheme, and hibernation.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_performance_ntfs_last_access_time_update` | bool | `false` | Enable or disable NTFS Last Access Time updates |
| `windows_manage_performance_page_file_size` | str | `auto` | `auto`, `disabled`, `system`, or a static size in MB (e.g. `"4096"`) |
| `windows_manage_performance_page_file_disk` | str | `C` | Drive letter hosting the page file (static/system managed) |
| `windows_manage_performance_page_file_reboot` | bool | `true` | Reboot when a page file change requires it |
| `windows_manage_performance_power_scheme` | str | `balanced` | Active power scheme: `balanced`, `power_saver`, or `high_performance` |
| `windows_manage_performance_hibernation` | bool | `false` | Enable or disable hibernation |

## Example Playbook

```yaml
- name: Tune Windows performance
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_performance
      vars:
        windows_manage_performance_ntfs_last_access_time_update: false
        windows_manage_performance_page_file_size: auto
        windows_manage_performance_power_scheme: high_performance
        windows_manage_performance_hibernation: false
```

## Notes

Windows power schemes and hibernation are managed through `powercfg.exe`. There
is no native `ansible.windows`/`community.windows` module for these operations,
so the role uses `ansible.windows.win_command` (read-only power scheme query)
and `ansible.windows.win_powershell` (power scheme activation and hibernation
toggle). Both PowerShell steps honour check mode and only report `changed` when
the target state differs from the current state.

## License

GPL-3.0-or-later
