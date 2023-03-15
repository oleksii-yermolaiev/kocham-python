# Oleksii Yermolaiev s25653


import time


# (nazwa, system)
NUMBER_DESCRIPTIONS = [
    ("W systemie dwójkowym", 2),
    ("W systemie ósemkowym", 8),
    ("W systemie szestanstkowym", 16),
]


if __name__ == '__main__':
    print("Wprowadź swoje liczby:")
    numbers = []
    for description in NUMBER_DESCRIPTIONS:
        user_input: str = input(f" {description[0]}: ")
        value: int = int(user_input, description[1])
        numbers.append(value)

    print("\nKonwertacja...\n")
    time.sleep(2)  # Udajemy pracę

    print("Twoje liczby:")
    for description, number in zip(NUMBER_DESCRIPTIONS, numbers):
        print(f" {description[0]}: {number}")
