import re


class Input:
    __message: str = "Hi, input number for us to be able print it into words:"
    __value: int = None

    def __init__(self, message: str = None):
        self.__message = message

    @staticmethod
    def __isinteger(value: any):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def __parsevalue(value: str):
        parsed_value = re.findall('^((\"|\'){0,2})([\d\.]*)((\"|\'){0,2})$', value)
        return {True: int(parsed_value[0][2]), False: None}[parsed_value and Input.__isinteger(parsed_value[0][2]) and parsed_value != "NaN"]

    def read_value(self):
        while self.__value is None:
            input_value = input(self.__message)
            self.__value = Input.__parsevalue(input_value)

    def get_value(self):
        return self.__value

    def set_value(self, value: int):
        self.__value = value

