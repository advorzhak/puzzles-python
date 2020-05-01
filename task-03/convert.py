from conversations.input import Input
from conversations.covnertations import Transform

def main():
    console_input = Input()
    console_input.read_value()
    transform = Transform(console_input.get_value())
    transform.print_number_into_words()


if __name__ == "__main__":
    main()
