from datetime import datetime

class Validate():
    """
    Uma classe utilitária para validação de dados.

    Esta classe fornece métodos estáticos para validar vários tipos de dados, como datas, nomes, status e índices de listas.

    Métodos:
        validar_data(data_str): Valida se uma string representa uma data no formato correto.
        validar_nome(nome): Valida se o nome é uma string não vazia.
        validar_status(status): Valida se o status é um inteiro dentro do intervalo [0, 2].
        validar_indice(lista_usuario, indice): Valida se o índice está dentro dos limites da lista.
    """
    @staticmethod
    def validate_date(date_str):
        """
        Valida se uma string representa uma data no formato correto.

        Args:
            data_str (str): A string contendo a data a ser validada.

        Returns:
            bool: True se a data for válida, False caso contrário.
        """
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
        except Exception:
            return False

    @staticmethod
    def validate_name(name):
        """
        Valida se o nome é uma string não vazia.

        Args:
            nome (str): O nome a ser validado.

        Raises:
            TypeError: Se o nome não for uma string.
            ValueError: Se o nome estiver vazio.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name:
            raise ValueError("Name cannot be empty.")

    @staticmethod
    def validate_status(status):
        """
        Valida se o status é um inteiro dentro do intervalo [0, 2].

        Args:
            status (int): O status a ser validado.

        Raises:
            TypeError: Se o status não for um inteiro.
            ValueError: Se o status não estiver dentro do intervalo especificado.
        """
        if not isinstance(status, int):
            raise TypeError("Status must be an integer.")
        if not status in range(3):
            raise ValueError("Status must be in the range from 0 to 2.")
        
    @staticmethod
    def validate_index(list_user, index):
        """
        Valida se o índice está dentro dos limites da lista.

        Args:
            lista_usuario (list): A lista a ser validada.
            indice (int): O índice a ser validado.

        Returns:
            bool: True se o índice for válido, False caso contrário.
        """
        try:
            list_user[index]
            return True
        except IndexError:
            return False
