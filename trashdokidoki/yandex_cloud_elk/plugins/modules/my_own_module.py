#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a text file with specified content

version_added: "1.0.0"

description:
    - Creates a text file at the path specified by the path parameter.
    - Writes content specified by the content parameter.
    - Does not modify the file if its content is already correct.

options:
    path:
        description:
            - Path to the file.
        required: true
        type: str
    content:
        description:
            - Content that should be written to the file.
        required: true
        type: str

author:
    - TrashDokiDoki
'''

EXAMPLES = r'''
- name: Create test file
  my_own_module:
    path: /tmp/netology.txt
    content: "Hello Netology"
'''

RETURN = r'''
path:
    description: Path to the managed file.
    returned: always
    type: str

content:
    description: Desired file content.
    returned: always
    type: str
'''

import os
import tempfile

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    path = module.params['path']
    content = module.params['content']

    current_content = None

    if os.path.exists(path):
        if not os.path.isfile(path):
            module.fail_json(
                msg='Specified path exists and is not a regular file',
                path=path,
            )

        try:
            with open(path, 'r', encoding='utf-8') as file:
                current_content = file.read()
        except OSError as error:
            module.fail_json(
                msg='Unable to read file: {0}'.format(error),
                path=path,
            )

    changed = current_content != content

    if changed and not module.check_mode:
        directory = os.path.dirname(path) or '.'

        if not os.path.isdir(directory):
            module.fail_json(
                msg='Parent directory does not exist',
                path=path,
            )

        try:
            fd, temp_path = tempfile.mkstemp(dir=directory)

            with os.fdopen(fd, 'w', encoding='utf-8') as temp_file:
                temp_file.write(content)

            module.atomic_move(temp_path, path)

        except OSError as error:
            module.fail_json(
                msg='Unable to write file: {0}'.format(error),
                path=path,
            )

    module.exit_json(
        changed=changed,
        path=path,
        content=content,
    )


def main():
    run_module()


if __name__ == '__main__':
    main()
