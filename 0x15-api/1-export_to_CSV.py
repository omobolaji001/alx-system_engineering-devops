#!/usr/bin/python3
"""A Python script that returns information about an employee

The script takes the empolyee ID as the first argument.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    emp_id = sys.argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_url = emp_url + "/todos"
    try:
        emp_res = requests.get(emp_url)
        if emp_res.status_code == 200:
            emp_username = emp_res.json().get("username")
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

    with open(f'{emp_id}.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            data = [emp_id, emp_username, task.get("completed"),
                    task.get("title")]
            writer.writerow(data)
