windows_manage_service
==================

A role to manage the lifecycle of Windows services. It controls the state and
start mode of existing services and can optionally create or reconfigure a
service (binary path, display name, description, dependencies, run-as account)
via `ansible.windows.win_service`. The resulting service state is reported with
`ansible.windows.win_service_info`.

Requirements
------------

* Windows Server

Role Variables
--------------

* **windows_manage_service_name**: The name of the service. Required.
* **windows_manage_service_state**: The state of the service. Required. Valid values are `absent`, `paused`, `started`, `stopped`, `restarted`.
* **windows_manage_service_start_mode**: The start mode of the service. Valid values are `auto`, `delayed`, `disabled`, `manual`. Default is `auto`.

The following optional variables enable service creation and reconfiguration.
When unset they are omitted from the underlying module call, so callers that
only manage state and start mode are unaffected.

* **windows_manage_service_path**: Path to the service executable. Supplying this creates the service if it does not exist, or reconfigures its binary path. Optional.
* **windows_manage_service_display_name**: The display name to set for the service. Optional.
* **windows_manage_service_description**: The description to set for the service. Optional.
* **windows_manage_service_dependencies**: A list of service names (not display names) this service depends on. Optional.
* **windows_manage_service_username**: The account the service runs as (e.g. `LocalSystem`, a local/domain account, or a gMSA `DOMAIN\gMSA$`). Optional.
* **windows_manage_service_password**: The password for the run-as account. Should be supplied together with `windows_manage_service_username` for a local or domain account. Marked `no_log`. Optional.
* **windows_manage_service_force_dependent_services**: If `true`, stopping or restarting a service with dependent services forces those to stop or restart as well. Optional.

Dependencies
------------

- NA

Example Playbook
----------------

Manage the state of an existing service:

    - hosts: windows
      tasks:
        - name: Start the Print Spooler service
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_service
          vars:
            windows_manage_service_name: spooler
            windows_manage_service_state: started
            windows_manage_service_start_mode: auto

Create and start a new service:

    - hosts: windows
      tasks:
        - name: Create the My Application service
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_service
          vars:
            windows_manage_service_name: myapp
            windows_manage_service_state: started
            windows_manage_service_start_mode: auto
            windows_manage_service_path: 'C:\Program Files\MyApp\myapp.exe'
            windows_manage_service_display_name: "My Application Service"
            windows_manage_service_description: "Runs the My Application background worker."
            windows_manage_service_dependencies:
              - Tcpip
              - Dnscache

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
