windows_manage_init
===================

A role to run one-time system initialization tasks on Windows. Creates a marker file to ensure initialization runs only once, with optional event log writing and reboot.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18
* `community.windows` collection (for event log support)

Role Variables
--------------

* **windows_manage_init_file**: Path to the init marker file. Default is **C:\Windows\init_info_system.txt**
* **windows_manage_init_message**: Message written to the init marker file. Default is **"System initialized by Ansible"**
* **windows_manage_init_log_message**: Event log message. Default is **""** (empty, skips event log)
* **windows_manage_init_final_actions**: List of final actions. Supported values: `reboot`, `syslog`. Default is **[]**

Dependencies
------------

- community.windows (>=3.0.0) — for `win_eventlog_entry` when using syslog action

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Run system initialization
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_init
          vars:
            windows_manage_init_message: "Provisioned by Ansible on {{ ansible_date_time.date }}"
            windows_manage_init_log_message: "System initialization complete"
            windows_manage_init_final_actions:
              - syslog
              - reboot

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
