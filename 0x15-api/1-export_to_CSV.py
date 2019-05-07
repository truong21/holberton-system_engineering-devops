#!/usr/bin/python3
"""
Script to export json to csv
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

    filename = userId + ".csv"
    with open(filename, mode="w") as csv_file:
        fieldnames = ["user_id", "username", "status", "title"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for todo in todo_json:
            writer.writerow({"user_id": userId,
                             "username": user_name,
                             "status": todo.get("completed"),
                             "title": todo.get("title")})
