# Oleksii Yermolaiev 16c


from time import sleep


def my_input(value_name, converter):
    while True:
        user_input = input(value_name + ": ")
        converted = converter(user_input)
        if converted is not None:
            return converted
        else:
            print("Niepoprawny format")


def wiek_validator(user_input):
    try:
        wiek = int(user_input)
        if wiek <= 0:
            return None

        return wiek
    except ValueError:
        return None


def wzrost_validator(user_input):
    try:
        wzrost = float(user_input)
        if wzrost <= 0:
            return None

        return wzrost
    except ValueError:
        return None


def str_validator(user_input):
    user_input = user_input.strip()
    if len(user_input) == 0:
        return None

    return user_input


if __name__ == '__main__':
    print(" Podaj swoje dane:")
    wiek = my_input("Wiek", wiek_validator)
    wzrost = my_input("Wzrost", wzrost_validator)
    kolor_oczu = my_input("Kolor oczu", str_validator)
    kolor_wlosow = my_input("Kolor włosów", str_validator)

    print("\n Wysyłanie danych do google.com... ", end='')
    sleep(2)
    print("Dziękuję")
