# my_own_role

Роль создаёт текстовый файл с помощью собственного Ansible-модуля
`trashdokidoki.yandex_cloud_elk.my_own_module`.

## Variables

| Variable | Default | Description |
|---|---|---|
| `my_own_module_path` | `/tmp/netology_role.txt` | Путь к файлу |
| `my_own_module_content` | `Hello from my own Ansible collection` | Содержимое файла |

## Example

```yaml
---
- name: Use my own role
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: trashdokidoki.yandex_cloud_elk.my_own_role