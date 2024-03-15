from task import Task


class Task_manager():
    def __init__(self):
        self.task_list = []

    def add_task(self, date, name, status=0):
        task = Task(date, name, status)
        self.task_list.append(task)

    def remove_task(self, index):
        del self.task_list.pop(index)

    def __str__(self):
        ...

    def __rep__(self):
        ...


if __name__ == "__main__":
    ...