# windows_manage_capabilities

Install or remove Windows capabilities (Features on Demand / FoD) via DISM.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

Windows capabilities are managed natively by the `ansible.windows.win_capability`
module, so no PowerShell shim is required.

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_capabilities_install` | list | `[]` | Capabilities to install. Each item is a capability name string, or a mapping with `name` and optional `source`/`disable_windows_update`. |
| `windows_manage_capabilities_remove` | list(str) | `[]` | Capability names to remove. Names also present in `windows_manage_capabilities_install` are skipped. |
| `windows_manage_capabilities_remove_ignore_unknown` | bool | `true` | Ignore failures when removing capabilities that are not present or unknown. |
| `windows_manage_capabilities_reboot` | bool | `true` | Reboot automatically when a capability change requires it. |
| `windows_manage_capabilities_log_level` | int | `1` | DISM logging level (`0`-`3`). |
| `windows_manage_capabilities_log_path` | str | _(unset)_ | Path to the DISM log file. When unset, the default DISM log location is used. |

## Example Playbook

```yaml
- name: Manage Windows capabilities
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_capabilities
      vars:
        windows_manage_capabilities_install:
          - OpenSSH.Client
          - name: OpenSSH.Server
            disable_windows_update: true
        windows_manage_capabilities_remove:
          - Browser.InternetExplorer
          - Media.WindowsMediaPlayer
        windows_manage_capabilities_reboot: true
```

## License

GPL-3.0-or-later
