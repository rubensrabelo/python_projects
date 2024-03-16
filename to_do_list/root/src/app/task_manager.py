from task import Task
from validate import Validate


class Task_manager():
    def __init__(self):
        self.task_list = []

    def add_task(self, date, name, status=0):
        task = Task(date, name, status)
        self.task_list.append(task)

    def remove_task(self, index):
        if not Validate.validate_index(self.task_list, index):
            raise IndexError("Error - Invalid Index.")

        del self.task_list.pop(index)
    
    def alter_status(self, status, index):
        if not Validate.validate_index(self.task_list, index):
            raise IndexError("Error - Invalid Index.")

        self.task_list[index].status = status

    def __str__(self):
        if not self.task_list:
            return "No tasks found. The task list is currently empty."
        
        return "\n".join(str(task) for task in self.task_list)


if __name__ == "__main__":
    ...