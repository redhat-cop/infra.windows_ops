# windows_manage_file_create

Create directories and files on Windows hosts and optionally set their owner.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_file_create_items` | list(dict) | `[]` | Directories and files to create |

Each item in `windows_manage_file_create_items`:

| Key | Description |
|---|---|
| `state` | `directory` or `file` (required) |
| `path` | Target path (required) |
| `owner` | Owner to set via `win_owner` (optional) |
| `recurse` | Recurse when setting owner (optional) |
| `access_time` / `access_time_format` | File access time (optional, files only) |
| `modification_time` / `modification_time_format` | File modification time (optional, files only) |

## Example Playbook

```yaml
- name: Create files and directories
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_file_create
      vars:
        windows_manage_file_create_items:
          - state: directory
            path: C:\Tools
            owner: BUILTIN\Administrators
            recurse: true
          - state: file
            path: C:\Tools\log.txt
```

## License

GPL-3.0-or-later
