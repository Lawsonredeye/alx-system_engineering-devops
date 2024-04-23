#!/usr/bin/python3
"""
Python script that uses a fake API data to extract data for use
"""

import json
import requests


def main():
    """
    main function which is the first poioint of execution for running this
    script to get the userName, ID, title
    """
    # - Variables to be used
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users")
    todoUrl = requests.get("https://jsonplaceholder.typicode.com/todos")

    # empty dict for dumping into json file
    new_dict = {}
    # use 2 loops to get both username, title and id
    for user in userUrl.json():
        new_list = []
        for todo in todoUrl.json():
            # create empty dict for new key-values
            empty = {}
            if todo["userId"] == user["id"]:
                empty["username"] = user["username"]
                empty["title"] = todo["title"]
                empty["completed"] = todo["completed"]
                new_list.append(empty)
            # store the non-empty list into new_dict
            new_dict[user["id"]] = new_list

    filename = "todo_all_employees.json"

    with open(filename, "w") as f:
        json.dump(new_dict, f)


if __name__ == "__main__":
    main()
