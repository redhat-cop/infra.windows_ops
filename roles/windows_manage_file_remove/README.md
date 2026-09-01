# windows_manage_file_remove

Remove files and directories on Windows, with wildcard and exclusion support.

> **Warning:** Be very careful with this role. Typos or unexpected wildcard expansion can remove
> unintended files and directories across all managed systems with no confirmation.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_file_remove_paths` | list(str) | `[]` | Files and directories to remove (wildcards allowed in the last element only) |
| `windows_manage_file_remove_recursive` | bool | `false` | Use recursive find for wildcard patterns |
| `windows_manage_file_remove_exclude` | list(str) | `[]` | Full paths to exclude from removal (no wildcards) |
| `windows_manage_file_remove_case_sensitive` | bool | `false` | Case-sensitive wildcard matching |

## Example Playbook

```yaml
- name: Remove temporary files
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_file_remove
      vars:
        windows_manage_file_remove_paths:
          - C:\Temp\log.txt
          - C:\Temp\*.old
        windows_manage_file_remove_exclude:
          - C:\Temp\keep.old
        windows_manage_file_remove_recursive: false
```

## License

GPL-3.0-or-later
