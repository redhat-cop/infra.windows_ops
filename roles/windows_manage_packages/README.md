# windows_manage_packages

Install and remove Windows software packages (MSI, EXE, or MSIX) with
`ansible.windows.win_package`, with optional reboot handling.

Packages are identified by a local path or URL together with a `product_id`
and are ensured present or absent. This is a native replacement for
Chocolatey-based package management and has no third-party dependencies.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_packages_install` | list(dict) | `[]` | Packages to ensure are installed (see item keys below) |
| `windows_manage_packages_remove` | list(dict) | `[]` | Packages to ensure are removed (see item keys below) |
| `windows_manage_packages_reboot` | bool | `false` | Allow reboot after changes; only reboots when a changed package reports a reboot is required |
| `windows_manage_packages_reboot_timeout` | int | `3600` | Maximum time in seconds to wait for the host to reboot |

Each item in `windows_manage_packages_install` and
`windows_manage_packages_remove` supports:

| Key | Required | Description |
|---|---|---|
| `path` | see note | Local path or URL to the package file (MSI/EXE/MSIX) |
| `product_id` | see note | Product ID used to determine install state |
| `arguments` | no | Installer arguments (string or list) |
| `expected_return_code` | no | List of return codes treated as success |
| `creates_path` | no | Path expected to exist once installed |
| `creates_service` | no | Service expected to exist once installed |
| `creates_version` | no | Version of the file at `creates_path` |

> **Note:** At least one of `path` or `product_id` is required per item. For
> reliable idempotency, provide `product_id` whenever it is known.

## Example Playbook

```yaml
- name: Manage Windows packages
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_packages
      vars:
        windows_manage_packages_reboot: true
        windows_manage_packages_install:
          - path: https://www.7-zip.org/a/7z2408-x64.msi
            product_id: '{23170F69-40C1-2702-2408-000001000000}'
        windows_manage_packages_remove:
          - product_id: '{OLD-PRODUCT-GUID-HERE}'
```

## License

GPL-3.0-or-later
