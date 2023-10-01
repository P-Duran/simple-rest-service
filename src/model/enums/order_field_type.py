from enum import Enum
from time import strptime


class OrderFieldType(Enum):
    Date = "date"
    String = "string"

    def validate(self, value: any):
        def is_datetime(x):
            try:
                strptime(x, '%d-%m-%Y')
                return True
            except:
                return False

        validators = {OrderFieldType.Date: is_datetime, OrderFieldType.String: lambda x: type(x) == str}
        return validators[self](value)
