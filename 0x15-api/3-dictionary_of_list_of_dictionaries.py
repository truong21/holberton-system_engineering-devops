#!/usr/bin/python3
"""
Script to export data to json
"""
import csv
import requests
import json


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    filename = "todo_all_employees.json"
    final_dict = {}

    resp_allusers = requests.get(base_url + "/users")
    allusers_json = resp_allusers.json()
    for user in allusers_json:
        userId = str(user.get("id"))

        user_get = "/users?id=" + userId
        todo_get = "/todos?userId=" + userId
        resp_user = requests.get(base_url + user_get)
        resp_todo = requests.get(base_url + todo_get)
        user_json = resp_user.json()
        todo_json = resp_todo.json()

        for user in user_json:
            user_name = user.get("username")

        task_list = []
        for todo in todo_json:
            todo_dict = {}
            todo_dict["task"] = todo.get("title")
            todo_dict["completed"] = todo.get("completed")
            todo_dict["username"] = user_name
            task_list.append(todo_dict)

        final_dict[userId] = task_list

    with open(filename, "w") as fp:
        json.dump(final_dict, fp)
