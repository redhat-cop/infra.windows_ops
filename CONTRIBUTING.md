# Contributing to the Infra Windows Ops Ansible Collection
 
We welcome community contributions to this collection.
This guide provides clear instructions for contributors on how to set up their environment for contributing to the `infra.windows_ops` Ansible Collection.
If you find problems, please open an issue or create a Pull Request (PR) against this collection repository.

## Integration Test Naming Convention

In the CI, the test names should follow the convention of starting with the name of the collection. In the Windows Ops collection, this is followed by test and the name of the role.

For example:
`windows_ops_test_windows_manage_iis`

## Prerequisites

Make sure you have the following installed on your Machine:

1. Python3 and pip3
2. Docker or Podman  
For more information on how containers are used with Ansible, refer to the [Containers section in the Ansible Community Documentation](https://docs.ansible.com/ansible/latest/dev_guide/testing_running_locally.html#containers).  
To allow managing Docker as a non-root user, refer to the [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/).
3. Ansible
   This can be installed by running `pip3 install ansible`

## Environment Setup

To set up your environment for contributing to the Infra Windows Ops Ansible Collection, follow these steps:

> **_NOTE:_** Make sure to replace `<working directory>` with the actual path where you want to clone the repositories and set up your environment. 

1. **Clone The "infra.windows_ops" Ansible Collection**:  
   This repository, includes a variety of Ansible roles to help automate the management of resources on Windows.
   ```shell
   git clone https://github.com/redhat-cop/infra.windows_ops.git <working directory>/ansible_collections/infra/windows_ops
   ```
2. ***Prepare Windows Inventory File***:  
Prepare the Windows Inventory file at `<working directory>/ansible_collections/infra/windows_ops/tests/integration/inventory.winrm`. A template of this file is available in [the Ansible repository](https://github.com/ansible/ansible/blob/devel/test/lib/ansible_test/config/inventory.winrm.template). Populate the file with your appropriate host and credentials information.

## Running tests

To run the tests, change directory into windows_ops directory:
```shell
   cd <working directory>/ansible_collections/infra/windows_ops
```

### Integration tests

Run Ansible Integration tests, using the following command:
```shell
   ansible-test windows-integration --docker
```

To run a specific test, add the test name before the `--docker` flag:
```shell
   ansible-test windows-integration <test name> --docker
```
The <test name> should be replaced with the specific folder name under `<working directory>/ansible_collections/infra/windows_ops/tests/integration/targets/` that you want to test.

### Sanity tests

Run Ansible Sanity tests, using the following command:
```shell
   ansible-test sanity --docker
```

### Lint tests

The project uses `ansible-lint` and `black`.
To execute these tools, run:
```shell
  tox -e linters
```

