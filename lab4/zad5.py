def ask_for_int(prompt: str, validator) -> int:
    while True:
        try:
            val = int(input(prompt))
            if validator(val):
                return val

            print("Podana liczba nie pasuje")
        except ValueError:
            print("Trzeba podać liczbę")


if __name__ == "__main__":
    ask_for_int("Podaj liczbe całkowitą dodatnią: ", lambda x: x > 0)
