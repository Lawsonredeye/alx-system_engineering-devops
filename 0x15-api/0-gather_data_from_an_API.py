#!/usr/bin/python3
"""
Learning about REST API and how to get data from an api service
using either requests or urllib
"""

import requests
import sys

if __name__ == "__main__":
    """
    main function which is the first poioint of execution for running this
    script to get the userName, ID, title
    """
    # - Variables to be used
    complete = 0
    total = 0
    args = int(sys.argv[1])
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users")
    todoUrl = requests.get("https://jsonplaceholder.typicode.com/todos")

    userUrl.json()
    for user in userUrl.json():
        if user["id"] == args:
            name = user["name"]

    for todo in todoUrl.json():
        if todo["userId"] == args:
            if todo["completed"] == True:
                complete += 1

    for todo in todoUrl.json():
        if todo["userId"] == args:
            if todo["completed"] == True or todo["completed"] == False:
                total += 1

    print(f"Employee {name} is done with tasks({complete}/{total}):")
    for todo in todoUrl.json():
        if todo["userId"] == args:
                if todo["completed"] == True:
                    print(f"\t{todo['title']}")
