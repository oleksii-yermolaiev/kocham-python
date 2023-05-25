def print_table(data):
    print("Nr Nazwa produkt Ilość Cena")
    print("===========================")

    for i, item in enumerate(data):
        print(f"{i + 1:2} {item['name']:13} {item['amount']:5} {item['price']:4}")


def input_with_converter(prompt, converter):
    while True:
        try:
            return converter(input(prompt))
        except ValueError:
            print("Błędna wartość")


def ask_for_product():
    name = input("Nazwa: ")
    amount = input_with_converter("Ilość: ", int)
    price = input_with_converter("Cena: ", float)
    return {'name': name, 'amount': amount, 'price': price}


def ask_for_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Trzeba podać liczbę")


if __name__ == "__main__":
    products = []
    while True:
        print("Podaj komende (dodaj, usun, pokaz, zmien):")
        command = input(" > ")

        if command == "dodaj":
            products.append(ask_for_product())
        elif command == "usun":
            print_table(products)
            index = ask_for_int("Nr: ") - 1
            if 0 <= index < len(products):
                del products[index]
            else:
                print("Niepoprawny numer")
        elif command == "pokaz":
            print_table(products)
        elif command == "zmien":
            print_table(products)
            index = ask_for_int("Nr: ") - 1
            if 0 <= index < len(products):
                new_values = ask_for_product()
                products[index] = new_values
            else:
                print("Niepoprawny numer")
        else:
            print("Nieznana komenda")
