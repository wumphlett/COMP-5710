def _sanitize(a, b):
    if not isinstance(a, int) and not isinstance(a, float) and not (isinstance(a, str) and a.isnumeric()):
        raise ValueError(f"parameter a ({a}) is not a valid num")
    if not isinstance(b, int) and not isinstance(b, float) and not (isinstance(b, str) and b.isnumeric()):
        raise ValueError(f"parameter b ({b}) is not a valid num")
    return int(a), int(b)


def add(a, b):
    a, b = _sanitize(a, b)
    return a + b


def subtract(a, b):
    a, b = _sanitize(a, b)
    return a - b


def multiply(a, b):
    a, b = _sanitize(a, b)
    return a * b


def divide(a, b):
    a, b = _sanitize(a, b)
    if b == 0:
        raise ZeroDivisionError
    return a / b
