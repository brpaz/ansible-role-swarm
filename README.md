# Ansible Docker Swarm Role

> A simple Ansible role to set up a single-node Docker Swarm cluster

## Requirements

- Ansible 2.10+
- Target machines with SSH access
- Docker

## Installation

### Using Ansible Galaxy

You can install this role directly from Ansible Galaxy:

```bash
ansible-galaxy install brpaz.swarm
```

### Using requirements.yml

For version-controlled, repeatable role installations, add to your `requirements.yml`:

```yaml
---
roles:
  - name: brpaz.swarm
    version: v1.0.0  # Specify the version you want

collections:
  - name: community.docker
```

Then install with:

```bash
ansible-galaxy install -r requirements.yml
```

### Manual Installation

Alternatively, you can clone the repository directly:

```bash
# Create a roles directory if it doesn't exist
mkdir -p ~/.ansible/roles
# Clone the repository
git clone https://github.com/brpaz/ansible-role-swarm.git ~/.ansible/roles/brpaz.swarm
```
## Testing

### Molecule Testing

Run the Molecule tests:

```bash
task test
```

## Role Variables

This role includes the following variables for configuration:

| Variable               | Default Value                        | Description                           |
| ---------------------- | ------------------------------------ | ------------------------------------- |
| `swarm_advertise_addr` | `{{ ansible_default_ipv4.address }}` | IP address to advertise for this node |

## Dependencies

- community.docker collection

## Example Playbook

This example sets up a single-node Docker Swarm cluster:

```yaml
---
- name: Setup Single-Node Docker Swarm Cluster
  hosts: swarm_host
  become: true

  roles:
    - role: brpaz.swarm
```

## Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is MIT Licensed [LICENSE](LICENSE)

## Author Information

Bruno Paz
