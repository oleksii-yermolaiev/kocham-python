def show_employee(surname, salary=9000):
    print(f"Nazwisko: {surname}, wynagrodzenie: {salary}")


if __name__ == "__main__":
    surname = input("Nazwisko: ")
    salary = input("Wynagrodzenie (opcjonalnie): ")
    try:
        show_employee(surname, int(salary))
    except ValueError:
        show_employee(surname)
