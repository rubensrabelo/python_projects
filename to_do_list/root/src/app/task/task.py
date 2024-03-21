import sys
sys.path.append("/to_do_list/root/src/utils/")
from datetime import datetime

from utils.validate import Validate


class Task():
    """
    Representa uma tarefa que possui uma data de vencimento, um nome descritivo e um status de conclusão.

    Atributos:
        date (date): A data de vencimento da tarefa.
        name (str): O nome descritivo da tarefa.
        status (int): O status de conclusão da tarefa, onde:
            - 0: Tarefa não concluída
            - 1: Tarefa concluída
    """

    def __init__(self, date, name, status=0):
        """
        Inicializa uma nova instância da classe Task.

        Args:
            date (str): A data da tarefa no formato 'dd/mm/yyyy'.
            name (str): O nome da tarefa.
            status (int, optional): O status da tarefa. Padrão é 0.

        Raises:
            ValueError: Se a data estiver em formato inválido.
            TypeError: Se o nome não for uma string.
            ValueError: Se o nome estiver vazio.
            TypeError: Se o status não for um inteiro.
            ValueError: Se o status estiver fora do intervalo permitido.
        """
        if Validate.validate_date(date):
            raise ValueError("Error - Invalid date format, please use the format dd/mm/yyyy.")
        
        Validate.validate_name(name)
        Validate.validate_status(status)
        
        self.date_str_conclusion = date

        # Alert: I have to test if the user change correct the date

        self.date_conclusion = datetime.strptime(date, "%d/%m/%Y").date()
        self.name = name
        self.status = status

    def __str__(self) -> str:
        """
        Retorna uma representação em string da tarefa.

        Returns:
            str: Uma string contendo a data, o nome e o status da tarefa.
        """
        return f"Date: {self.date_str_conclusion}, Name: {self.name}, Status: {self.status}"

    def __repr__(self) -> str:
        """
        Retorna uma representação em string da tarefa para uso em debug.

        Returns:
            str: Uma string contendo a data, o nome e o status da tarefa.
        """
        return f"Task(Date: {self.date_str_conclusion}, Name: {self.name}, Status: {self.status})"

if __name__ == "__main__":
    task = Task("01/01/2022", "tarefa 01")

    