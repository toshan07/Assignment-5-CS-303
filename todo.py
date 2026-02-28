tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

#added new feature
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed}" deleted.')
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    add_task("Finish Assignment")
    add_task("Study Git")
    list_tasks()
    delete_task(1)
    list_tasks()