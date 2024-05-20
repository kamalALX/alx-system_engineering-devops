#!/usr/bin/python3
""" Python script that consume a REST api"""
import requests
import sys


employer_id = int(sys.argv[1])

todos_url = 'https://jsonplaceholder.typicode.com/todos'
users_url = 'https://jsonplaceholder.typicode.com/users'

todos_response = requests.get(todos_url)
todos = todos_response.json()

all_tasks = 0
done = 0

for task in todos:
    if task['userId'] == employer_id:
        if task['completed']:
            done += 1
        all_tasks += 1

users_response = requests.get(users_url)
users = users_response.json()

name = None
for user in users:
    if user['id'] == employer_id:
        name = user['name']
        break

print('Employee {} is done with tasks({}/{}):'.format(name, done, all_tasks))

for task in todos:
    if task['userId'] == employer_id and task['completed']:
        print("\t {}".format(task['title']))
