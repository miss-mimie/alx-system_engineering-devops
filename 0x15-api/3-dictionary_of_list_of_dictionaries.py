#!/usr/bin/python3

"""
This module provides a function to export all tasks to a JSON file.
"""

import prototype


if __name__ == "__main__":
    # get user info and todos once so we can minimize the number of requests.
    # this helps to achieve more speed since everything will be done locally
    # after the data has been retrieved.
    users = prototype.get_users()
    todos = prototype.get_todos()
    prototype.export_all_to_json(users=users, tasks=todos)
