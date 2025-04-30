#!/usr/bin/env python3
GREEN = "\033[38;5;82m"
RESET = "\033[0m"

import json
import os

DATA_FILE = os.path.expanduser("~/.todo-sample")


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def green_print(message):
    print(GREEN + message + RESET)


def print_help():
    green_print("Commands:")
    green_print("  help      Show this help message")
    green_print("  add       Add a new TODO")
    green_print("  list      List all TODOs")
    green_print("  edit      Edit an existing TODO")
    green_print("  delete    Delete a TODO")
    green_print("  complete  Mark a TODO as complete")
    green_print("  exit      Exit the application")


def main():
    tasks = load_tasks()
    next_id = max((task['id'] for task in tasks), default=0) + 1

    green_print("Welcome to the TODO CLI application.")
    print_help()

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command in ["exit", "quit"]:
            green_print("Goodbye!")
            break
        elif command == "help":
            print_help()
        elif command == "add":
            title = input("Title: ").strip()
            description = input("Description (optional): ").strip()
            tasks.append({
                "id": next_id,
                "title": title,
                "description": description,
                "completed": False
            })
            green_print(f"Task {next_id} added.")
            next_id += 1
            save_tasks(tasks)
        elif command == "list":
            if not tasks:
                green_print("No tasks available.")
            else:
                for task in tasks:
                    status = "Done" if task["completed"] else "Pending"
                    green_print(f"{task['id']}. {task['title']} [{status}]")
                    if task["description"]:
                        green_print(f"   {task['description']}")
        elif command == "delete":
            try:
                task_id = int(input("Enter task id to delete: ").strip())
            except ValueError:
                green_print("Invalid id.")
                continue
            task_found = False
            for task in tasks:
                if task["id"] == task_id:
                    tasks.remove(task)
                    task_found = True
                    green_print(f"Task {task_id} deleted.")
                    break
# TODO: Add save_tasks(tasks) here to persist changes after deletion

            if not task_found:
                green_print("Task not found.")
        elif command == "edit":
            try:
                task_id = int(input("Enter task id to edit: ").strip())
            except ValueError:
                green_print("Invalid id.")
                continue
            for task in tasks:
                if task["id"] == task_id:
                    new_title = input(f"New title (leave empty to keep '{task['title']}'): ").strip()
                    if new_title:
                        task["title"] = new_title
                    new_description = input("New description (leave empty to keep current): ").strip()
                    if new_description:
                        task["description"] = new_description
# TODO: Add save_tasks(tasks) here to persist changes after editing

                    green_print("Task updated.")
                    break
            else:
                green_print("Task not found.")
        elif command == "complete":
            try:
                task_id = int(input("Enter task id to mark as complete: ").strip())
            except ValueError:
                green_print("Invalid id.")
                continue
            for task in tasks:
# TODO: Add save_tasks(tasks) here to persist changes after marking as complete

                if task["id"] == task_id:
                    task["completed"] = True
                    green_print("Task marked as complete.")
                    break
            else:
                green_print("Task not found.")
        else:
            green_print("Unknown command. Type 'help' for a list of commands.")


if __name__ == '__main__':
    main()
