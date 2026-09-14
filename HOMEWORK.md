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

<img width="1364" height="138" alt="Снимок экрана 2026-09-14 190608" src="https://github.com/user-attachments/assets/784a5c66-4330-4a71-b0a0-dbdec22fb500" />

## Проверка через playbook

Создан playbook, который использует собственный модуль.

При первом запуске:

`changed=1`

При повторном запуске:

`changed=0`

### Пункт 6 — проверка идемпотентности

<img width="1506" height="422" alt="Снимок экрана 2026-09-14 191023" src="https://github.com/user-attachments/assets/381d0384-3495-4ce5-a230-6cc9215e9a81" />

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

<img width="1022" height="109" alt="Снимок экрана 2026-09-14 193959" src="https://github.com/user-attachments/assets/888a987c-41b1-4c49-9711-87b3112587b8" />

### Пункт 16 — запуск playbook с установленной collection

Playbook успешно использует установленную collection и роль.

При первом запуске:

`changed=1`

При повторном запуске:

`changed=0`

<img width="1491" height="393" alt="Снимок экрана 2026-09-14 194107" src="https://github.com/user-attachments/assets/5e382b38-c454-41d9-bbc4-da07fdd08cb6" />

