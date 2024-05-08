# wyniki wypisz na konsoli
import sys

# 2A.
# Wypisz 10 następnych liczb naturalnych od wskazanej liczby (wyłącznie). 
# Przykład, number = 5, wyświetl od 5 do 14

# 2B. 
# Napisz program, który będzie zwracał tabliczkę mnożenia (do 20.) dla podanej liczby 
# UWAGA - w dwóch kolumnach, moe być w podziale parzyste/nieparzyste


# 2C.
# pobierz od użytkownika liczbę (pomińmy sprawdzanie czy to liczba, póki co...)
# dodaj do niej wszystkie liczby w zakresie od 0 do tej liczby (włącznie!)

if __name__ == '__main__':
    # 2A.

    # number: int = int(input("Podaj liczbe "))
    #
    # for i in range(number, number+10):
    #     print(i, end=", ")



    # 2B.

    # table_size: int = int(input("Podaj rozmiar tablicy "))
    # if table_size > 20:
    #     print("Liczab jest za duża")
    #     sys.exit(1)
    #
    # mult_table: [[int]] = []
    # for i in range(1, table_size + 1):
    #     row: [int] = []
    #     for j in range(1, table_size + 1):
    #         row.append(i * j)
    #     mult_table.append(row)
    #
    # for row in mult_table:
    #     print(row)



    # 2C.

    number: int = int(input("Podaj liczbe: "))

    for i in range(0, number):
        number += i

    print(number)
