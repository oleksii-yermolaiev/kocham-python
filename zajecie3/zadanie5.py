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


if __name__ == "__main__":
    products = [
        {'name': 'test', 'amount': 2, 'price': 20.0},
        {'name': 'aaa', 'amount': 2, 'price': 10.0}
    ]
    products.append(ask_for_product())
    print_table(products)
