from enum import Enum
from time import strptime


class OrderFieldType(Enum):
    Date = "date"
    Time = "time"
    String = "string"
    Integer = "int"
    Float = "float"

    def validate(self, value: any):
        def is_date(x):
            try:
                strptime(x, '%d-%m-%Y')
                return True
            except:
                return False

        def is_time(x):
            try:
                strptime(x, "%H:%M:%S")
                return True
            except:
                return False

        validators = {OrderFieldType.Date: is_date,
                      OrderFieldType.Time: is_time,
                      OrderFieldType.String: lambda x: isinstance(x, str),
                      OrderFieldType.Integer: lambda x: isinstance(x, int),
                      OrderFieldType.Float: lambda x: isinstance(x, float)}

        return validators[self](value)
