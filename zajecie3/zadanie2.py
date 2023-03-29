def ask_for_int(prompt: str, validator) -> int:
    while True:
        try:
            val = int(input(prompt))
            if validator(val):
                return val

            print("Podana liczba nie pasuje")
        except ValueError:
            print("Trzeba podać liczbę")


def is_prime(x: int) -> bool:
    return x >= 2 and not any(map(
        lambda divisor: x % divisor == 0,
        range(2, x // 2 + 1)
    ))


if __name__ == "__main__":
    numbers = []
    for i in range(20):
        numbers.append(ask_for_int("Podaj liczbę z zakresu od -20 do 20: ", lambda x: -20 <= x <= 20))

    numbers_copy = numbers.copy()
    prime_numbers = tuple(filter(is_prime, numbers))
    squared_even_numbers = tuple(map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    ))
    numbers_with_even_replaced_with_a = list(map(lambda x: 'A' if x % 2 == 0 else x, numbers))

    print("Kopia:", numbers_copy)
    print("Krotka z liczb pierwszych:", prime_numbers)
    print("Krotka z kwadratów liczby podzielnych przez 2:", squared_even_numbers)
    print("Pierwotna lista, ale liczby podzielne przez 2 są zamienione na A:", numbers_with_even_replaced_with_a)
