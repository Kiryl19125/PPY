# -*- coding: utf-8 -*-

'''
Napisz funkcję slowa_podobne(s, words), która wyświetli słowa, które są ,,podobne" do napisu s
w tym sensie, że składające się z tych samych znaków — ale ewentualnie występujących inną liczbę razy
#PRZYKŁAD
slowa_podobne('one', ['one', 'two', 'none', 'three', 'neon', 'eon']) 
>> none neon eon
'''


def slowa_podobne(s: str, worlds: list[str]) -> None:
    for w in worlds:
        if set(s) == set(w) and w != s:
            print(w)


if __name__ == '__main__':
    slowa_podobne('one', ['one', 'two', 'none', 'three', 'neon', 'eon'])
