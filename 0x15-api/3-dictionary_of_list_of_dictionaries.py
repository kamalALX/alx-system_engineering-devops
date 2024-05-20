#!/usr/bin/python3
""" Python script that consume a REST api"""


if __name__ == "__main__":
    import requests
    import sys
    import json


    """ Define the API URLs """
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    """ Make a GET request to fetch todos """
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    """ Make a GET request to fetch user information """
    users_response = requests.get(users_url)
    users = users_response.json()

    """ Find the user with the given employer_id """
    names = []
    ids = []
    for user in users:
            names.append(user['username'])
            ids.append(user['id'])

    user_tasks = []
    task_data = {}
    users_data = {}
    i = 1
    for i in range(len(names)):
        for task in todos:
            task_data = {
                    "username": names[i],
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    }
            user_tasks.append(task_data)
            users_data = {ids[i]: user_tasks}
        i = i + 1

    """ Write the JSON object to a file """
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(users_data, json_file)
