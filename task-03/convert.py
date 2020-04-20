import inflect


def main():

    p = inflect.engine()
    print(p.number_to_words(1345))


if __name__ == "__main__":
    main()
