from datetime import datetime

class Validate():
    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
        except Exception:
            return False

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise TypeError("Error - name must be a string.")
        if not name:
            raise ValueError("Error - name cannot be empty.")

    @staticmethod
    def validate_status(status):
        if not isinstance(status, int):
            raise TypeError("Error - status must be an integer.")
        if not status in range(3):
            raise ValueError("Error - status must be in the range from 0 to 2.")


if __name__ == "__main__":
    ...