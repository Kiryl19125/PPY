# napisz program, który zwróci wszystkie liczby pierwsze dla wybranego zakresu
# Podpowiedź - znajdź warunki, które eliminują kryteria liczby pierwszej.
start = 25
end = 55
print("Liczby pierwsze pomiędzy", start, "i", end, "to:")


def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(start, end):
        if czy_pierwsza(i):
            print(i)
