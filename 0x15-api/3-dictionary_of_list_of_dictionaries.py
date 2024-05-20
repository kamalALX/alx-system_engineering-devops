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

    all_users_data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        
        user_tasks = []
        for task in todos:
            if task['userId'] == user_id:
                task_data = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_data)
        
        all_users_data[user_id] = user_tasks

    """ Write the JSON object to a file """
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(all_users_data, json_file)
