# Windows Roles Collection for Ansible Automation Platform

This repository hosts the `infra.windows_ops` Ansible Collection.

The collection includes a variety of Ansible roles to help automate the management of resources on Microsoft Windows.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.18.0**.

## Included content

Click on the name of a plugin or module to view that content's documentation:

<!--start collection content-->
### Roles

#### Infrastructure Management
Name | Description
--- | ---
[infra.windows_ops.windows_manage_iis](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_iis/README.md)|Role to manage IIS web server on Windows.
[infra.windows_ops.windows_manage_scheduled_tasks](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_scheduled_tasks/README.md)|Create, enable, disable, and remove Windows scheduled tasks.
[infra.windows_ops.windows_manage_service](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_service/README.md)|Manage the lifecycle of Windows services, including creation and reconfiguration.
[infra.windows_ops.windows_manage_updates](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_updates/README.md)|Manage Windows updates including search, download, and install with filtering and retry.

#### System Configuration
Name | Description
--- | ---
[infra.windows_ops.windows_manage_boot](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_boot/README.md)|Configure Windows Boot Manager settings such as the boot menu timeout.
[infra.windows_ops.windows_manage_description](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_description/README.md)|Configure Windows system description, organization, and owner fields.
[infra.windows_ops.windows_manage_disk_cleanup](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_disk_cleanup/README.md)|Reclaim disk space by cleaning superseded Windows Update files and clearing event logs.
[infra.windows_ops.windows_manage_environment](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_environment/README.md)|Manage Windows environment variables and PATH settings.
[infra.windows_ops.windows_manage_hostname](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_hostname/README.md)|Configure Windows system hostname with validation and optional reboot.
[infra.windows_ops.windows_manage_init](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_init/README.md)|Run one-time system initialization tasks on Windows.
[infra.windows_ops.windows_manage_locale](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_locale/README.md)|Configure Windows locale, language, and input settings.
[infra.windows_ops.windows_manage_performance](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_performance/README.md)|Apply Windows performance tuning settings (NTFS, page file, power scheme, hibernation).
[infra.windows_ops.windows_manage_reboot](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_reboot/README.md)|Reboot a Windows system with configurable delays and timeout.
[infra.windows_ops.windows_manage_recovery](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_recovery/README.md)|Manage Windows Recovery Environment (WinRE).
[infra.windows_ops.windows_manage_registry](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_registry/README.md)|Apply system-wide Windows registry settings with ansible.windows.win_regedit.
[infra.windows_ops.windows_manage_time](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_time/README.md)|Configure Windows NTP servers and timezone.

#### Networking and Remote Access
Name | Description
--- | ---
[infra.windows_ops.windows_manage_dns_client](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_dns_client/README.md)|Configure Windows DNS client settings including DNS servers and suffix search lists.
[infra.windows_ops.windows_manage_firewall](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_firewall/README.md)|Manage Windows firewall profiles and rules.
[infra.windows_ops.windows_manage_hosts_file](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_hosts_file/README.md)|Manage Windows hosts file entries with optional self-entry and IPv4/IPv6 filtering.
[infra.windows_ops.windows_manage_network](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_network/README.md)|Configure Windows network settings including IPv6, NetBIOS, LMHOSTS, and static routes.
[infra.windows_ops.windows_manage_rdp](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_rdp/README.md)|Enable or disable Remote Desktop Protocol (RDP) with firewall and authentication settings.
[infra.windows_ops.windows_manage_sshd](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_sshd/README.md)|Manage OpenSSH Server on Windows.
[infra.windows_ops.windows_manage_winrm](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_winrm/README.md)|Configure Windows Remote Management (WinRM) service, listeners, and firewall rules.

#### Software, Features, and Configuration Management
Name | Description
--- | ---
[infra.windows_ops.windows_manage_capabilities](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_capabilities/README.md)|Install or remove Windows capabilities (Features on Demand) via DISM.
[infra.windows_ops.windows_manage_dotnet](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_dotnet/README.md)|Optimize .NET native images (ngen) for PowerShell and installed assemblies.
[infra.windows_ops.windows_manage_dsc](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_dsc/README.md)|Apply Windows PowerShell DSC resource configurations with optional reboot handling.
[infra.windows_ops.windows_manage_dsc3](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_dsc3/README.md)|Apply Windows DSC v3 configurations with optional reboot handling.
[infra.windows_ops.windows_manage_features](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_features/README.md)|Install and remove Windows Server roles and features.
[infra.windows_ops.windows_manage_optional_features](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_optional_features/README.md)|Install and remove Windows optional features.
[infra.windows_ops.windows_manage_packages](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_packages/README.md)|Install and remove Windows software packages with ansible.windows.win_package.
[infra.windows_ops.windows_manage_wsl](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_wsl/README.md)|Install, configure, and remove the Windows Subsystem for Linux (WSL) and its distributions.

