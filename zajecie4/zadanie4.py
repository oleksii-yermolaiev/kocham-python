def ask_for_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Trzeba podać liczbę")


if __name__ == "__main__":
    a = ask_for_int("Podaj dolną granicę: ")
    b = ask_for_int("Podaj górną granicę: ")

    if b < a:
        print("Uwaga: górna granica jest mniejsza od dolnej, podany przedział nie zawiera żadnej liczby")

    for i in range(a, b + 1):
        print(i)
