#!/usr/bin/python3
""" Python script that consume a REST api"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    """ Get employer_id from command line arguments """
    employer_id = int(sys.argv[1])

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
    name = None
    for user in users:
        if user['id'] == employer_id:
            name = user['username']
            break

    user_tasks = []
    task_data = {}
    for task in todos:
        if task['userId'] == employer_id:
            task_data = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": name
        }
            user_tasks.append(task_data)

    """ Create the JSON object """
    user_data = {str(employer_id): user_tasks}

    """ Write the JSON object to a file """
    filename = "{}.json".format(employer_id)
    with open(filename, 'w') as json_file:
        json.dump(user_data, json_file)
