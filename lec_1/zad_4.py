if __name__ == '__main__':
    wiek: int = int(input("Podaj wiek: "))

    if wiek < 0:
        print("nie poprawny wiek")
    elif wiek == 0:
        print("niemowle")
    elif wiek < 18:
        print("Dziecko")
    elif wiek > 18 and wiek < 120:
        print("Dorosly")
    else:
        print("Ludzie tyle nie zyją")
