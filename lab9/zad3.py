def obliczanie(a, b):
    return a + b, a - b


if __name__ == "__main__":
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

    sum_, diff = obliczanie(a, b)
    print(f"Suma: {sum_}, roznica: {diff}")
