if __name__ == '__main__':
    rownanie: str = input("Podaj rownanie kwadratowe a= b= c=: ")
    try:
        numbers: [float] = [float(num) for num in rownanie.split(" ")]

        delta = numbers[1] ** 2 - 4 * numbers[0] * numbers[2]
    except ValueError as e:
        print(f"Wprowadzono niepoprawne rownainie {e}")
    else:
        print(f"Delta = {delta}")
