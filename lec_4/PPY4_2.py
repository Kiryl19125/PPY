# -*- coding: utf-8 -*-
# Napisz funkcje validate_pesel, która przyjmuje ciąg znaków (str) i sprawdza, czy jest on poprawnie sformatowanym numerem PESEL.
# Numer PESEL składa się z 11 cyfr. W celu sprawdzenia sumy kontrolnej użyj wag [1, 3, 7, 9, 1, 3, 7, 9, 1, 3].
# Tutaj suma kontrolna to wynik odejmowania jedności od 10.
# Funkcja powinna zwracać wartość logiczną: True jeśli numer PESEL jest poprawny, False w przeciwnym przypadku.


weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def validate_pesel(pesel):
    # TWÓJ KOD

    scalar = 0
    for i in range(len(pesel) - 1):
        scalar += (int(pesel[i]) * weights[i])

    last_digit = int(repr(scalar)[-1])

    result = 10 - last_digit == int(pesel[-1])

    return result


print(validate_pesel('12345678901'))  # False
print(validate_pesel('44051401458'))  # True
