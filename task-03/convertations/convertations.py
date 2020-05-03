import inflect
import tools
from num2words import num2words
from enum import Enum


class LibraryType(Enum):
    NUM2WORDS = "num2words"
    INFLECT = "inflect"


class Transform:
    __message: str = "Hi, input number for us to be able print it into words: "
    __value: int = None
    __inflect_engine: inflect.engine = None
    __library_type: LibraryType = None

    def __init__(self, value: int = None, message: str = None, library_type: LibraryType = LibraryType.NUM2WORDS):
        self.__library_type = library_type
        if self.__library_type == library_type.INFLECT:
            self.__inflect_engine = inflect.engine()
        if message:
            self.__message = message
        if value:
            self.__value = value

    @staticmethod
    def __parsevalue(value: str):
        return tools.value_validation(value)

    def read_value(self):
        while self.__value is None:
            input_value = input(self.__message)
            self.__value = Transform.__parsevalue(input_value)

    def get_value(self):
        return self.__value

    def set_value(self, value: int):
        self.__value = value

    def get_number_into_words(self):
        validated_value = tools.value_validation(str(self.__value))
        if self.__library_type.value is LibraryType.INFLECT:
            return {True: self.__inflect_engine.number_to_words(validated_value), False: None}[validated_value is not None]
        return {True: num2words(validated_value), False: None}[validated_value is not None]

    def print_number_into_words(self):
        print(self.get_number_into_words())
