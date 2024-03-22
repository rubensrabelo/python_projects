class Task:
    """
    Representa uma tarefa do sistema.

    Attributes:
        id (int): O ID único da tarefa.
        date_conclusion (str): A data de conclusão da tarefa no formato "dd/mm/aaaa".
        name (str): O nome ou título da tarefa.
        status (int): O status da tarefa (0: Pendente, 1: Em andamento, 2: Concluída). Padrão é 0.
    """

    def __init__(self, id, date, name, status=0):
        """
        Inicializa um objeto Task.

        Args:
            id (int): O ID único da tarefa.
            date (str): A data de conclusão da tarefa no formato "dd/mm/aaaa".
            name (str): O nome ou título da tarefa.
            status (int, optional): O status da tarefa (0: Pendente, 1: Em andamento, 2: Concluída). Padrão é 0.
        """
        self.id = id
        self.date_conclusion = date
        self.name = name
        self.status = status

    def __str__(self):
        """
        Retorna uma representação de string do objeto Task.

        Returns:
            str: A representação de string da tarefa.
        """
        return f"Task(id={self.id}, title={self.title}, status={self.status})"