class User:
    """
    Representa um usuário do sistema.
    """

    def __init__(self, id, username, password):
        """
        Inicializa um objeto User.

        Args:
            id (int): O ID único do usuário.
            username (str): O nome de usuário do usuário.
            password (str): A senha do usuário.
        """
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        """
        Retorna uma representação de string do objeto User.

        Returns:
            str: A representação de string do usuário.
        """
        return f"User(id={self.id}, username={self.username})"