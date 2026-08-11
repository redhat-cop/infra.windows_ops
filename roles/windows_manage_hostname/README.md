windows_manage_hostname
=======================

A role to configure the Windows system hostname with validation and optional reboot.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18

Role Variables
--------------

* **windows_manage_hostname_name**: The hostname to configure on the system. Should be a short name (not FQDN) and valid for DNS. Max 63 characters. Required.
* **windows_manage_hostname_reboot**: Whether to reboot the system after a hostname change. A reboot is required for the change to take effect. Default is **true**

Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Configure system hostname
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_hostname
          vars:
            windows_manage_hostname_name: "WEBSERVER01"
            windows_manage_hostname_reboot: true

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
