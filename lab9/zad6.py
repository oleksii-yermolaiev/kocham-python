def trojkapitagorejska(a, b, c):
    return a * a + b * b == c * c


if __name__ == "__main__":
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))

    print(trojkapitagorejska(a, b, c))
