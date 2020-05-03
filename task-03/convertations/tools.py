import contextlib


def isinteger(value: any):
    try:
        int(value)
        return True
    except ValueError:
        return False


def value_validation(value: str):
    with contextlib.suppress(ValueError):
        parsed_value = int(value)
        if int(parsed_value) >= 0:
            return int(parsed_value)
        else:
            return None
    return None
