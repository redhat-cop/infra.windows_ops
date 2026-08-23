# windows_manage_dotnet

Optimize .NET native images (ngen) for PowerShell and installed assemblies.

Compiling native images speeds up .NET/PowerShell startup, which improves the
responsiveness of subsequent Ansible operations over WinRM/PowerShell.

> **Note:** This is a maintenance action. The PowerShell-assembly step is
> idempotent (it only compiles images that are pending or not installed);
> compiling all assemblies may report `changed` while ngen processes its queue.

## Requirements

- Ansible >= 2.18
- `ansible.windows` collection
- `community.windows` collection

## Role Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `windows_manage_dotnet_powershell` | bool | `true` | Compile the PowerShell assemblies used by Ansible connections |
| `windows_manage_dotnet_all_assemblies` | bool | `false` | Compile all installed .NET assemblies (can be slow) |

## Example Playbook

```yaml
- name: Optimize .NET native images
  hosts: windows
  roles:
    - role: infra.windows_ops.windows_manage_dotnet
      vars:
        windows_manage_dotnet_powershell: true
        windows_manage_dotnet_all_assemblies: false
```

## License

GPL-3.0-or-later
