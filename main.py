
"""Main module - command-line interface for the Todo App."""

import argparse

from src.todo_list import TodoList


def main() -> None:
    """Parse command-line arguments and execute the requested action."""

    parser = argparse.ArgumentParser(
        description="A simple OOP To-Do App."
    )
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    # Add command
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task",
    )
    add_parser.add_argument(
        "title",
        type=str,
        help="Title of the task",
    )

    # List command
    subparsers.add_parser(
        "list",
        help="List all tasks",
    )

    # Done command
    done_parser = subparsers.add_parser(
        "done",
        help="Mark a task as done",
    )
    done_parser.add_argument(
        "id",
        type=int,
        help="ID of the task",
    )

    # Delete command
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task",
    )
    delete_parser.add_argument(
        "id",
        type=int,
        help="ID of the task",
    )

    # Edit command
    edit_parser = subparsers.add_parser(
        "edit",
        help="Edit a task's title or status",
    )
    edit_parser.add_argument(
        "id",
        type=int,
        help="ID of the task",
    )
    edit_parser.add_argument(
        "--title",
        type=str,
        help="New title for the task",
    )
    edit_parser.add_argument(
        "--status",
        choices=["todo", "done"],
        help="New status of the task",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    # Edit requires at least one field to update
    if (
        args.command == "edit"
        and args.title is None
        and args.status is None
    ):
        edit_parser.print_help()
        return

    todo = TodoList()

    if args.command == "add":
        task = todo.add(args.title)
        print(f"Task added successfully! (ID: {task.id})")

    elif args.command == "list":
        tasks = todo.list_tasks()

        if not tasks:
            print("Your to-do list is empty.")
            return

        print("\n--- Your To-Do List ---")

        for task in tasks:
            status_icon = "Done" if task.is_done else "Todo"
            print(f"[{task.id}] [{status_icon}] {task.title}")

        print("-----------------------")

    elif args.command == "done":
        if todo.done(args.id):
            print(f"Task {args.id} marked as done.")
        else:
            print(f"Task with ID {args.id} not found.")

    elif args.command == "delete":
        if todo.delete(args.id):
            print(f"Task {args.id} deleted successfully.")
        else:
            print(f"Task with ID {args.id} not found.")

    elif args.command == "edit":
        is_done = None

        if args.status == "done":
            is_done = True
        elif args.status == "todo":
            is_done = False

        if todo.edit(
            args.id,
            new_title=args.title,
            is_done=is_done,
        ):
            print(f"Task {args.id} updated successfully.")
        else:
            print(f"Task with ID {args.id} not found.")


if __name__ == "__main__":
    main()
