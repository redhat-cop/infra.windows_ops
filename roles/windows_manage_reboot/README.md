windows_manage_reboot
=====================

A role to reboot a Windows system with configurable delays, timeout, and user message.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18

Role Variables
--------------

* **windows_manage_reboot_timeout**: Maximum time in seconds to wait for the system to reboot and become reachable. Default is **600**
* **windows_manage_reboot_delay_pre**: Delay in seconds before initiating the reboot. Default is **2**
* **windows_manage_reboot_delay_post**: Delay in seconds after the reboot before continuing with tasks. Default is **0**
* **windows_manage_reboot_message**: Message displayed to logged-in users before the reboot. Default is **Reboot initiated by Ansible**

Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Reboot the system
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_reboot
          vars:
            windows_manage_reboot_timeout: 300
            windows_manage_reboot_message: "Scheduled maintenance reboot"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
