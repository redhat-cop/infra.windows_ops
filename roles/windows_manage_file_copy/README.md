# windows_manage_file_copy

Copy files and render templates to Windows hosts, optionally setting the path owner.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_file_copy_files` | list(dict) | `[]` | Files/directories to copy (`dest` plus `src` or `content`, optional `force`, `backup`, `remote_src`, `local_follow`, `owner`) |
| `windows_manage_file_copy_templates` | list(dict) | `[]` | Templates to render (`src`, `dest`, optional Jinja2 delimiter/formatting overrides, `owner`) |

## Example Playbook

```yaml
- name: Copy files and templates
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_file_copy
      vars:
        windows_manage_file_copy_files:
          - src: files/app.conf
            dest: C:\Tools\app.conf
            owner: BUILTIN\Administrators
        windows_manage_file_copy_templates:
          - src: settings.conf.j2
            dest: C:\Tools\settings.conf
```

## License

GPL-3.0-or-later
