tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

# Example usage:
add_task("Buy groceries")
add_task("Finish assignment")
mark_done(0)
show_tasks()

