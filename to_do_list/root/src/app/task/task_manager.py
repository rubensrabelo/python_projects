from task import Task

class Task_manager():
    """
    Classe para gerenciar uma lista de tarefas.

    Métodos:
        add_task(date, name, status=0): Adiciona uma nova tarefa à lista.
        remove_task(index): Remove a tarefa na posição especificada da lista.
        alter_status(status, index): Altera o status de uma tarefa na lista.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Task_manager.
        """
        self.task_list = []

    def add_task(self, date, name, status=0):
        """
        Adiciona uma nova tarefa à lista.

        Args:
            date (str): Data da tarefa no formato 'dd/mm/yyyy'.
            name (str): Nome descritivo da tarefa.
            status (int, optional): Status da tarefa. Padrão é 0.
        """
        task = Task(date, name, status)
        self.task_list.append(task)

    def remove_task(self, index):
        """
        Remove a tarefa na posição especificada da lista.

        Args:
            index (int): Índice da tarefa a ser removida.
        """
        self.task_list.pop(index)
    
    def alter_status(self, status, index):
        """
        Altera o status de uma tarefa na lista.

        Args:
            status (int): Novo status da tarefa.
            index (int): Índice da tarefa cujo status será alterado.
        """
        self.task_list[index].status = status

    def __str__(self):
        """
        Retorna uma representação em string da lista de tarefas.

        Returns:
            str: Uma string contendo todas as tarefas da lista, numeradas.
        """
        if not self.task_list:
            return "No tasks found. The task list is currently empty."
        
        return "\n".join(f"{index}: {task}" for index, task in enumerate(self.task_list))
