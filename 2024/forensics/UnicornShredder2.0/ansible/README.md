Ansible playbook for deploying Unicorn Shredder 2.0 to a standalone container/VM. Will install nginx, PHP and required Python modules, and request a certificate via Let's Encrypt. Assumes that the container has TCP ports 80 and 443 open to the internet and that the hostname given in `inventory.cfg` resolves to the container's IP.

Run with:
```
ansible-playbook -i inventory.cfg deploy-container.yml
```
