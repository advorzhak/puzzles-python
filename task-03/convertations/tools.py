import re


class Tools:

    def __init__(self):
        pass

    @staticmethod
    def isinteger(value: any):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def value_validation(value: str):
        parsed_value = re.findall('^((\"|\'){0,2})((\-){0,1})([\d\.]*)((\"|\'){0,2})$', value)
        if parsed_value is not None and len(parsed_value) > 0:
            if parsed_value != "NaN" and Tools.isinteger(parsed_value[0][4]) and int(value) >= 0:
                return int(parsed_value[0][4])
            else:
                return None
        else:
            return None
