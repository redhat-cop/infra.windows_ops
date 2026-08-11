windows_manage_recovery
=======================

A role to manage Windows Recovery Environment (WinRE). Enables or disables WinRE and optionally removes the Recovery partition data when disabling.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18

Role Variables
--------------

* **windows_manage_recovery_enable**: Whether to enable or disable Windows Recovery Environment. When set to `false`, also removes `C:\Recovery` directory. Default is **false**

Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Disable Windows Recovery Environment
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_recovery
          vars:
            windows_manage_recovery_enable: false

        - name: Enable Windows Recovery Environment
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_recovery
          vars:
            windows_manage_recovery_enable: true

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
