# -*- coding: utf-8 -*-
"""
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu ax^2+bx+c.
Klasa powinna zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze.
Główną metodą powinna być Rozwiaz(), która zwraca miejsca zerowe podanej funkcji.
Klasa powinna zawierać metode wypisz, która wypisuje funckje w postacji iloczynowej, ogólnej i kanonicznej.
Klasa ma zawierać metode, która wyświetla na ektanie stwierdzenie, czy podane koordynaty punktu (x,y) należą do funkcji kwadratowej,
Klasa ma zawierać metody wyprintowujące monotoniczność funkcji ,zbiór wartości funkcji oraz
kiedy przyjmuje wartości ujemne i dodatnie.
Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0,
a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub zerze rozwiązań.
Uzględnij komunikaty, przy wyjątkach takich jak dzielenie przez 0 i wpisanie przez użytkownika nieliczby
Klasa może przyjmować liczby albo przez input albo przy wywołaniu.
"""


from typing import Union, Tuple


class FunkcjaKwadratowa:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def Rozwiaz(self) -> Union[None, Tuple[float, float], Tuple[float]]:
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta > 0:
            x1 = (-self.b + delta ** 0.5) / (2 * self.a)
            x2 = (-self.b - delta ** 0.5) / (2 * self.a)
            return x1, x2
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return x,
        else:
            return None

    def wypisz(self) -> None:
        print(f"Funkcja kwadratowa: {self.a}x^2 + {self.b}x + {self.c}")
        print("Postać iloczynowa: ", end="")
        if self.a != 0:
            print(f"{self.a}(x - x1)(x - x2)")
        elif self.b != 0:
            print(f"{self.b}x(x - x1)")
        else:
            print(f"{self.c}")
        print(f"Postać ogólna: {self.a}x^2 + {self.b}x + {self.c}")
        print("Postać kanoniczna: ", end="")
        if self.a != 0:
            vertex_x = -self.b / (2 * self.a)
            vertex_y = self.a * vertex_x ** 2 + self.b * vertex_x + self.c
            print(f"{self.a}(x - {vertex_x})^2 + {vertex_y}")
        else:
            print(self.c)

    def czy_nalezy(self, x: float, y: float) -> None:
        if self.a * x ** 2 + self.b * x + self.c == y:
            print(f"Punkt ({x}, {y}) należy do funkcji kwadratowej.")
        else:
            print(f"Punkt ({x}, {y}) nie należy do funkcji kwadratowej.")

    def monotonicznosc(self) -> None:
        if self.a > 0:
            print("Funkcja jest malejąca w przedziale (-inf, x1] i rosnąca w przedziale [x1, +inf).")
        elif self.a < 0:
            print("Funkcja jest rosnąca w przedziale (-inf, x1] i malejąca w przedziale [x1, +inf).")
        else:
            print("Funkcja jest stała.")

    def zbior_wartosci(self) -> None:
        if self.a > 0:
            print("Zbiór wartości funkcji to przedział (y_min, +inf).")
        elif self.a < 0:
            print("Zbiór wartości funkcji to przedział (-inf, y_min].")
        else:
            print(f"Zbiór wartości funkcji to {self.c}.")

    def kiedy_dodatnie_i_ujemne(self) -> None:
        if self.a > 0:
            print("Funkcja jest dodatnia w przedziale (x1, +inf) i ujemna w przedziale (-inf, x1).")
        elif self.a < 0:
            print("Funkcja jest ujemna w przedziale (x1, +inf) i dodatnia w przedziale (-inf, x1).")
        else:
            if self.c > 0:
                print("Funkcja jest dodatnia dla wszystkich x.")
            elif self.c < 0:
                print("Funkcja jest ujemna dla wszystkich x.")
            else:
                print("Funkcja przyjmuje wartość zero dla wszystkich x.")


if __name__ == '__main__':
    try:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        c = float(input("Podaj c: "))
        funkcja = FunkcjaKwadratowa(a, b, c)
        funkcja.wypisz()
        miejsca_zerowe = funkcja.Rozwiaz()
        if miejsca_zerowe is not None:
            print("Miejsca zerowe:", miejsca_zerowe)
        else:
            print("Brak miejsc zerowych.")
        funkcja.czy_nalezy(1, 4)
        funkcja.monotonicznosc()
        funkcja.zbior_wartosci()
        funkcja.kiedy_dodatnie_i_ujemne()
    except ValueError:
        print("Podano niepoprawne dane - oczekiwano liczby.")
    except ZeroDivisionError:
        print("Wystąpiło dzielenie przez zero.")
