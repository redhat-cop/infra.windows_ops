# windows_manage_dsc

Apply Windows PowerShell Desired State Configuration (DSC) resource configurations with optional reboot handling.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- PowerShell 5.0 or newer on the target host (required by `ansible.windows.win_dsc`)

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_dsc_settings` | list(dict) | `[]` | DSC resource configurations to apply |
| `windows_manage_dsc_reboot` | bool | `true` | Reboot after DSC changes when a changed setting requests it |

Each item in `windows_manage_dsc_settings` accepts:

| Key | Type | Required | Description |
|---|---|---|---|
| `setting` | str | yes | Human-readable label shown in task output |
| `resource_name` | str | yes | DSC resource to invoke (e.g. `Registry`, `File`, `Environment`) |
| `parameters` | dict | yes | Mapping of DSC resource properties passed to `win_dsc` |
| `reboot` | bool | no (`false`) | Whether a reboot is required after this setting changes |

## Notes

- The role uses the native `ansible.windows.win_dsc` module. Resource properties are
  dynamic, so `parameters` is passed through with the task-level `args` keyword.
- A few DSC resources (for example `Registry`, `File`, `Environment`, `Archive`,
  `Script`) ship built in with PowerShell 5.0. Custom resources must be installed on
  the target host separately.

## Example Playbook

```yaml
- name: Apply DSC settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_dsc
      vars:
        windows_manage_dsc_reboot: true
        windows_manage_dsc_settings:
          - setting: Enable User Account Control (UAC)
            resource_name: Registry
            parameters:
              Key: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
              ValueName: EnableLUA
              ValueType: DWord
              ValueData: 1
              Ensure: Present
            reboot: true
          - setting: Create C:\Temp
            resource_name: File
            parameters:
              DestinationPath: C:\Temp
              Type: Directory
              Ensure: Present
```

## License

GPL-3.0-or-later
