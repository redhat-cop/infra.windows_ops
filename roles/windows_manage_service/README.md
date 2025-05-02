windows_manage_service
==================

A role to Manage Windows Services.

Requirements
------------

* Windows Server

Role Variables
--------------

* **windows_manage_service_name**: The name of the Service.
* **windows_manage_service_state**: The state of the Service. Valid values are 'absent', 'paused', 'started', 'stopped', 'restarted'.
* **windows_manage_service_start_mode**: The start mode of the service. Valied values are 'auto', 'delayed', 'disabled', 'manual'. Default is **auto**


Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: localhost
      tasks:
        - name: Enable Print Service
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_service
          vars:
            windows_manage_service_name: spooler
            windows_manage_service_start_mode: restarted

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
