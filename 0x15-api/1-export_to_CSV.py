#!/usr/bin/python3

"""
This module provides a function to export user tasks to a CSV file.
"""

import prototype
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user_id = sys.argv[1]
    user = prototype.get_username(user_id)
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = prototype.get_todos(user_id)
    prototype.export_to_csv(user_id=user_id, username=user, tasks=todos)
