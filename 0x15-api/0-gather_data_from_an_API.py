#!/usr/bin/python3
"""
Script that use https://jsonplaceholder.typicode.com/ to return
a todo list progress for a giveen employee
"""

import re
import requests as r
import sys

url = "https://jsonplaceholder.typicode.com"
"""URL for API"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            usr_req = r.get('{}/users/{}'.format(url, id)).json()
            all_todos = r.get('{}/todos'.format(url)).json()
            usr_name = usr_req.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, all_todos))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    usr_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
