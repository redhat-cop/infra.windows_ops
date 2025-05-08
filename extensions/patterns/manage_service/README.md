# Windows Service Pattern

## Description

This pattern is designed to facilitate the automated management of services using Ansible. It provides a streamlined way to seed the necessary resources to manage a service, Service state and start mode.

## What This Pattern Covers

This pattern includes the following key components:

### Project Templates

- **Manage Service Project Template**: Defined within the `setup.yaml` playbook, this template helps organize and manage all necessary components for the manage service pattern. It ensures that relevant files, roles, and configurations are logically arranged, making it easier to maintain and execute automation tasks.

### Playbooks

- **Playbooks**: Located in the playbooks directory, these scripts are specifically designed to execute the `windows_manage_service` role with the appropriate variables.

### Surveys

- **Manage Service Surveys**: Defined within the `manage_service.yaml` file, manage service surveys provide a dynamic interaction mechanism for users to specify parameters for the creation jobs. These surveys enable users to:
  - Choose the name of the service
  - Choose the state of the service
  - Optional specify the start mode of the service

## Resources Created by This Pattern

1. **Project Templates**
    - Ensure that all relevant files, roles, and configurations are logically arranged, facilitating easier maintenance and execution of automation tasks.

2. **Job Templates**
    - Outline the necessary parameters and configurations to perform management of services using the provided playbooks.

## How to Use

1. **Use Seed Red Hat pattern Job**
    - Ensure the custom EE is correctly built and available in your Ansible Automation Platform. Execute the "Seed Red Hat pattern" job within the Ansible Automation Platform, and select the "Windows" category to load this pattern.

2. **Use the Job Templates**
    - In the `Windows Operations / Manage Service` execute the required job templates to manage services. Monitor the job execution and verify that the service is in the correct state.

## Contribution

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text. This project is licensed under the MIT License. See the [LICENSE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) file for details.

---

For any issues or questions, please open an issue on the [GitHub issue tracker](https://github.com/redhat-cop/infra.windows_ops/issues).

