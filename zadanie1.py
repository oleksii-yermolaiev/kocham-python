# Oleksii Yermolaiev 16c


def solve(expr):
    index_op = None
    op = None
    for i, ch in enumerate(expr):
        if ch in ('+', '-', '*', '/'):
            index_op = i
            op = ch

    if index_op is None:
        raise Exception("Nie ma operatora")

    first_number = int(expr[:index_op].strip())
    second_number = int(expr[index_op+1:].strip())

    match op:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number
        case '/':
            return first_number / second_number
        case other:
            raise Exception(f"Nieznany operator {other}")


if __name__ == '__main__':
    print("Epicki Kalkulator")
    while True:
        expr = input(" > ")
        try:
            print(solve(expr))
        except Exception as e:
            print("Bląd:", e)
