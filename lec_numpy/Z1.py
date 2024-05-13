# -*- coding: utf-8 -*-
"""
- Wczytaj danych i wyświetl kilka pierwszych wierszy, aby zapoznać się ze strukturą danych.
  Sprawdź liczby wierszy i kolumn w zbiorze danych.
- Usuń pingwiny z brakami danych i dodaj nową kolumnę, gdzie każdemu pingwinowi przypiszemy liczbę gdzie 1 to pingwin o największej masie (0,25)
- Oblicz średnią i odchylenie standardowe z cech fizycznych pingwinów (wszystkich i dla każdego z gatanku). (0,5)
- Zwizualizuj dane za pomocą histogramu przedstawiającego rozkład mas pingwinów oraz boxplot prezentującego rozkład mas w zależności od gatunku pingwinów. (0,5)
- Utwórz nowy dataset który zwiera tylko pingwiny z masą nie wiekszą niż 3 odchelnia standardowe od średniej (0,25)
- Zobrazuj zależność między "flipper_length_mm" i "bill_length_mm" za pomocą scatter plotu (uwzględnij gatunek) (0,5)

import seaborn as sns
#Wczytanie danych
pingwiny = sns.load_dataset("penguins")
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pingwiny = sns.load_dataset("penguins") # czytam dane

print(pingwiny.head()) # wyswietlam kilka kolumn

print(pingwiny.describe())

# Usunięcie wierszy z brakującymi danymi
pingwiny = pingwiny.dropna()

# Sortowanie pingwinów według masy malejąco
pingwiny = pingwiny.sort_values(by='body_mass_g', ascending=False)

# Dodanie nowej kolumny z numerem pingwina
pingwiny['numer_pingwina'] = range(1, len(pingwiny) + 1)

# Wyświetlenie kilku pierwszych wierszy
print(pingwiny.head())


# Średnia i odchylenie standardowe dla wszystkich cech fizycznych
# srednia_all = pingwiny.mean()
# odchylenie_all = pingwiny.std()
# print(f"srednia all {srednia_all}")
# print(f"odchylenie all {odchylenie_all}")
