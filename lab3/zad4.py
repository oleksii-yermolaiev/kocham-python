def ask_for_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Trzeba podać liczbę")


def catalan_numbers():
    current = 1
    n = 0
    while True:
        yield current

        current = int(2 * (2 * n + 1) / (n + 2) * current)
        n += 1


if __name__ == "__main__":
    top = ask_for_int("Podaj górną granicę: ")

    for i in catalan_numbers():
        if i > top:
            break

        print(i)
