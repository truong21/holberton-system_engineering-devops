#!/usr/bin/python3
"""
Script that connects to https://jsonplaceholder.typicode.com/ API to return
information on a employee
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    try:
        employee_id = sys.argv[1]
    except Exception:
        employee_id = ""

    r = requests.get(url)
    total_task = 0
    completed_task = 0
    compl_task_list = []
    res = r.json()
    for task in res:
        if task.get("userId") == int(employee_id):
            total_task += 1
            if task.get("completed") is True:
                completed_task += 1
                compl_task_list.append(task.get("title"))
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    r2 = requests.get(url)
    user_info = r2.json()
    print("Employee {} is done with tasks({}/{}):"
          .format(user_info.get("name"), completed_task, total_task))
    for i in compl_task_list:
        print("\t {}".format(i))