#### File Management
Name | Description
--- | ---
[infra.windows_ops.windows_manage_file_acl](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_file_acl/README.md)|Manage Windows file and directory ACLs, ownership, and ACL inheritance.
[infra.windows_ops.windows_manage_file_copy](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_file_copy/README.md)|Copy files and render templates to Windows hosts, optionally setting the path owner.
[infra.windows_ops.windows_manage_file_create](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_file_create/README.md)|Create directories and files on Windows hosts and optionally set their owner.
[infra.windows_ops.windows_manage_file_fetch](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_file_fetch/README.md)|Fetch files from remote Windows hosts to the Ansible controller.
[infra.windows_ops.windows_manage_file_get](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_file_get/README.md)|Download files to Windows hosts over HTTP/HTTPS with optional ownership.
[infra.windows_ops.windows_manage_file_remove](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_file_remove/README.md)|Remove files and directories on Windows, with wildcard and exclusion support.

#### Users and User Experience
Name | Description
--- | ---
[infra.windows_ops.windows_manage_accounts](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_accounts/README.md)|Manage local Windows user accounts, groups, group memberships, rights, and profiles.
[infra.windows_ops.windows_manage_user_experience](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_user_experience/README.md)|Configure Windows user experience settings such as Server Manager auto-launch, network location wizard, and Welcome Screen behavior.
[infra.windows_ops.windows_manage_user_settings](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_user_settings/README.md)|Apply per-user registry settings across existing and logged-in Windows user profiles.

#### Security and Compliance
Name | Description
--- | ---
[infra.windows_ops.windows_manage_audit](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_audit/README.md)|Manage Windows audit policies and audit rules.
[infra.windows_ops.windows_manage_cis](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_cis/README.md)|A role to enforce CIS Microsoft Windows Server 2019, 2022, and 2025 Benchmark compliance.
[infra.windows_ops.windows_manage_stig](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_stig/README.md)|A role to enforce DISA STIG compliance for Windows Server 2019, 2022, and 2025.


## Supported Platforms

### CIS Compliance

The `windows_manage_cis` role supports the following Windows Server versions:

- **Windows Server 2019** - CIS Benchmark v3.0.0
- **Windows Server 2022** - CIS Benchmark v3.0.0
- **Windows Server 2025** - CIS Benchmark v1.0.0

### Key Features

*   **Multi-Version Support:** Single role supports Windows Server 2019, 2022, and 2025 with automatic version detection.
*   **Drift Detection:** Run in check mode to generate compliance reports without applying changes.
*   **Comprehensive Reporting:** Generates detailed JSON/HTML reports showing pass/fail status for every control.
*   **Windows 2025 Features:** Includes support for new 2025 security baselines like Azure Arc integration, Zero Trust Network Access, and AD 32k page support.

### DISA STIG Compliance

The `windows_manage_stig` role supports the following Windows Server versions:

- **Windows Server 2019** - DISA STIG V3R7
- **Windows Server 2022** - DISA STIG V2R7
- **Windows Server 2025** - DISA STIG V1R0

### Coverage Statistics

The role achieves **100% coverage** of DISA STIG requirements through a combination of automated enforcement and detailed manual verification documentation.

| Platform | STIG Version | Automated Controls | Manual Controls | Total Coverage |
|----------|--------------|-------------------|-----------------|----------------|
| Windows Server 2019 | V3R7 | 248 automated | 36 documented | **100%** |
| Windows Server 2022 | V2R7 | 274 automated | 9 documented | **100%** |
| Windows Server 2025 | V1R0 | 248 automated | 33 documented | **100%** |

### Key Features

*   **Version Detection:** Automatically detects the OS version and applies the correct STIG benchmark (2019, 2022, or 2025).
*   **Safe Automation:** High-risk controls that could sever remote administration (e.g., NTLM blocking, specific User Rights) are flagged for manual review to preventing lockouts.
*   **Detailed Reporting:**
    *   **Failed Controls Summary:** A specific list of controls that failed automation, with "Expected" vs "Current" values.
    *   **Manual Controls List:** A clear checklist of items requiring administrative action.
    *   **Advanced Audit Compliance:** Smart validation that accepts "over-compliant" settings (e.g., "Success and Failure" when only "Failure" is required).
*   **Advanced Security Features:** Supports modern Windows security features including DNS-over-HTTPS (DoH), SMB QUIC, TLS 1.3, and Hotpatching.

## Installation and Usage

### Installation

To consume this Validated Content from Automation Hub, please ensure that you add the following lines to your ansible.cfg file.

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```
The token can be obtained from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

Once the above steps are done, you can run the following command to install the collection.

```
ansible-galaxy collection install infra.windows_ops
```

### Using this collection

Once installed, you can reference the infra.windows_ops collection content by its fully qualified collection name (FQCN), for example:

```yaml
- hosts: all
  tasks:
      - name: Create IIS Web Server
        ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_iis
        vars:
            windows_manage_iis_operation: create
            windows_manage_iis_name: MyWebServer
            windows_manage_iis_path: c:\\sites\MyWebServer
            windows_manage_iis_port: 80
            windows_manage_iis_test_message: "This is my test message for MyWebServer"
```

### See Also

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.


## Testing and Development

* This collection is tested using GitHub Actions. To know more about CI, refer to [CI.md](https://github.com/redhat-cop/infra.windows_ops/blob/main/CI.md).
* For more information about testing and development, refer to [CONTRIBUTING.md](https://github.com/redhat-cop/infra.windows_ops/blob/main/CONTRIBUTING.md)


## License

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.
