"""
A. 
napisz program, którego wynik będzie jak poniżej
Podpowiedź: argumenty, które przyjmuje funkcja range to (start, stop, step)
step przyjmuje domyślnie wartość 1
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""

"""
B. 
Rozszerz powyzszy kod o warunki i dostosuj go do ponieszego wzoru:
11 # 9 -8 7 -6 # -4 3 -2 1 
# 9 -8 7 -6 # -4 3 -2 1 
9 -8 7 -6 # -4 3 -2 1 
-8 7 -6 # -4 3 -2 1 
7 -6 # -4 3 -2 1 
-6 # -4 3 -2 1 
# -4 3 -2 1 
-4 3 -2 1 
3 -2 1 
-2 1 
1 
"""

if __name__ == '__main__':
    number: int = int(input("Podaj liczbe: "))

    while number != 0:

        for i in range(number, 0, -1):
            if i % 5 == 0:
                print("#", end=" ")
            elif i % 2 == 0:
                print(f"{i*-1}", end=" ")
            else:
                print(i, end=" ")
        print()
        number -= 1
