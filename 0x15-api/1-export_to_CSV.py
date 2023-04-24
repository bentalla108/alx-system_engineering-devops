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
            usr_name = usr_req.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, all_todos))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            usr_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
