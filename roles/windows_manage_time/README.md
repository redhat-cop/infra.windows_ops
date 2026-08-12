windows_manage_time
===================

A role to configure Windows NTP servers and timezone.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18

Role Variables
--------------

* **windows_manage_time_ntp_servers**: List of NTP server addresses. Default is **[time.windows.com]**
* **windows_manage_time_timezone**: Timezone identifier (use `tzutil /l` on Windows for valid values). Default is **UTC**
* **windows_manage_time_reboot**: Whether to reboot after timezone changes. Default is **true**

Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Configure time settings
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_time
          vars:
            windows_manage_time_ntp_servers:
              - time.windows.com
              - pool.ntp.org
            windows_manage_time_timezone: "Eastern Standard Time"
            windows_manage_time_reboot: true

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
