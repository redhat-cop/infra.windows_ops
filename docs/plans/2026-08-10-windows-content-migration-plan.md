# Windows Content Migration Plan

**Date:** 2026-08-10
**Author:** Hen Yaish
**Status:** Draft
**Epic:** ACA-2792 - Windows Content Migration
**Related Tasks:** ACA-2568 (Migrate), ACA-2664 (Update Playbooks), ACA-2656 (Validate), ACA-2604 (Document)
**Source Repository:** https://github.com/myllynen/windows-ansible-roles

---

## Executive Summary

This plan covers the migration of **42 upstream Windows Ansible roles** from [`myllynen/windows-ansible-roles`](https://github.com/myllynen/windows-ansible-roles) into the `infra.windows_ops` validated collection, per Epic [ACA-2792](https://redhat.atlassian.net/browse/ACA-2792).

**Key decisions:**
- All roles renamed to `windows_manage_*` convention
- Every role meets **full quality standard**: argument_specs, integration tests, README, changelog, **AAP pattern**
- Overlapping upstream roles (service_management/enablement/recovery, system_update) **merged into existing roles**
- 3 upstream service roles **consolidated** into the existing `windows_manage_service`
- `chocolatey.chocolatey` dependency **replaced** with `ansible.windows` / `microsoft.*` equivalents
- Both DSC and DSC3 roles migrated
- Every role ships with a **full AAP pattern** (setup.yml, playbook, survey, execution environment)
- Work split into **8 category-based batches** (3-7 roles each)
- All 4 Jira tasks (migrate, update playbooks, validate, document) executed **together per role**, not sequentially

**Scope:** 42 upstream roles mapped to 38 new `windows_manage_*` roles + 2 existing role enhancements = 40 units of work. Each role includes a complete AAP pattern for Ansible Automation Platform readiness.

**Out of scope:** New modules (roles only), CIS/STIG changes

---

## Role Mapping: Upstream to infra.windows_ops

Every upstream role is renamed to the `windows_manage_*` convention. All variables within each role are prefixed `windows_manage_<short_name>_`.

### Consolidations (4 upstream roles merged into 2 existing roles)

| Upstream Role | Target | Action |
|---|---|---|
| `service_management` | `windows_manage_service` (existing) | Merge features into existing role |
| `service_enablement` | `windows_manage_service` (existing) | Merge features into existing role |
| `service_recovery` | `windows_manage_service` (existing) | Merge features into existing role |
| `system_update` | `windows_manage_updates` (existing) | Merge features into existing role |

### New Roles (38 upstream roles become 38 new roles)

| Upstream Role | New Role Name |
|---|---|
| `accounts_local` | `windows_manage_accounts` |
| `audit_configuration` | `windows_manage_audit` |
| `boot_configuration` | `windows_manage_boot` |
| `disk_cleanup` | `windows_manage_disk_cleanup` |
| `dns_client` | `windows_manage_dns_client` |
| `dotnet_optimize` | `windows_manage_dotnet` |
| `dsc_settings` | `windows_manage_dsc` |
| `dsc3_settings` | `windows_manage_dsc3` |
| `environment_settings` | `windows_manage_environment` |
| `etc_hosts` | `windows_manage_hosts_file` |
| `files_acl` | `windows_manage_file_acl` |
| `files_copy` | `windows_manage_file_copy` |
| `files_create` | `windows_manage_file_create` |
| `files_fetch` | `windows_manage_file_fetch` |
| `files_get` | `windows_manage_file_get` |
| `files_remove` | `windows_manage_file_remove` |
| `firewall_configuration` | `windows_manage_firewall` |
| `network_configuration` | `windows_manage_network` |
| `packages_chocolatey` | `windows_manage_packages` |
| `performance_tuning` | `windows_manage_performance` |
| `rdp_configuration` | `windows_manage_rdp` |
| `registry_settings` | `windows_manage_registry` |
| `sshd_configuration` | `windows_manage_sshd` |
| `system_description` | `windows_manage_description` |
| `system_hostname` | `windows_manage_hostname` |
| `system_init` | `windows_manage_init` |
| `system_locale` | `windows_manage_locale` |
| `system_reboot` | `windows_manage_reboot` |
| `system_time` | `windows_manage_time` |
| `task_scheduling` | `windows_manage_scheduled_tasks` |
| `user_experience` | `windows_manage_user_experience` |
| `user_settings` | `windows_manage_user_settings` |
| `win_capabilities` | `windows_manage_capabilities` |
| `win_features` | `windows_manage_features` |
| `win_optional_features` | `windows_manage_optional_features` |
| `windows_recovery` | `windows_manage_recovery` |
| `winrm_configuration` | `windows_manage_winrm` |
| `wsl_configuration` | `windows_manage_wsl` |

---

## Role Quality Standard

Every migrated role must meet this standard before it is considered done.

### Required Directory Structure

```
roles/windows_manage_<name>/
├── README.md
├── defaults/main.yml
├── meta/
│   ├── main.yml
│   └── argument_specs.yml
├── tasks/
│   ├── main.yml
│   └── <operation>.yml            # one file per operation (if multi-operation)
├── handlers/main.yml              # only if needed
├── templates/                     # only if needed, no empty dirs
├── files/                         # only if needed, no empty dirs
└── vars/                          # only if version-specific overrides needed
```

### defaults/main.yml

- Every variable prefixed `windows_manage_<name>_`
- Sensible defaults where possible; required params have no default (enforced by argument_specs)
- Organized with comment section headers for complex roles

### meta/main.yml Template

```yaml
galaxy_info:
  author: Red Hat Ansible Content Team
  description: "<One clear sentence describing the role>"
  company: Red Hat, Inc.
  license: GPL-3.0-or-later
  min_ansible_version: "2.18"
  platforms:
    - name: Windows
      versions: ["2019", "2022", "2025"]
  galaxy_tags: [windows, <relevant-tags>]
dependencies: []
```

### meta/argument_specs.yml

- Every parameter has: `description`, `type`, `required` (or `default`), and `choices` where applicable
- Include `version_added` using the next release version
- Use `elements:` for list types, `options:` for dict sub-keys
- Follow `windows_manage_iis` as the gold standard reference

### tasks/main.yml Patterns

**Operation-based dispatch** (for roles with distinct modes like create/delete):
```yaml
- name: "<Role description>"
  ansible.builtin.include_tasks: "{{ windows_manage_<name>_operation }}.yml"
```

**Direct inline** (for single-purpose roles like reboot, hostname):
All tasks directly in `main.yml`.

### README.md Structure

- Role title and one-line description
- Requirements (min Ansible version, required collections)
- Role Variables table (bold name, description, type, default)
- Dependencies
- Example Playbook using FQCNs
- License and Author

### Required AAP Pattern

Every role must include a full AAP pattern for Ansible Automation Platform readiness:

```
extensions/patterns/<pattern_name>/
├── README.md
├── setup.yml                          # AAP controller config (labels, EE, project, job template)
├── playbooks/
│   └── run_<pattern_name>.yml         # Thin wrapper playbook that calls the role
├── template_surveys/
│   └── <pattern_name>.yml             # AAP survey definition (user prompts)
└── exec_env/
    ├── execution-environment.yml      # EE build spec (v3, base image, deps)
    ├── requirements.yml               # Collection requirements for EE
    ├── .gitignore
    └── README.md
```

**setup.yml**: Defines AAP controller objects using `controller_*` variables for the `redhat.controller` collection — labels, execution environment, project, and job template.

**playbooks/run_\<pattern_name\>.yml**: Thin wrapper that calls `include_role` with variables mapped from survey inputs to role variables (e.g., survey `hostname` maps to role var `windows_manage_hostname_name`).

**template_surveys/\<pattern_name\>.yml**: Defines the AAP survey UI — question names, types, variable names, choices, defaults. Survey variables use shortened names; the pattern playbook bridges them to the role's `windows_manage_*` prefixed variables.

**exec_env/**: Builds a container image based on `quay.io/ansible-product-demos/apd-ee-25:latest` with the collection installed from git.

Follow the existing `create_iis` pattern as the gold standard reference.

### Required Integration Test

```
tests/integration/targets/windows_ops_test_windows_manage_<name>/
├── aliases                    # Contains: "windows" and "infra/windows"
├── defaults/main.yml          # Test-specific variable values
└── tasks/main.yml             # Test orchestration
```

Test requirements:
- Verify the role runs successfully (apply + assert expected state)
- Verify idempotency where applicable (second run = `changed: false`)
- Clean up resources created during tests (block/rescue/always pattern)
- Include both success and failure cases where practical

### Required Changelog Fragment

One fragment per batch in `changelogs/fragments/`:
```yaml
minor_changes:
  - "windows_manage_<name> - new role for managing <description>."
```

### Checklist Per Role

- [ ] Variables renamed to `windows_manage_<name>_*` prefix
- [ ] `defaults/main.yml` with all defaults
- [ ] `meta/main.yml` with correct Windows platform and tags
- [ ] `meta/argument_specs.yml` with full parameter specs
- [ ] `tasks/main.yml` with proper dispatch or inline logic
- [ ] All FQCNs used in tasks (`ansible.windows.*`, `community.windows.*`)
- [ ] `no_log: true` on any sensitive parameters (passwords, tokens)
- [ ] `README.md` following standard format
- [ ] Integration test at `windows_ops_test_windows_manage_<name>`
- [ ] AAP pattern at `extensions/patterns/<pattern_name>/`
- [ ] AAP pattern includes: `setup.yml`, playbook, survey, execution environment
- [ ] Survey variables correctly mapped to role variables in pattern playbook
- [ ] Changelog fragment created
- [ ] `ansible-test sanity` passes
- [ ] `ansible-lint` passes

---

## Batches

Work is split into 9 batches (0-8), ordered by dependency and complexity. Each batch is one feature branch and one PR.

### Batch 0: Existing Role Enhancements (Pre-migration)

Merge upstream features into the 2 existing roles and fix quality issues across all existing roles. This resolves overlaps and sets the standard before new role migration begins.

**Role enhancements:**

| Role | Upstream Source | Key Features to Merge |
|---|---|---|
| `windows_manage_service` | `service_management` (14 tasks), `service_enablement`, `service_recovery` | Service discovery via PowerShell, create/remove services, configure recovery options, delayed start, dependency management, `no_log` for service passwords |
| `windows_manage_updates` | `system_update` | Any additional features from upstream not already present |

**Existing role fixes:**
- Add `meta/argument_specs.yml` to `windows_manage_cis` and `windows_manage_stig`
- Fix `meta/main.yml` on IIS/service/updates roles (wrong `EL` platform to `Windows`, wrong `linux` tags)
- Add missing integration tests for `windows_manage_service` and `windows_manage_updates`
- Add missing AAP patterns for `windows_manage_cis` and `windows_manage_stig`

**Estimated: 2 enhancements + 5 fixes, 16-22 hours**

---

### Batch 1: System Configuration (7 roles)

Foundational system-level roles. Many are simple and good for establishing the migration pattern.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_hostname` | `system_hostname` | Simple | `ansible.windows.win_hostname` |
| 2 | `windows_manage_reboot` | `system_reboot` | Simple | `ansible.windows.win_reboot` |
| 3 | `windows_manage_description` | `system_description` | Simple | `ansible.windows.win_regedit` |
| 4 | `windows_manage_locale` | `system_locale` | Simple | `community.windows.win_region` |
| 5 | `windows_manage_time` | `system_time` | Simple | `community.windows.win_timezone`, `ansible.windows.win_service` |
| 6 | `windows_manage_init` | `system_init` | Moderate | Multiple (initial system setup orchestrator) |
| 7 | `windows_manage_recovery` | `windows_recovery` | Simple | `ansible.windows.win_command` |

**Estimated: 22-30 hours** (includes AAP patterns for all 7 roles)

---

### Batch 2: Network and Remote Access (5 roles)

Closely related roles for network stack and remote connectivity.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_network` | `network_configuration` | Moderate | `community.windows.win_net_adapter_feature`, `ansible.windows.win_route` |
| 2 | `windows_manage_dns_client` | `dns_client` | Simple | `ansible.windows.win_dns_client` |
| 3 | `windows_manage_hosts_file` | `etc_hosts` | Simple | `community.windows.win_hosts` |
| 4 | `windows_manage_rdp` | `rdp_configuration` | Moderate | `ansible.windows.win_regedit`, `community.windows.win_firewall_rule` |
| 5 | `windows_manage_winrm` | `winrm_configuration` | Complex | `ansible.windows.win_powershell`, `ansible.windows.win_service` |

**Estimated: 20-28 hours** (includes AAP patterns for all 5 roles)

---

### Batch 3: Security and Audit (3 roles)

Security hardening and audit configuration.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_firewall` | `firewall_configuration` | Moderate | `ansible.windows.win_firewall`, `community.windows.win_firewall_rule` |
| 2 | `windows_manage_audit` | `audit_configuration` | Moderate | `ansible.windows.win_audit_policy_system`, `ansible.windows.win_audit_rule` |
| 3 | `windows_manage_sshd` | `sshd_configuration` | Complex | `ansible.windows.win_service`, `ansible.windows.win_powershell` |

**Estimated: 16-22 hours** (includes AAP patterns for all 3 roles)

---

### Batch 4: Accounts and User Experience (3 roles)

User and account management.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_accounts` | `accounts_local` | Complex | `ansible.windows.win_user`, `ansible.windows.win_group`, `ansible.windows.win_group_membership` |
| 2 | `windows_manage_user_experience` | `user_experience` | Moderate | `ansible.windows.win_regedit` |
| 3 | `windows_manage_user_settings` | `user_settings` | Moderate | `ansible.windows.win_regedit` |

**Estimated: 16-22 hours** (includes AAP patterns for all 3 roles)

---

### Batch 5: Files and Registry (7 roles)

File operations and registry management.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_file_acl` | `files_acl` | Moderate | `ansible.windows.win_acl` |
| 2 | `windows_manage_file_copy` | `files_copy` | Moderate | `ansible.windows.win_copy` |
| 3 | `windows_manage_file_create` | `files_create` | Moderate | `ansible.windows.win_file`, `ansible.windows.win_template` |
| 4 | `windows_manage_file_fetch` | `files_fetch` | Simple | `ansible.builtin.fetch` |
| 5 | `windows_manage_file_get` | `files_get` | Simple | `ansible.windows.win_stat`, `ansible.windows.win_find` |
| 6 | `windows_manage_file_remove` | `files_remove` | Simple | `ansible.windows.win_file` |
| 7 | `windows_manage_registry` | `registry_settings` | Moderate | `ansible.windows.win_regedit` |

**Estimated: 25-33 hours** (includes AAP patterns for all 7 roles)

---

### Batch 6: Packages and Features (5 roles)

Package and Windows feature management. Includes the `packages_chocolatey` role that needs dependency replacement.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_features` | `win_features` | Moderate | `ansible.windows.win_feature` |
| 2 | `windows_manage_capabilities` | `win_capabilities` | Moderate | `ansible.windows.win_powershell` |
| 3 | `windows_manage_optional_features` | `win_optional_features` | Moderate | `ansible.windows.win_optional_feature` |
| 4 | `windows_manage_packages` | `packages_chocolatey` | Complex | **Needs research** — replace `chocolatey.chocolatey` with `ansible.windows.win_package` or equivalent |
| 5 | `windows_manage_dotnet` | `dotnet_optimize` | Simple | `ansible.windows.win_command` |

**Estimated: 24-30 hours** (includes dependency research for packages and AAP patterns for all 5 roles)

---

### Batch 7: Maintenance and Configuration (7 roles)

System maintenance, DSC, and remaining configuration roles.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_boot` | `boot_configuration` | Simple | `ansible.windows.win_command` |
| 2 | `windows_manage_disk_cleanup` | `disk_cleanup` | Simple | `ansible.windows.win_powershell` |
| 3 | `windows_manage_performance` | `performance_tuning` | Moderate | `ansible.windows.win_regedit`, `ansible.windows.win_powershell` |
| 4 | `windows_manage_scheduled_tasks` | `task_scheduling` | Complex | `community.windows.win_scheduled_task` |
| 5 | `windows_manage_environment` | `environment_settings` | Simple | `ansible.windows.win_environment` |
| 6 | `windows_manage_dsc` | `dsc_settings` | Complex | `ansible.windows.win_dsc`, `ansible.windows.win_powershell` |
| 7 | `windows_manage_wsl` | `wsl_configuration` | Moderate | `ansible.windows.win_powershell` |

**Estimated: 28-36 hours** (includes AAP patterns for all 7 roles)

---

### Batch 8: DSC3 (1 role)

Separated because DSC3 is the newest framework and may need additional research.

| # | New Role | Upstream | Complexity | Key Modules |
|---|---|---|---|---|
| 1 | `windows_manage_dsc3` | `dsc3_settings` | Complex | `ansible.windows.win_powershell` |

**Estimated: 6-8 hours** (includes AAP pattern)

---

### Batch Summary

| Batch | Category | Roles | Estimated Hours |
|---|---|---|---|
| 0 | Existing Role Enhancements | 2 + 5 fixes | 16-22 |
| 1 | System Configuration | 7 | 22-30 |
| 2 | Network and Remote Access | 5 | 20-28 |
| 3 | Security and Audit | 3 | 16-22 |
| 4 | Accounts and User Experience | 3 | 16-22 |
| 5 | Files and Registry | 7 | 25-33 |
| 6 | Packages and Features | 5 | 24-30 |
| 7 | Maintenance and Configuration | 7 | 28-36 |
| 8 | DSC3 | 1 | 6-8 |
| | **Total** | **40 units** | **~173-231 hours** |

All estimates include AAP pattern creation (setup.yml, playbook, survey, execution environment) for every role.

---

## Workflow

### Per Role Pipeline

All 4 Jira tasks are executed together per role, not sequentially:

```
For each role in batch:
  1. MIGRATE    - Copy upstream tasks, rename variables, restructure to standard
  2. UPDATE     - Ensure FQCNs, fix module calls, replace disallowed dependencies
  3. VALIDATE   - Create argument_specs, write integration test, run sanity + lint
  4. AAP READY  - Create pattern (setup.yml, playbook, survey, execution environment)
  5. DOCUMENT   - Write README, create changelog fragment
```

### Per Batch Workflow

```
1. Create feature branch: feature/batch-N-<category>
2. For each role in the batch:
   a. Migrate + Update + Validate + AAP Ready + Document (the 5-step pipeline above)
   b. Run ansible-test sanity, ansible-lint, yamllint
   c. Verify AAP pattern structure (setup.yml, playbook, survey, exec_env)
3. Run full batch validation (all roles and patterns in batch together)
4. Create PR with changelog fragments
5. Review + merge
```

---

## Dependencies Between Batches

```
Batch 0 (Existing Role Fixes) ---- MUST go first
     |
     v
Batches 1-8 ---- Can run in ANY order (no cross-dependencies)
```

Batch 0 is the only hard prerequisite. It establishes the enhanced `windows_manage_service` and `windows_manage_updates` roles and fixes existing quality issues, setting the standard for all subsequent work.

Batches 1-8 are independent. Recommended order is as listed (simple to complex) to build migration muscle on easier roles first, but can be reordered based on priority.

---

## Special Considerations

### windows_manage_packages (Batch 6) - Dependency Research

The upstream `packages_chocolatey` uses the `chocolatey.chocolatey` collection which is not allowed in official Red Hat repos. Before migrating this role:

1. Research `ansible.windows.win_package` capabilities (MSI, MSIX, EXE installers)
2. Check if `microsoft.*` collections have a package management module
3. Determine if Chocolatey can be driven via `ansible.windows.win_command` / `win_powershell` without the dedicated collection
4. Design the replacement approach, then migrate

### windows_manage_init (Batch 1) - Orchestrator Role

The upstream `system_init` role calls other roles as an initial system setup orchestrator. After migration, its `include_role` calls must reference the new `infra.windows_ops.windows_manage_*` FQCNs. If roles it depends on are not yet migrated (they are in later batches), use conditional includes or migrate this role last within Batch 1.

### Version Compatibility

- Collection `meta/runtime.yml` requires Ansible `>=2.18.0`
- All migrated roles must set `min_ansible_version: "2.18"` in their `meta/main.yml`
- Upstream requires `ansible.windows >= 3.6.1` and `community.windows >= 3.2.0`
- **Update `galaxy.yml`** dependency versions to match upstream minimums

---

## Jira Ticket Strategy

The 4 existing tasks under ACA-2792 map to cross-cutting concerns, not per-role work:

- Keep the 4 tasks as-is (they represent overall process phases)
- Track per-batch progress via PR links on the epic
- Update each task status as all batches complete that phase

---

## Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| Integration tests cannot run without Windows hosts | Tests written but unverified | Document test requirements, verify in CI when Windows inventory is available |
| `packages_chocolatey` replacement is non-trivial | One role delayed | Research first, can defer to separate PR if needed |
| `system_init` orchestrator calls roles not yet migrated | Broken role if batch order changes | Migrate `system_init` last within Batch 1, or use conditional includes |
| Variable renaming breaks upstream playbooks | Users of upstream repo affected | Out of scope, this is a new collection not an in-place rename |
| `galaxy.yml` dependency version bump | May break users on older ansible.windows | Document in changelog as minor_change |

---

## Migration Progress Tracker

### Batch 1: System Configuration

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_hostname` | [#63](https://github.com/redhat-cop/infra.windows_ops/pull/63) | [x] | [x] |
| `windows_manage_reboot` | [#64](https://github.com/redhat-cop/infra.windows_ops/pull/64) | [x] | [x] |
| `windows_manage_description` | [#65](https://github.com/redhat-cop/infra.windows_ops/pull/65) | [x] | [x] |
| `windows_manage_locale` | [#66](https://github.com/redhat-cop/infra.windows_ops/pull/66) | [x] | [x] |
| `windows_manage_time` | [#67](https://github.com/redhat-cop/infra.windows_ops/pull/67) | [x] | [x] |
| `windows_manage_init` | [#68](https://github.com/redhat-cop/infra.windows_ops/pull/68) | [x] | [x] |
| `windows_manage_recovery` | [#69](https://github.com/redhat-cop/infra.windows_ops/pull/69) | [x] | [x] |

### Batch 0: Existing Role Enhancements

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_service` (merge 3 upstream roles) | | [ ] | [ ] |
| `windows_manage_updates` (merge upstream features) | | [ ] | [ ] |

### Batch 2: Network and Remote Access

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_network` | [#71](https://github.com/redhat-cop/infra.windows_ops/pull/71) | [x] | [ ] |
| `windows_manage_dns_client` | [#70](https://github.com/redhat-cop/infra.windows_ops/pull/70) | [x] | [ ] |
| `windows_manage_hosts_file` | [#72](https://github.com/redhat-cop/infra.windows_ops/pull/72) | [x] | [x] |
| `windows_manage_rdp` | [#73](https://github.com/redhat-cop/infra.windows_ops/pull/73) | [x] | [x] |
| `windows_manage_winrm` | [#74](https://github.com/redhat-cop/infra.windows_ops/pull/74) | [x] | [x] |

### Batch 3: Security and Audit

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_firewall` | | [ ] | [ ] |
| `windows_manage_audit` | | [ ] | [ ] |
| `windows_manage_sshd` | | [ ] | [ ] |

### Batch 4: Accounts and User Experience

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_accounts` | | [ ] | [ ] |
| `windows_manage_user_experience` | | [ ] | [ ] |
| `windows_manage_user_settings` | | [ ] | [ ] |

### Batch 5: Files and Registry

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_file_acl` | | [ ] | [ ] |
| `windows_manage_file_copy` | | [ ] | [ ] |
| `windows_manage_file_create` | | [ ] | [ ] |
| `windows_manage_file_fetch` | | [ ] | [ ] |
| `windows_manage_file_get` | | [ ] | [ ] |
| `windows_manage_file_remove` | | [ ] | [ ] |
| `windows_manage_registry` | | [ ] | [ ] |

### Batch 6: Packages and Features

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_features` | | [ ] | [ ] |
| `windows_manage_capabilities` | | [ ] | [ ] |
| `windows_manage_optional_features` | | [ ] | [ ] |
| `windows_manage_packages` | | [ ] | [ ] |
| `windows_manage_dotnet` | | [ ] | [ ] |

### Batch 7: Maintenance and Configuration

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_boot` | | [ ] | [ ] |
| `windows_manage_disk_cleanup` | | [ ] | [ ] |
| `windows_manage_performance` | | [ ] | [ ] |
| `windows_manage_scheduled_tasks` | | [ ] | [ ] |
| `windows_manage_environment` | | [ ] | [ ] |
| `windows_manage_dsc` | | [ ] | [ ] |
| `windows_manage_wsl` | | [ ] | [ ] |

### Batch 8: DSC3

| Role | PR | In Review | Done |
|---|---|---|---|
| `windows_manage_dsc3` | | [ ] | [ ] |
