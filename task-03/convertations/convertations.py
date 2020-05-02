import inflect
from tools import Tools


class Transform:
    __init_value = None
    __inflect_engine: inflect.engine = None

    def __init__(self, value: int):
        self.__inflect_engine = inflect.engine()
        self.__init_value = value

    def get_number_into_words(self):
        validated_value = Tools.value_validation(str(self.__init_value))
        return {True: self.__inflect_engine.number_to_words(validated_value), False: None}[validated_value is not None]

    def print_number_into_words(self):
        print(self.get_number_into_words())
