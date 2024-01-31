#!/usr/bin/python3
"""A Python script that returns information about an employee

The script takes the empolyee ID as the first argument.
"""
import requests
import sys


emp_id = sys.argv[1]
emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
todo_url = emp_url + "/todos"
try:
    emp_res = requests.get(emp_url)
    if emp_res.status_code == 200:
        emp_name = emp_res.json().get("name")
    else:
        print(f"Request for users failed with the status code:\
              {emp_res.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")

try:
    todo_res = requests.get(todo_url)
    if todo_res.status_code == 200:
        tasks = todo_res.json()
    else:
        print(f"Request for todo failed with the status code:\
              {todo_res.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")

done_tasks = 0
task_title = []

for task in tasks:
    if task.get("completed"):
        done_tasks += 1
        task_title.append(task.get("title"))
print(f"Employee {emp_name} is done with tasks({done_tasks}/{len(tasks)}):")
for title in task_title:
    print(f"\t {title}")
