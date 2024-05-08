# -*- coding: utf-8 -*-

''''
Zmodyfikuj funkcje kalkulator tak, żeby uwzględniała te błędy:
TypeError: Jeżli args nie zawiera liczb lub kwargs nie zawiera znaków
ZeroDivisionError
IndexError: Jeśli ilość kwargs jest równa lub większa niż args
MyError(zdefiniowany przez Ciebie): Jeśli znak jest inny niż +-*/ wyświetl komunikat o niepoprawnym znaku
'''


class InvalidOperatorException(Exception):
    pass


def kalkulator(*args, **kwargs):
    result = args[0]
    temp_liczba=args[1]

    values = kwargs.values()

    if not all(isinstance(v, int) for v in args):
        raise TypeError

    if not all(isinstance(v, str) for v in values):
        raise TypeError

    if len(kwargs) >= len(args):
        raise IndexError


    for index, dzialanie in enumerate(values):
        match dzialanie:
          case '+':
            result+=args[index+1]
          case '-':
            result-=args[index+1]
          case '*':
            result*=args[index+1]
          case '/':
            try:
                result/=args[index+1]
            except ZeroDivisionError:
                print("Nie mozna dzielic przez zero")
                exit()
          case _:
              raise InvalidOperatorException("Jakis dziwny operator")
    return result

print(kalkulator(1,3,0, działanie_1='+',działanie_2="/"))




