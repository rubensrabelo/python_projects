from datetime import datetime

class Task():
    """
    Representa uma tarefa que possui uma data de vencimento, um nome descritivo e um status de conclusão.

    Atributos:
        conclusion_date (datetime.date): A data de vencimento da tarefa.
        name (str): O nome descritivo da tarefa.
        status (int): O status de conclusão da tarefa, onde:
            - 0: Tarefa não concluída
            - 1: Tarefa concluída
            - 2: Tarefa incompleta
    """
    def __init__(self, date, name, status=0): 
        """
        Inicializa uma nova instância da classe Task.

        Args:
            date (str): A data da tarefa no formato 'dd/mm/yyyy'.
            name (str): O nome da tarefa.
            status (int, optional): O status da tarefa. Padrão é 0 (tarefa não concluída).
        """
        self.conclusion_date = datetime.strptime(date, "%d/%m/%Y")
        self.name = name
        self.status = status
        self.str_date = date

    def __str__(self) -> str:
        """
        Retorna uma representação em string da tarefa.

        Returns:
            str: Uma string contendo a data, o nome e o status da tarefa.
        """
        return f"Date: {self.str_date}, Name: {self.name}, Status: {self.status}"

    def __repr__(self) -> str:
        """
        Retorna uma representação em string da tarefa para uso em debug.

        Returns:
            str: Uma string contendo a data, o nome e o status da tarefa.
        """
        return f"Task(Date: {self.str_date}, Name: {self.name}, Status: {self.status})"
