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
* **windows_manage_updates_accept_list**: List of update titles or KB numbers to restrict which updates are searched or installed. Empty means no restriction. Default is **[]**
* **windows_manage_updates_reject_list**: List of update titles or KB numbers to exclude. Empty means nothing excluded. Default is **[]**
* **windows_manage_updates_skip_optional**: Skip optional updates (BrowseOnly). Default is **false**
* **windows_manage_updates_retry_count**: Number of times to retry the update task on a transient failure. Default is **3**
* **windows_manage_updates_retry_delay**: Seconds to wait between update retry attempts. Default is **60**
* **windows_manage_updates_reboot_timeout**: Maximum seconds to wait for the host to come back online after a reboot. Default is **1200**
* **windows_manage_updates_compile_assemblies**: After a successful update that changed the host, run the `windows_manage_dotnet` role to compile .NET native images. Default is **false**
* **windows_manage_updates_compile_filter**: Optional regex matched against applied update titles; when set, .NET compilation only runs if an applied update title matches. Default is **""** (compile whenever updates changed the host)


Dependencies
------------

- Optionally uses the in-collection `windows_manage_dotnet` role when `windows_manage_updates_compile_assemblies` is enabled (included at runtime; not a hard dependency).

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
            windows_manage_updates_reboot: 'Yes'

    - hosts: localhost
      tasks:
        - name: Install specific security updates with retry and assembly compilation
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_updates
          vars:
            windows_manage_updates_categories:
              - SecurityUpdates
            windows_manage_updates_state: installed
            windows_manage_updates_accept_list:
              - KB5000001
            windows_manage_updates_reject_list:
              - Windows Malicious Software Removal Tool
            windows_manage_updates_skip_optional: true
            windows_manage_updates_retry_count: 5
            windows_manage_updates_retry_delay: 120
            windows_manage_updates_reboot_timeout: 1800
            windows_manage_updates_compile_assemblies: true
            windows_manage_updates_compile_filter: "Cumulative Update|NET"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
