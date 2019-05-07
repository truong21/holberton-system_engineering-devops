#!/usr/bin/python3
"""
Script to export data to json
"""
import csv
import requests
import sys
import json


if __name__ == "__main__":
    userId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_get = "/users?id=" + userId
    todo_get = "/todos?userId=" + userId
    resp_user = requests.get(base_url + user_get)
    resp_todo = requests.get(base_url + todo_get)
    user_json = resp_user.json()
    todo_json = resp_todo.json()
    done_tasks = 0
    total_tasks = 0

    for user in user_json:
        user_name = user.get("username")

    filename = userId + ".json"

    task_list = []
    for todo in todo_json:
        todo_dict = {}
        todo_dict["task"] = todo.get("title")
        todo_dict["completed"] = todo.get("completed")
        todo_dict["username"] = user_name
        task_list.append(todo_dict)

    final_dict = {userId: task_list}
    with open(filename, "w") as fp:
        json.dump(final_dict, fp)
