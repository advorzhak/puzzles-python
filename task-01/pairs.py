import sys
import re


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def find_sums(inputs, sum_to_find=10):
    l: int = len(inputs)
    pairs = list()
    print("All pairs:")
    for i in range(l - 1):
        for j in range(i + 1, l):
            if inputs[i] + inputs[j] == sum_to_find:
                print("{0} + {1} = {2}".format(inputs[i], inputs[j], sum_to_find))
                current_pair = [inputs[i], inputs[j]]
                current_pair.sort()
                pairs.append(current_pair)
    print("Unique pairs:")
    unique_pairs = set(tuple(current_pair) for current_pair in pairs)
    for current_pair in unique_pairs:
        print("{0} + {1} = {2}".format(current_pair[0], current_pair[1], sum_to_find))


def main():
    inputs = []
    for current_input in sys.argv[1:]:
        current_input_parsed = re.findall('^((\"|\'){0,2})([\d.]*)((\"|\'){0,2})$', current_input)
        if current_input_parsed and isfloat(current_input_parsed[0][2]):
            if current_input_parsed != "NaN":
                inputs.append(float(current_input_parsed[0][2]))
            else:
                print("\"{0}\" - is NaN, ommited.".format(current_input_parsed[0][2]))
        else:
            print("\"{0}\" - isn't figure, ommited.".format(current_input))
    find_sums(inputs)


if __name__ == "__main__":
    main()
