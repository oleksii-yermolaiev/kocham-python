if __name__ == "__main__":
    print("Podaj swoje dane")
    name = input("Imie: ")
    date_of_birth = input("Data urodzenia: ")
    email = input("Adres e-mail: ")
    phone_number = input("Numer telefonu: ")

    print("Lista:", [name, date_of_birth, email, phone_number])
    print("Kratka:", (name, date_of_birth, email, phone_number))
    print("Słownik: ", {
        'name': name,
        'date_of_birth': date_of_birth,
        'email': email,
        'phone_number': phone_number
    })
