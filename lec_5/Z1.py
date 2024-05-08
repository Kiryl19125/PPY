# -*- coding: utf-8 -*-
import os
from datetime import date



'''
1. Utwórz katalog o nazwie zajecia
2. Do pliku dzis.txt zapisz dzisiejszą datę
3. Przenieść plik dzis.txt do katalogu zajecia
4. Utworz listę integerow z w zakresie 1-15.
5. Do pliku liczby.txt w katalogu zajecia zapisz liczby z utworzonej listy, ale tak, aby każdy był w nowej linijce. Upewnij się, że dane nie zostały nadpisane.
6. Do pliku liczby_parzyste.txt zapisz liczby parzyste z utworzonej wcześniej listy, a do pliku liczby_nieparzyste.txt zapisz liczby nieparzyste z tej listy.
7. Wszystkie te pliki z polecenia 6 umieść w katalogu zajecia albo przy tworzeniu albo po zapisaniu do nich.
8. Wyświetl zawartość katalogu zajecia
'''

#wynikiem ma być ["dzis.txt", "liczby.txt", "liczby_nieparzyste.txt", "liczby_parzyste.txt]
today = date.today()

if __name__ == "__main__":

    os.makedirs("zajecia")
    with open("dzis.txt", "w") as file:
        file.write(today.strftime("%d-%m-%Y"))

    os.rename("dzis.txt", "zajecia/dzis.txt")

    list_int: list[int] = [num for num in range(1,16)]
    
    with open("zajecia/liczby.txt", "a") as file:
        for num in list_int:
            file.write(str(f"{num}\n"))

    with open("zajecia/liczby_parzyste.txt", "a") as file_parzyste:
        for num in list_int:
            if num % 2 == 0:
                file_parzyste.write(f"{num}\n")


    with open("zajecia/liczby_nieparzyste.txt", "a") as file_nieparzyste:
        for num in list_int:
            if num % 2 == 1:
                file_nieparzyste.write(f"{num}\n")

    list_dir = os.listdir("zajecia")
    for file in list_dir:
        print(file)







