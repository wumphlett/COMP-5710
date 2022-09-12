def simpleCalculator(v1, v2, operation):
    res = 0
    if operation == "+":
        res = v1 + v2
    elif operation == "-":
        res = v1 - v2
    elif operation == "*":
        res = v1 * v2
    elif operation == "/":
        res = v1 / v2
    elif operation == "%":
        res = v1 % v2
    return res


if __name__ == "__main__":
    val1, val2, op = 100, 1, "+"

    data = simpleCalculator(val1, val2, op)
    print("Operation:{}\nResult:{}".format(op, data))
