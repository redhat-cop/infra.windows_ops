windows_manage_updates
==================

A role to manage updates on a Windows server.

Requirements
------------

* Windows Server

Role Variables
--------------

* **windows_manage_updates_categories**: Which categories to install.  Default to 'CriticalUpdates', 'SecurityUpdates'
* **windows_manage_updates_state**: State for the updates.  Valid values are 'installed', 'searched', 'downloaded'. Default is **searched**
* **windows_manage_updates_reboot**: If the server should reboot.  Valued values are 'Yes', 'No'. Default is **Yes**


Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: localhost
      tasks:
        - name: Install Critical and Security updates
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_updates
          vars:
            windows_manage_updates_categories:
              - CriticalUpdates
              - SecurityUpdates
            windows_manage_updates_state: installed
            windows_manage_updates_reboot: yes

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
