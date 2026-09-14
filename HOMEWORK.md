# Домашнее задание к занятию «Создание собственных модулей»

## Репозиторий collection

Репозиторий:

`https://github.com/TrashDokiDoki/my_own_collection`

Collection:

`trashdokidoki.yandex_cloud_elk`

Версия:

`1.0.0`

## Собственный модуль

Создан модуль:

`my_own_module`

Он принимает параметры:

- `path` — путь к файлу;
- `content` — содержимое файла.

Модуль идемпотентный: если файл уже существует и его содержимое совпадает с переданным значением, изменений не происходит.

### Пункт 4 — локальная проверка модуля

При первом запуске:

`changed: true`

При повторном запуске:

`changed: false`

![Пункт 4](screenshots/04-module-local.png)

## Проверка через playbook

Создан playbook, который использует собственный модуль.

При первом запуске:

`changed=1`

При повторном запуске:

`changed=0`

### Пункт 6 — проверка идемпотентности

![Пункт 6](screenshots/06-playbook.png)

## Ansible Collection

Создана collection:

`trashdokidoki.yandex_cloud_elk`

В неё входят:

- `plugins/modules/my_own_module.py`
- `roles/my_own_role`

Роль использует собственный модуль и принимает переменные:

- `my_own_module_path`
- `my_own_module_content`

Collection собрана в архив:

`trashdokidoki-yandex_cloud_elk-1.0.0.tar.gz`

### Пункт 15 — установка collection из архива

Collection успешно установлена локально из `.tar.gz`.

![Пункт 15](screenshots/15-collection-install.png)

### Пункт 16 — запуск playbook с установленной collection

Playbook успешно использует установленную collection и роль.

При первом запуске:

`changed=1`

При повторном запуске:

`changed=0`

![Пункт 16](screenshots/16-collection-playbook.png)
