from datetime import datetime
from validate import Validate


class Task():
    def __init__(self, date, name, status=0):
        if Validate.validate_date(date):
            raise ValueError("Error - Invalid date format, please use the format dd/mm/yyyy.")
        
        Validate.validate_name(name)
        Validate.validate_status(status)

        self.date = datetime.strptime(date, "%d/%m/%Y").date()
        self.name = name
        self.status = status

    def __str__(self) -> str:
        date_str = datetime.strftime(self.date, "%d/%m/%Y")
        output = f"Date: {date_str}, Name: {self.name}, Status: {self.status}"
        return output

    def __repr__(self) -> str:
        date_str = datetime.strftime(self.date, "%d/%m/%Y")
        output = f"Task(Date: {date_str}, Name: {self.name}, Status: {self.status})"
        return output

if __name__ == "__main__":
    ...