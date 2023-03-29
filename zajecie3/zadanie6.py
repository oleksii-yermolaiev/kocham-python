def ask_for_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Trzeba podać liczbę")


if __name__ == "__main__":
    a = ask_for_int("Podaj dolną granicę: ")
    b = ask_for_int("Podaj górną granicę: ")

    first_odd = a if a % 2 == 1 else a + 1
    sum_of_odds = sum(range(first_odd, b + 1, 2))
    print(sum_of_odds)
