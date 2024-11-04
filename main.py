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

    for i in data["tasks"]:
        if i["id"] == str(id):
            print(i)

def delete_task(id):
    print(f"Task number {id} has been deleted")

def in_progress(id):
    print(f"Updated status of task number {id} to in progress")

def done(id):
    print(f"Marked task number {id} as done")

def task_list(status):
    print("Showing all the tasks")

while True:
    command = input("Enter command: ")

    try:
        if command[:3] == "add":
            add_task(command.split('"')[1::2][0])

        elif command[:6] == "update":
            update_task(int(command.split(" ")[1]), command.split('"')[1::2][0])

        elif command[:6] == "delete":
            pass

        elif command[:16] == "mark-in-progress":
            pass

        elif command[:9] == "mark-done":
            pass

        elif command[:4] == "list":
            pass

        else:
            print("Unknown command")
            
    except Exception as e:
        print("Invalid syntax")
        print(f"Error: {e}")
