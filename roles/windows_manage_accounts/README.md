# windows_manage_accounts

Manage local Windows user accounts, groups, group memberships, user rights, and profiles.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_accounts_administrator_enable` | bool | `false` | Enable or disable the built-in Administrator account |
| `windows_manage_accounts_ansible_user_password_expires` | bool | `false` | Allow the Ansible connection user's password to expire |
| `windows_manage_accounts_ansible_user_show_on_welcome` | bool | `false` | Show or hide the Ansible connection user on the Welcome Screen |
| `windows_manage_accounts_no_log` | bool | `true` | Value for `no_log` on tasks that set passwords |
| `windows_manage_accounts_profiles_delete` | list(str) | `[]` | User profiles to delete (user name or SID) |
| `windows_manage_accounts_users_delete` | list(str) | `[]` | Local users to delete |
| `windows_manage_accounts_groups_delete` | list(str) | `[]` | Local groups to delete |
| `windows_manage_accounts_groups_create` | list(dict) | `[]` | Local groups to create (`name`, `description`, `members`) |
| `windows_manage_accounts_users_create` | list(dict) | `[]` | Local users to create (`name` plus optional attributes) |
| `windows_manage_accounts_group_members` | list(dict) | `[]` | Group memberships to configure (`name`, `members`, `state`) |
| `windows_manage_accounts_users_rights` | list(dict) | `[]` | User rights to configure (`name`, `users`, `action`) |
| `windows_manage_accounts_profiles_create` | list(dict) | `[]` | User profiles to create (`username`, optional `name`) |

Reserved account names (`administrator`, `guest`, `krbtgt`, `local`, `none`) are never created or
deleted. The role refuses to disable the Administrator account when it is the connecting user.

## Example Playbook

```yaml
- name: Manage local accounts
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_accounts
      vars:
        windows_manage_accounts_groups_create:
          - name: testgroup
            description: Test Group
        windows_manage_accounts_users_create:
          - name: testuser
            fullname: Test User
            description: User for testing
            password: Foobar_12
            groups:
              - Users
        windows_manage_accounts_group_members:
          - name: testgroup
            members:
              - testuser
            state: pure
```

## License

GPL-3.0-or-later
