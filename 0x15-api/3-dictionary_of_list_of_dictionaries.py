#!/usr/bin/python3
"""
Script that use https://jsonplaceholder.typicode.com/ to return
a todo list progress for a giveen employee
"""

import re
import requests as requests
import sys
import json
url = "https://jsonplaceholder.typicode.com"
"""URL for API"""


if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(url)).json()
    todos_res = requests.get('{}/todos'.format(url)).json()
    users_data = {}
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
