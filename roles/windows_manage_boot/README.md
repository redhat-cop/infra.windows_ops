# windows_manage_boot

Configure Windows Boot Manager settings such as the boot menu timeout.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_boot_timeout` | int | `30` | Boot Manager menu timeout in seconds (applied via `bcdedit /timeout` only when it differs from the current value) |

## Example Playbook

```yaml
- name: Configure Windows boot settings
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_boot
      vars:
        windows_manage_boot_timeout: 10
```

## License

GPL-3.0-or-later
