class FunkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Rozwiaz(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Nieskończona liczba rozwiązań"
                else:
                    return "Brak rozwiązań"
            else:
                return f"Rozwiązanie: x = {-self.c / self.b}"
        else:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta < 0:
                return "Brak rozwiązań"
            elif delta == 0:
                x = -self.b / (2 * self.a)
                return f"Rozwiązanie: x = {x}"
            else:
                x1 = (-self.b + delta ** 0.5) / (2 * self.a)
                x2 = (-self.b - delta ** 0.5) / (2 * self.a)
                return f"Rozwiązania: x1 = {x1}, x2 = {x2}"

    def wypisz(self):
        print(f"Funkcja kwadratowa: {self.a}x^2 + {self.b}x + {self.c}")
        print(f"W postaci iloczynowej: {self.a}(x - x1)(x - x2)")
        print(f"W postaci ogólnej: {self.a}x^2 + {self.b}x + {self.c}")
        print(
            f"W postaci kanonicznej: {self.a}(x - h)^2 + k, gdzie h = {-self.b / (2 * self.a)}, k = {self.c - (self.b ** 2) / (4 * self.a)}")

    def czy_nalezy(self, x, y):
        if self.a * x ** 2 + self.b * x + self.c == y:
            return f"Punkt ({x}, {y}) należy do funkcji kwadratowej"
        else:
            return f"Punkt ({x}, {y}) nie należy do funkcji kwadratowej"

    def monotonicznosc(self):
        if self.a > 0:
            return "Funkcja jest rosnąca"
        elif self.a < 0:
            return "Funkcja jest malejąca"
        else:
            return "Funkcja jest stała"

    def zbior_wartosci(self):
        if self.a > 0:
            return f"Zbiór wartości funkcji: [ {self.c - (self.b ** 2) / (4 * self.a)}, +∞ )"
        elif self.a < 0:
            return f"Zbiór wartości funkcji: ( -∞, {self.c - (self.b ** 2) / (4 * self.a)} ]"
        else:
            return f"Zbiór wartości funkcji: {self.c}"

    def kiedy_ujemne_dodatnie(self):
        if self.a > 0:
            return f"Funkcja przyjmuje wartości ujemne dla x < {-self.b / (2 * self.a)} i dodatnie dla x > {-self.b / (2 * self.a)}"
        elif self.a < 0:
            return f"Funkcja przyjmuje wartości ujemne dla x > {-self.b / (2 * self.a)} i dodatnie dla x < {-self.b / (2 * self.a)}"
        else:
            return f"Funkcja jest stała i nie zmienia znaku"


try:
    a = float(input("Podaj wartość parametru a: "))
    b = float(input("Podaj wartość parametru b: "))
    c = float(input("Podaj wartość parametru c: "))

    funkcja = FunkcjaKwadratowa(a, b, c)

    print(funkcja.Rozwiaz())
    funkcja.wypisz()
    x = float(input("Podaj wartość x punktu: "))
    y = float(input("Podaj wartość y punktu: "))
    print(funkcja.czy_nalezy(x, y))
    print(funkcja.monotonicznosc())
    print(funkcja.zbior_wartosci())
    print(funkcja.kiedy_ujemne_dodatnie())

except ValueError:
    print("Błąd: Wprowadzono niepoprawne dane.")
except ZeroDivisionError:
    print("Błąd: Dzielenie przez zero.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
