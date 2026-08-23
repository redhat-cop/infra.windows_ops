# windows_manage_environment

Manage Windows environment variables and PATH settings.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_environment_paths` | list(dict) | `[]` | PATH-like environment settings. Each item: `scope` (machine/user), `name`, `elements`, `state` (present/absent), optional `reboot`. |
| `windows_manage_environment_variables` | list(dict) | `[]` | Environment variable settings. Each item: `level` (machine/user), `variables` (name/value mapping), optional `reboot`. Set a value to `''` to remove it. |
| `windows_manage_environment_reboot` | bool | `true` | Reboot after changes when a changed item requested it via `reboot: true`. |

## Example Playbook

```yaml
- name: Configure environment settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_environment
      vars:
        windows_manage_environment_reboot: false
        windows_manage_environment_paths:
          - scope: machine
            name: PATH
            elements:
              - C:\Tools\bin
            state: present
        windows_manage_environment_variables:
          - level: machine
            variables:
              JAVA_HOME: C:\Java
              LEGACY_VAR: ''
```

## License

GPL-3.0-or-later
