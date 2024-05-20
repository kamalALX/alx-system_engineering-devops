#!/usr/bin/python3
""" Python script that consume a REST api"""
import requests
import sys


""" Get employer_id from command line arguments """
employer_id = int(sys.argv[1])

""" Define the API URLs """
todos_url = 'https://jsonplaceholder.typicode.com/todos'
users_url = 'https://jsonplaceholder.typicode.com/users'

""" Make a GET request to fetch todos """
todos_response = requests.get(todos_url)
todos = todos_response.json()

""" Initialize task counters """
all_tasks = 0
done = 0

""" Iterate through the tasks and count """
for task in todos:
    if task['userId'] == employer_id:
        if task['completed']:
            done += 1
        all_tasks += 1

""" Make a GET request to fetch user information """
users_response = requests.get(users_url)
users = users_response.json()

""" Find the user with the given employer_id """
name = None
for user in users:
    if user['id'] == employer_id:
        name = user['name']
        break

""" Print the result """
print('Employee {} is done with tasks({}/{}):'.format(name, done, all_tasks))

""" Print the titles of the completed tasks """
for task in todos:
    if task['userId'] == employer_id and task['completed']:
        print("\t {}".format(task['title']))
