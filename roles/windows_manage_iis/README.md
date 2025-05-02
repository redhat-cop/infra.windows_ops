windows_manage_iis
==================

A role to Create/Delete/Configure an IIS Web server.

Requirements
------------

* Windows Server which is entitled to install IIS

Role Variables
--------------

* **windows_manage_iis_operation**: Operation to perform. Valid values are 'create', 'delete'. Default is **create**
* **windows_manage_iis_name**: The name of the Server.
* **windows_manage_iis_port**: Network port to listen on. Default: 80
* **windows_manage_iis_path**: Location on disk to store Web root.
* **windows_manage_iis_test_message**: The test message that will be used in the index.html.
* **windows_mamage_iis_delete_option**: Relevant for **delete** operation. Valid values are 'all', 'server'. Specifies whether to delete all resources including the IIS service, or only the server. Default is **server**


Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: localhost
      tasks:
        - name: Create IIS server
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_iis
          vars:
            windows_manage_iis_name: iis-server
            windows_manage_iis_operation: create
            windows_manage_iis_port: 80
            windows_manage_iis_path: 'c:\\sites\iis-server'
            windows_manage_iis_test_message: 'IIS Server'

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
