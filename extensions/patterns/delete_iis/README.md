# Windows Delete IIS Pattern

## Description

This pattern is designed to facilitate the automated deletion of a web server using Ansible. It provides a streamlined way to seed the necessary resources to delete the web server, storage location, firewall ports if needed.

## What This Pattern Covers

This pattern includes the following key components:

### Project Templates

- **Delete IIS Project Template**: Defined within the `setup.yaml` playbook, this template helps organize and manage all necessary components for the delete iis pattern. It ensures that relevant files, roles, and configurations are logically arranged, making it easier to maintain and execute automation tasks.

### Playbooks

- **Playbooks**: Located in the playbooks directory, these scripts are specifically designed to execute the windows_manage_iis role with the appropriate variables.

### Surveys

- **Delete IIS Surveys**: Defined within the `delete_iis.yaml` file, delete iis surveys provide a dynamic interaction mechanism for users to specify parameters for the deletion jobs. These surveys enable users to:
  - Choose the name of the web server
  - Select all to remove the IIS Service as well as the Web Server definition

## Resources Created by This Pattern

1. **Project Templates**
    - Ensure that all relevant files, roles, and configurations are logically arranged, facilitating easier maintenance and execution of automation tasks.

2. **Job Templates**
    - Outline the necessary parameters and configurations to perform deletion of iis web server using the provided playbooks.

## How to Use

1. **Use Seed Red Hat pattern Job**
    - Ensure the custom EE is correctly built and available in your Ansible Automation Platform. Execute the "Seed Red Hat pattern" job within the Ansible Automation Platform, and select the "Windows" category to load this pattern.

2. **Use the Job Templates**
    - In the `Windows Operations / Delete IIS` execute the required job templates to delete IIS web server. Monitor the job execution and verify that the web server is correctly stopped and removed.

## Contribution

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text. This project is licensed under the MIT License. See the [LICENSE](https://github.com/redhat-cop/infra.windows_ops/blob/main/LICENSE) file for details.

---

For any issues or questions, please open an issue on the [GitHub issue tracker](https://github.com/redhat-cop/infra.windows_ops/issues).

