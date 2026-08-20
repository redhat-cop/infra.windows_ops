# windows_manage_file_acl

Manage Windows file and directory ACLs, ownership, and ACL inheritance.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_file_acl_acls` | list(dict) | `[]` | ACLs to apply. Each item: `path`, `user`, `type`, `rights` (required); optional `state`, `follow`, `inherit`, `propagation`, `owner`, `recurse` |
| `windows_manage_file_acl_inheritance` | list(dict) | `[]` | ACL inheritance rules. Each item: `path` (required); optional `state`, `reorganize` |

When an item in `windows_manage_file_acl_acls` includes `owner`, the path owner is set with
`ansible.windows.win_owner` (with optional `recurse`).

## Example Playbook

```yaml
- name: Manage file ACLs
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_file_acl
      vars:
        windows_manage_file_acl_acls:
          - path: C:\Temp\log.txt
            owner: BUILTIN\Administrators
            user: Guests
            type: deny
            rights: Write,Modify
            state: present
        windows_manage_file_acl_inheritance:
          - path: C:\Temp
            state: absent
            reorganize: true
```

## License

GPL-3.0-or-later
