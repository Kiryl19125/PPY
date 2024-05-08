# -*- coding: utf-8 -*-
'''

Napisz definicje, która przeprowadzi analizę tekstu. Program powinien wykonać następujące czynności:
- Wczytać tekst
- Podzielić tekst na słowa.
- Usunąć znaki interpunkcyjne i zamienić wszystkie litery na małe litery.
- Utworzyć kolekcję słów i zliczyć ile razy każde słowo występuje w tekście.
- Wyświetlić 10 najczęściej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić 10 najrzadziej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić liczbę unikalnych słów w tekście.
- Wyświetlić średnią długość słowa w tekście.
'''


# from typing import Dict


def read_file(path: str) -> str:
    with open(path, "r") as file:
        data = file.read()
    return data


def divide_to_word(text: str) -> list[str]:
    return text.split()


def delete_signs_and_lowercase(data: list[str]) -> list[str]:
    znaki = [",", ".", ":", ";", "!", "?"]
    result = []
    for word in data:
        word = word.lower()
        for char in word:
            if char in znaki:
                word = word.replace(char, "")
        result.append(word)

    return result


def get_dict_of_words(data: list[str]) -> dict[str, int]:
    dictionary = {}
    for word in data:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    return dictionary


def calc_everage_word_length(data: dict[str, int]) -> float:
    devision = len(data)
    sum = 0
    for word in data:
        sum += len(word)
    return sum / devision


if __name__ == '__main__':
    text = read_file("../lec_3/Z2_txt.txt")
    data = divide_to_word(text)
    data = delete_signs_and_lowercase(data)
    dictionary = get_dict_of_words(data)

    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])

    # print(dictionary)
    # print(sorted_dict)

    print("Najczęsciej spotykane słowa")
    print(sorted_dict[-10:])

    print("Najrzadziej spotykane słowa")
    print(sorted_dict[:10])

    print(f"Liczba unikalnych słów: {len(dictionary)}")

    print(f"Srednia dłógość słow: {calc_everage_word_length(dictionary)}")
