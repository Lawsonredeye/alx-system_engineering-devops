#!/usr/bin/python3
"""
Python script that uses a fake API data to extract data for use
"""

import json
import requests
import sys


def main():
    """
    main function which is the first poioint of execution for running this
    script to get the userName, ID, title
    """
    # - Variables to be used
    complete = 0
    total = 0
    username = ''
    args = int(sys.argv[1])
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users")
    todoUrl = requests.get("https://jsonplaceholder.typicode.com/todos")

    userUrl.json()
    for user in userUrl.json():
        if user["id"] == args:
            name = user["name"]
            username = user["username"]

    for todo in todoUrl.json():
        if todo["userId"] == args:
            if todo["completed"] is True:
                complete += 1

    for todo in todoUrl.json():
        if todo["userId"] == args:
            if todo["completed"] is True or todo["completed"] is False:
                total += 1

    my_list = []
    count = 0
    for todos in todoUrl.json():
        mydict = {}
        if todos["userId"] == args:
            mydict["task"] = todos["title"]
            mydict["completed"] = todos["completed"]
            mydict["username"] = username
            my_list.append(mydict)
    mydict[args] = my_list

    filename = f"{args}.json"
    with open(filename, "w") as f:
        json.dump(mydict, f, indent=4)


if __name__ == "__main__":
    main()
