from datetime import datetime

class Validate():
    """
    A utility class for data validation.

    This class provides static methods to validate various types of data, such as dates, names, status, and list indices.

    Methods:
        validate_date(date_str): Validate if a string represents a date in the correct format.
        validate_name(name): Validate if the name is a non-empty string.
        validate_status(status): Validate if the status is an integer within the range [0, 2].
        validate_index(list_user, index): Validate if the index is within the bounds of the list.
    """
    @staticmethod
    def validate_date(date_str):
        """
        Validate if a string represents a date in the correct format.

        Args:
            date_str (str): The string containing the date to validate.

        Returns:
            bool: True if the date is valid, False otherwise.
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
        Validate if the name is a non-empty string.

        Args:
            name (str): The name to validate.

        Raises:
            TypeError: If the name is not a string.
            ValueError: If the name is empty.
        """
        if not isinstance(name, str):
            raise TypeError("Error - name must be a string.")
        if not name:
            raise ValueError("Error - name cannot be empty.")

    @staticmethod
    def validate_status(status):
        """
        Validate if the status is an integer within the range [0, 2].

        Args:
            status (int): The status to validate.

        Raises:
            TypeError: If the status is not an integer.
            ValueError: If the status is not within the specified range.
        """
        if not isinstance(status, int):
            raise TypeError("Error - status must be an integer.")
        if not status in range(3):
            raise ValueError("Error - status must be in the range from 0 to 2.")
        
    @staticmethod
    def validate_index(list_user, index):
        """
        Validate if the index is within the bounds of the list.

        Args:
            list_user (list): The list to validate.
            index (int): The index to validate.

        Returns:
            bool: True if the index is valid, False otherwise.
        """
        try:
            list_user[index]
            return True
        except IndexError:
            return False


if __name__ == "__main__":
    ...