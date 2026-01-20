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
[infra.windows_ops.windows_manage_stig](https://github.com/redhat-cop/infra.windows_ops/blob/main/roles/windows_manage_stig/README.md)|A role to enforce DISA STIG Windows Server 2022 compliance.


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
