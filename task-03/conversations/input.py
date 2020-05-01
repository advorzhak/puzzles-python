import re
from tools import Tools


class Input:
    __message: str = "Hi, input number for us to be able print it into words: "
    __value: int = None

    def __init__(self, message: str = None):
        if message:
            self.__message = message

    @staticmethod
    def __parsevalue(value: str):
        return Tools.value_validation(value)

    def read_value(self):
        while self.__value is None:
            input_value = input(self.__message)
            self.__value = Input.__parsevalue(input_value)

    def get_value(self):
        return self.__value

    def set_value(self, value: int):
        self.__value = value

