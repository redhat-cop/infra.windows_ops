# windows_manage_dsc3

Apply Windows Desired State Configuration (DSC) v3 configuration documents with optional reboot handling.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- The DSC v3 engine (`dsc`) installed on the target host and discoverable via the
  `PATH` environment variable (`dsc` itself also relies on `PATH` for resource
  discovery)

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_dsc3_settings` | list(dict) | `[]` | DSC v3 configurations to apply |
| `windows_manage_dsc3_reboot` | bool | `false` | Reboot after DSC v3 changes when a changed setting requests it |
| `windows_manage_dsc3_reboot_timeout` | int | `3600` | Timeout in seconds for the reboot after DSC v3 changes |

Each item in `windows_manage_dsc3_settings` accepts:

| Key | Type | Required | Description |
|---|---|---|---|
| `setting` | str | yes | Human-readable label shown in task output |
| `config` | dict | one of `config`/`config_file` | Inline DSC v3 configuration document |
| `config_file` | path | one of `config`/`config_file` | Path to a DSC v3 configuration document |
| `remote_config_file` | bool | no | Whether `config_file` already exists on the target host (`true`) or is transferred from the control node (`false`) |
| `parameters` | dict | no | Runtime parameter values for the configuration document |
| `trace_level` | str | no | `dsc` trace level (`error`, `warn`, `info`, `debug`, `trace`) |
| `reboot` | bool | no (`false`) | Whether a reboot is required after this setting changes |

Each item must specify **exactly one** of `config` or `config_file`.

## Notes

- The role uses the native `ansible.windows.dsc3` module, which calls
  `dsc config set` (or `dsc config test` in check mode) with the supplied
  configuration document.
- This role targets DSC **v3** and is distinct from `windows_manage_dsc`, which
  applies classic PowerShell DSC resources via `ansible.windows.win_dsc`.

## Example Playbook

```yaml
- name: Apply DSC v3 settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_dsc3
      vars:
        windows_manage_dsc3_reboot: true
        windows_manage_dsc3_settings:
          - setting: Set an environment variable
            config:
              resources:
                - name: Set MY_VAR
                  type: Microsoft.Windows/Registry
                  properties:
                    keyPath: HKLM\SOFTWARE\ExampleApp
                    valueName: MyValue
                    valueData:
                      String: enabled
            reboot: false
```

## License

GPL-3.0-or-later
