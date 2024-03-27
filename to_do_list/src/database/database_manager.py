import psycopg2

class DatabaseManager:
    """
    Gerencia a interação com o banco de dados PostgreSQL.
    """

    def __init__(self, dbname, user, password, host="localhost", port=5432):
        """
        Inicializa o DatabaseManager com as informações de conexão ao banco de dados PostgreSQL.

        Args:
            dbname (str): O nome do banco de dados.
            user (str): O nome do usuário do banco de dados.
            password (str): A senha do usuário do banco de dados.
            host (str): O host do banco de dados. Padrão é 'localhost'.
            port (int): A porta do banco de dados. Padrão é 5432.
        """

        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connection(self):
        """
        Estabelece uma conexão com o banco de dados PostgreSQL.
        """

        try:
            self.connection = psycopg2.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port
            )
            print("Connection established successfully.")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def close(self):
        """
        Fecha a conexão com o banco de dados PostgreSQL.
        """

        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, params=None):
        """
        Executa uma consulta SQL no banco de dados PostgreSQL.

        Args:
            query (str): A consulta SQL a ser executada.
            params (tuple, optional): Os parâmetros da consulta. Padrão é None.

        Returns:
            list: Uma lista de tuplas representando os resultados da consulta.
        """

        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def save(self, query, params=None):
        """
        Executa uma consulta SQL para inserir dados no banco de dados.

        Args:
            query (str): A consulta SQL de inserção.
            params (tuple, optional): Os parâmetros da consulta. Padrão é None.

        Returns:
            int: O ID do registro inserido, se aplicável.
        """
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Data inserted successfully.")
            inserted_id = cursor.fetchone()[0] if cursor.rowcount > 0 else None
            return inserted_id
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Error inserting data into the database: {e}")
        finally:
            cursor.close()
