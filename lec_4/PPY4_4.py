# -*- coding: utf-8 -*-
# Napisz funckje, która przyjmuje dowolną ilość liczb (args*) i znaków działania (kwargs**), gdzie znakami działania mogą być:
# '+', '-', '*', '/'
# Funckcja ma zwracać wynik działania na liczbach
def kalkulator(*args, **kwargs):
    result = args[0]  # Początkowa wartość wyniku

    for i, num in enumerate(args[1:], start=1):
        if f'działanie_{i}' in kwargs:
            operator = kwargs[f'działanie_{i}']
            if operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator == '*':
                result *= num
            elif operator == '/':
                if num != 0:
                    result /= num
                else:
                    raise ValueError("Nie można dzielić przez zero.")
            else:
                raise ValueError("Nieprawidłowy operator.")

    print(result)


# Przykładowe użycie funkcji
kalkulator(10, 8, 2, działanie_1='*', działanie_2="+")  # 82
