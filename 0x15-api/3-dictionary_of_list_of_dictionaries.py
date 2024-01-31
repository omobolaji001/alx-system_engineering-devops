#!/usr/bin/python3
"""A Python script that returns information about an employee

The script takes the empolyee ID as the first argument.
"""
import json
import requests


if __name__ == '__main__':
    emp_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    try:
        emp_res = requests.get(emp_url)
        if emp_res.status_code == 200:
            employees = emp_res.json()
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

    with open('todo_all_employees.json', 'w') as file:
        dict_t = {}
        for emp in employees:
            emp_id = emp.get("id")
            username = emp.get("username")
            data = []
            for task in tasks:
                if task.get("userId") == emp_id:
                    dic = {"username": username,
                           "title": task.get("title"),
                           "completed": task.get("completed")}
                data.append(dic)
            dict_t[emp_id] = data
        json.dump(dict_t, file)
