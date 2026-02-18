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
[infra.windows_ops.windows_manage_iis](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_iis/README.md)|A role to manage IIS Web Server.
[infra.windows_ops.windows_manage_service](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_service/README.md)|A role to manage Windows Services.
[infra.windows_ops.windows_manage_updates](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_updates/README.md)|A role to manage Windows Updates.

#### Security and Compliance
Name | Description
--- | ---
[infra.windows_ops.windows_manage_cis](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_cis/README.md)|A role to enforce CIS Microsoft Windows Server 2022 Benchmark compliance.
[infra.windows_ops.windows_manage_stig](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_stig/README.md)|A role to enforce DISA STIG compliance for Windows Server 2019, 2022, and 2025.


## Supported Platforms

### DISA STIG Compliance

The `windows_manage_stig` role supports the following Windows Server versions:

- **Windows Server 2019** - DISA STIG V3R7 (284 controls)
- **Windows Server 2022** - DISA STIG V2R7 (283 controls)
- **Windows Server 2025** - DISA STIG V1R0-1 (281 controls)

### Coverage Statistics

The role achieves **100% coverage** of DISA STIG requirements through a combination of automated enforcement and detailed manual verification documentation.

| Platform | STIG Version | Automated Controls | Manual Controls | Total Coverage |
|----------|--------------|-------------------|-----------------|----------------|
| Windows Server 2019 | V3R7 | 248 automated | 36 documented | **100%** |
| Windows Server 2022 | V2R7 | 274 automated | 9 documented | **100%** |
| Windows Server 2025 | V1R0-1 | 248 automated | 33 documented | **100%** |

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
