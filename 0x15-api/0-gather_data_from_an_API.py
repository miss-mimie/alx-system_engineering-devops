#!/usr/bin/python3

"""
Script takes an employee ID and returns the information about his/her
completed TODO list progress. 
"""

import prototype
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user = prototype.get_name(sys.argv[1])
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = prototype.get_todos(sys.argv[1])
    completed_tasks = prototype.get_completed_tasks(todos)
    prototype.print_completed_tasks(user, len(todos), completed_tasks)
