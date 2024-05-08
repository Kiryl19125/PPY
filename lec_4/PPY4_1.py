# -*- coding: utf-8 -*-
#Napisz funkcje silnii używając rekurencji


def silnia_rec(number: int):
    if number > 1:
        return number * silnia_rec(number-1)
    else:
        return 1


if __name__ == '__main__':
    print(silnia_rec(3))
