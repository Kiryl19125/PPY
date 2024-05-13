# -*- coding: utf-8 -*-
'''
- Napisz klasę Kwadrat, Trójkąt, które są subklasami klasy Wielokąt
- Klasa Wielokąt ma zawierać  
    -Metodę askNSides(), która pyta użytkownika o ilość boków wielokąta (która się przyda tylko, gdy wywołamy obiekt poprzez klasę Wielokąt)
    -Metode inputSides(), która przyjmuje (od użytkownika przez input) wielkość każdego boku
    -Metode dispSides(), która wyświetla długości boków
    -Metode circuit(), która wyświetla obwód
    
- Klasa Trójkąt ma zwierać:
    -Zainicjowanie liczby boków trójkąta do 3 przez wywołanie metody __init__ klasy Polygon
    -Metode area(), która liczy pole, o wskazanych przez użytkownika długościach
    -Metoda isright(), która sprawdza czy trójkąt jest prostkątny
    
- Klasa Kwadrat ma zwierać:
    -Zainicjowanie liczby boków kwadratu do odpowiednio 1 przez wywołanie metody __init__ klasy Polygon
    -Metode area(), która liczy pole, o wskazanych przez użytkownika długościach
'''

from typing import List, override
import math


class Poligon:

    def __init__(self, sides: int) -> None:
        self.sizes = []
        self.__askNSides(sides)

    def __askNSides(self, sides):
        for _ in range(sides):
            self.sizes.append(self.__inputSides())
        # print(self.__sizes)

    def __inputSides(self) -> int:
        size = int(input("Podaj rozmiar boku: "))
        return size

    def dispSides(self):
        for i in range(len(self.sizes)):
            print(f"side # {i+1}, size = {self.sizes[i]}")

    def circuit(self):
        print(f"obwod = {sum(self.sizes)}")


class Triangle(Poligon):
    
    def __init__(self) -> None:
        super().__init__(3)


    def area(self) -> float:
        s: float = sum(self.sizes) / 2
        area: float = math.sqrt(s * ( s - self.sizes[0]) * (s - self.sizes[1]) * (s - self.sizes[2] ) )
        return area



    def isRight(self) -> bool:
        check_1 = self.sizes[0]**2 + self.sizes[1]**2 == self.sizes[2]
        check_2 = self.sizes[0]**2 + self.sizes[2]**2 == self.sizes[1]
        check_3 = self.sizes[2]**2 + self.sizes[1]**2 == self.sizes[0]
        return check_1 or check_2 or check_3


class Rectangle(Poligon):

    def __init__(self) -> None:
        super().__init__(1)


    def area(self) -> int:
        return self.sizes[0] ** 2

if __name__ == "__main__":

    trianle = Triangle()
    trianle.dispSides()
    # print(trianle.__sizes)
    aria = trianle.area()
    print(aria)
    print(trianle.isRight())




    











