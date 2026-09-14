# trashdokidoki.yandex_cloud_elk

Учебная Ansible Collection, созданная в рамках домашнего задания Netology
«Создание собственных модулей».

## Состав collection

Collection содержит:

- модуль `my_own_module`;
- роль `my_own_role`.

## Модуль my_own_module

Модуль создаёт текстовый файл.

Параметры:

- `path` — путь к создаваемому файлу;
- `content` — содержимое файла.

Модуль является идемпотентным: если файл уже существует и его содержимое
соответствует переданному параметру `content`, изменений не производится.

Пример:

```yaml
- name: Create text file
  trashdokidoki.yandex_cloud_elk.my_own_module:
    path: /tmp/example.txt
    content: "Hello Netology"
Роль my_own_role

Роль использует my_own_module.

Переменные по умолчанию:

my_own_module_path: "/tmp/netology_role.txt"
my_own_module_content: "Hello from my own Ansible collection"

Пример использования:

---
- name: Use my own role
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: trashdokidoki.yandex_cloud_elk.my_own_role