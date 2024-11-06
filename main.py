import json

def add_task(name):
    with open("task_list.json", "r") as f:
        data = json.load(f)

    data["tasks"].append({
        "id": str(len(data["tasks"]) + 1),
        "name": name,
        "status": "todo"
    })

    with open("task_list.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Task has been successfully created (id: {len(data["tasks"])})")

def update_task(id, name):
    with open("task_list.json", "r") as f:
        data = json.load(f)

    try:
        data["tasks"][id - 1].update({"name": name})

        with open("task_list.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"Task {id} has been updated")
    except:
        print("No task with such id")

def delete_task(id):
    with open("task_list.json", "r") as f:
        data = json.load(f)

    try:
        data["tasks"].pop(id - 1)

        with open("task_list.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"Task {id} has been deleted")
    except:
        print("No task with such id")

def in_progress(id):
    with open("task_list.json", "r") as f:
        data = json.load(f)

    try:
        data["tasks"][id - 1].update({"status": "In progress"})

        with open("task_list.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Status has been updated to In progress")
    except:
        print("No task with such id")

def done(id):
    with open("task_list.json", "r") as f:
        data = json.load(f)

    try:
        data["tasks"][id - 1].update({"status": "Done"})

        with open("task_list.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Status has been updated to Done")
    except:
        print("No task with such id")

def task_list():
    with open("task_list.json", "r") as f:
        data = json.load(f)

    if len(data["tasks"]) == 0:
        print("Task list is empty")
    else:
        for i in data["tasks"]:
            print(f"Id: {i["id"]}, Name: {i["name"]}, Task Status: {i["status"]}")

while True:
    command = input("Enter command: ")

    try:
        if command[:3] == "add":
            add_task(command.split('"')[1::2][0])

        elif command[:6] == "update":
            update_task(int(command.split(" ")[1]), command.split('"')[1::2][0])

        elif command[:6] == "delete":
            delete_task(int(command.split(" ")[1]))

        elif command[:16] == "mark-in-progress":
            in_progress(int(command.split(" ")[1]))

        elif command[:9] == "mark-done":
            done(int(command.split(" ")[1]))

        elif command[:4] == "list":
            task_list()

        elif command[:4] == "help":
            print("""----------------
add <task name>
update <task id> <updated task name>
delete <task id>
mark-in-progress <task id>
mark-done <task id>
list <Optional: done, todo, in-progress>
----------------""")

        else:
            print("Unknown command: type 'help' to view the list of commands")
            
    except Exception as e:
        print("Invalid syntax")
        print(f"Error: {e}")
