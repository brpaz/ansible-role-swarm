# Ansible Docker Swarm Role

> A simple [Ansible](https://docs.ansible.com/ansible/latest/index.html) role to set up a single-node Docker Swarm cluster

## Requirements

- Ansible 2.10+
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

| Variable               | Default Value                        | Description                                                 |
| ---------------------- | ------------------------------------ | ----------------------------------------------------------- |
| `swarm_advertise_addr` | `{{ ansible_default_ipv4.address }}` | IP address to advertise for this node                       |
| `swarm_network`        | `swarm_network`                      | The name of the default Swarm overlay network to be created |
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

## 🫶 Support

If you find this project helpful and would like to support its development, there are a few ways you can contribute:

[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23db61a2.svg?&logo=github&logoColor=red&&style=for-the-badge&labelColor=white)](https://github.com/sponsors/brpaz)

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## 📃 License

Distributed under the MIT License.
See [LICENSE](LICENSE.md) file for details.

## 📩 Contact

✉️ **Email** - [oss@brunopaz.dev](oss@brunopaz.dev)

🖇️ **Source code**: [https://github.com/brpaz/ansible-role-swarm](https://github.com/brpaz/ansible-role-swarm)


