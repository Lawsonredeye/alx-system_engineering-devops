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

    innerlist = []
    for user in userUrl.json():
        innerlist.append(user["userId"])
    print(innerlist)
        

if __name__ == "__main__":
    main()