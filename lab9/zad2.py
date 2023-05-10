def func1(*args):
    print(*args)


if __name__ == "__main__":
    func1(1, 2, 3)
    func1("Hello,", "world!")
    func1()
