if __name__ == '__main__':
    print("Witaj!")

    try:
        number: int = int(input("Podaj liczbe załkowitą: "))
    except ValueError as e:
        print("Musisz podac liczbe!")
    else:
        if number % 2 == 0:
            print("Liczba jest podzielna przez 7")
        else:
            print("Liczba NIE jest podzielna przez 7")
