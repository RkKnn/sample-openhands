#!/usr/bin/env python3

def print_help():
    print("Commands:")
    print("  help      Show this help message")
    print("  add       Add a new TODO")
    print("  list      List all TODOs")
    print("  edit      Edit an existing TODO")
    print("  delete    Delete a TODO")
    print("  complete  Mark a TODO as complete")
    print("  exit      Exit the application")


def main():
    tasks = []
    next_id = 1

    print("Welcome to the TODO CLI application.")
    print_help()

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command in ["exit", "quit"]:
            print("Goodbye!")
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
            print(f"Task {next_id} added.")
            next_id += 1
        elif command == "list":
            if not tasks:
                print("No tasks available.")
            else:
                for task in tasks:
                    status = "Done" if task["completed"] else "Pending"
                    print(f"{task['id']}. {task['title']} [{status}]")
                    if task["description"]:
                        print(GREY + f"   {task['description']}" + RESET)
        elif command == "delete":
            try:
                task_id = int(input("Enter task id to delete: ").strip())
            except ValueError:
                print("Invalid id.")
                continue
            task_found = False
            for task in tasks:
                if task["id"] == task_id:
                    tasks.remove(task)
                    task_found = True
                    print(f"Task {task_id} deleted.")
                    break
            if not task_found:
                print("Task not found.")
        elif command == "edit":
            try:
                task_id = int(input("Enter task id to edit: ").strip())
            except ValueError:
                print("Invalid id.")
                continue
            for task in tasks:
                if task["id"] == task_id:
                    new_title = input(f"New title (leave empty to keep '{task['title']}'): ").strip()
                    if new_title:
                        task["title"] = new_title
                    new_description = input("New description (leave empty to keep current): ").strip()
                    if new_description:
                        task["description"] = new_description
                    print("Task updated.")
                    break
            else:
                print("Task not found.")
        elif command == "complete":
            try:
                task_id = int(input("Enter task id to mark as complete: ").strip())
            except ValueError:
                print("Invalid id.")
                continue
            for task in tasks:
                if task["id"] == task_id:
                    task["completed"] = True
                    print("Task marked as complete.")
                    break
            else:
                print("Task not found.")
        else:
            print("Unknown command. Type 'help' for a list of commands.")


if __name__ == '__main__':
    main()
