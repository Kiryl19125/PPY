# -*- coding: utf-8 -*-
# Napisz funkcje o nazwie calculate_statistics, która przyjmuje dowolną liczbę argumentów liczbowych oraz str określający typ operacji ("mean", "median" lub "mode")
# Funkcja ma obliczyć i zwrócić wynik wybranego działania
# Użyj funkcji match case

def calc_mean(numbers: list[int]) -> float:
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def calc_median(numbers: list[int]) -> float:
    n = len(numbers)
    s = sorted(numbers)
    return (s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2] if n else None


def calc_mode(numbers: list[int]) -> int:
    dictt = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for number in numbers:
        dictt[number] += 1

    max_key = max(dictt, key=lambda x: dictt[x])

    return dictt[max_key]


def calculate_statistics(operation, *args):
    # TWÓJ KOD
    match operation:
        case "mean":
            arr = []
            for n in args:
                arr.append(n)
            return calc_mean(arr)
        case "median":
            arr = []
            for n in args:
                arr.append(n)
            return calc_median(arr)
        case "mode":
            arr = []
            for n in args:
                arr.append(n)
            return calc_mode(arr)


# Przykładowe użycie funkcji
print(calculate_statistics("mean", 1, 2, 3, 4, 5))  # 3.0
print(calculate_statistics("median", 1, 2, 3, 4, 5))  # 3
print(calculate_statistics("mode", 1, 2, 2, 3, 3, 3))  # [3]
