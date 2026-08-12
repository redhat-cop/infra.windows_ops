windows_manage_locale
=====================

A role to configure Windows locale, language, input methods, and regional settings.

Requirements
------------

* Windows Server 2019, 2022, or 2025
* Ansible >= 2.18
* MUI language pack installed for the target UI language

Role Variables
--------------

* **windows_manage_locale_location**: Geographic location identifier (GeoId). Default is **244** (United States)
* **windows_manage_locale_system**: System locale affecting non-Unicode programs. Default is **en-US**
* **windows_manage_locale_ui**: UI display language. Default is **en-US**
* **windows_manage_locale_user**: User locale for date, time, and number formats. Default is **en-US**
* **windows_manage_locale_input**: Input method profiles as semicolon-separated locale names or hex code pairs. Default is **en-US**
* **windows_manage_locale_welcome_screen_update_always**: Force updating Welcome screen settings even if locale config was not changed. Default is **false**
* **windows_manage_locale_reboot**: Whether to reboot after locale changes. Default is **true**

Dependencies
------------

- NA

Example Playbook
----------------

    - hosts: windows
      tasks:
        - name: Configure locale settings
          ansible.builtin.include_role:
            name: infra.windows_ops.windows_manage_locale
          vars:
            windows_manage_locale_system: "en-US"
            windows_manage_locale_ui: "en-US"
            windows_manage_locale_user: "en-US"
            windows_manage_locale_reboot: true

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Red Hat Ansible Content Team
