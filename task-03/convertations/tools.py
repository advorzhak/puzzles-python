import contextlib


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
        print(value)
        with contextlib.suppress(ValueError):
            parsed_value = int(value)
            if int(parsed_value) >= 0:
                return int(parsed_value)
            else:
                return None
        return None
