windows_manage_description
==========================

A role to configure the Windows system description, organization, and owner fields.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18

Role Variables
--------------

All variables are optional. Undefined variables are not modified. Use an empty string to clear a field.

* **windows_manage_description_organization**: The registered organization for the system.
* **windows_manage_description_owner**: The registered owner of the system.
* **windows_manage_description_text**: The system description text.

Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Configure system description
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_description
          vars:
            windows_manage_description_organization: "Red Hat"
            windows_manage_description_owner: "Ansible Team"
            windows_manage_description_text: "Managed by Ansible"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Ecosystem Engineering team (@eco-ansible-content)
