# windows_manage_scheduled_tasks

Create, enable, disable, and remove Windows scheduled tasks.

## Requirements

- Ansible >= 2.18
- `community.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_scheduled_tasks_create` | list(dict) | `[]` | Scheduled tasks to create, enable, or disable. Each item is passed to `community.windows.win_scheduled_task`; `name` is required. |
| `windows_manage_scheduled_tasks_remove` | list(str) | `[]` | Scheduled task names to remove. A name also present in `windows_manage_scheduled_tasks_create` is skipped. |

Each item in `windows_manage_scheduled_tasks_create` accepts the keys supported by
the [`community.windows.win_scheduled_task`](https://docs.ansible.com/ansible/latest/collections/community/windows/win_scheduled_task_module.html)
module (for example `actions`, `triggers`, `description`, `username`, `password`,
`logon_type`, `run_level`, and `path`). Set `enabled: false` to create a disabled
task; when `enabled` is omitted the task is enabled.

## Example Playbook

```yaml
- name: Manage scheduled tasks
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_scheduled_tasks
      vars:
        windows_manage_scheduled_tasks_create:
          - name: Report system info
            description: Daily system info update
            enabled: true
            actions:
              - path: cmd.exe
                arguments: /c systeminfo.exe > \Windows\Temp\systeminfo.txt
            triggers:
              - type: daily
                start_boundary: '2026-01-01T00:00:00'
            username: SYSTEM
        windows_manage_scheduled_tasks_remove:
          - Obsoleted task
```

## License

GPL-3.0-or-later
