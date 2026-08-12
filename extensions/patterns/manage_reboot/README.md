# Windows Manage Reboot Pattern

## Description

This pattern automates Windows system reboots through Ansible Automation Platform with configurable timeout and user messaging.

## What This Pattern Covers

### Job Templates

- **Reboot System Job Template**: Reboots a Windows system with configurable delays, timeout, and user notification message.

### Surveys

- **Reboot System Survey**: Prompts users to specify:
  - Reboot timeout (how long to wait for the system to come back)
  - Reboot message (notification for logged-in users)

## How to Use

1. **Use Seed Red Hat pattern Job**
    - Execute the "Seed Red Hat pattern" job and select the "Windows" category to load this pattern.

2. **Use the Job Templates**
    - In `Windows Operations / Reboot System` execute the job template. Monitor the job execution and verify the system comes back online.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) for details.
