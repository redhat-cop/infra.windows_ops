# Windows Manage Hostname Pattern

## Description

This pattern automates the configuration of Windows system hostnames through Ansible Automation Platform. It validates the hostname against DNS naming rules and optionally reboots the system for the change to take effect.

## What This Pattern Covers

### Job Templates

- **Manage Hostname Job Template**: Defined within the `setup.yml` playbook, this template configures the Windows system hostname with validation and optional reboot.

### Playbooks

- **Playbooks**: Located in the playbooks directory, these scripts execute the `windows_manage_hostname` role with the appropriate variables.

### Surveys

- **Manage Hostname Survey**: Defined within the `manage_hostname.yml` file, the survey prompts users to specify:
  - The hostname to configure (short name, not FQDN, max 63 characters)
  - Whether to reboot after the change

## How to Use

1. **Use Seed Red Hat pattern Job**
    - Ensure the custom EE is correctly built and available in your Ansible Automation Platform. Execute the "Seed Red Hat pattern" job within the Ansible Automation Platform, and select the "Windows" category to load this pattern.

2. **Use the Job Templates**
    - In the `Windows Operations / Manage Hostname` execute the required job template to configure the system hostname. Monitor the job execution and verify that the hostname is correctly changed.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) for details.
