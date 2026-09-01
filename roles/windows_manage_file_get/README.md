# windows_manage_file_get

Download files to Windows hosts over HTTP/HTTPS with optional ownership.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_file_get_files` | list(dict) | `[]` | Files to download; each item requires `url` and `dest` |
| `windows_manage_file_get_no_log` | bool | `true` | Hide task output when an item defines `url_password` |

Each item in `windows_manage_file_get_files` requires `url` and `dest`. Optional
per-item keys mirror the `ansible.windows.win_get_url` options (for example
`url_username`, `url_password`, `timeout`, `method`, `validate_certs`,
`force_basic_auth`, `use_default_credential`, `use_proxy`, `proxy_url`, `headers`,
`follow_redirects`, `force`, `checksum`, `checksum_algorithm`, `checksum_url`).
When `owner` is set for an item, the downloaded file's owner is updated with
`ansible.windows.win_owner`.

## Example Playbook

```yaml
- name: Download files
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_file_get
      vars:
        windows_manage_file_get_files:
          - url: https://server.example.com/data.zip
            dest: C:\Temp\data.zip
            validate_certs: false
          - url: https://server.example.com/secret.bin
            url_username: admin
            url_password: admin123
            dest: C:\Temp\secret.bin
            owner: BUILTIN\Administrators
```

## License

GPL-3.0-or-later
