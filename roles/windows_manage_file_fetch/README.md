# windows_manage_file_fetch

Fetch files from remote Windows hosts to the Ansible controller.

## Requirements

- Ansible >= 2.18

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_file_fetch_files` | list(dict) | `[]` | Files to fetch (`src`, `dest`, optional `flat`, `fail_on_missing`, `validate_checksum`) |

## Example Playbook

```yaml
- name: Fetch files from Windows hosts
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_file_fetch
      vars:
        windows_manage_file_fetch_files:
          - src: C:\Temp\log.txt
            dest: /tmp/log-{{ inventory_hostname }}.txt
            flat: true
            validate_checksum: false
```

## License

GPL-3.0-or-later
