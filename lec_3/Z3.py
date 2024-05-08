# -*- coding: utf-8 -*-
"""
Napisz program, który umożliwia zarządzanie książką adresową. Program powinien umożliwiać użytkownikowi wykonywanie następujących operacji:

Dodawanie nowego kontaktu do książki adresowej.
Wyświetlanie wszystkich kontaktów z książki adresowej.
Wyszukiwanie kontaktu po nazwie.
Usuwanie kontaktu z książki adresowej.

Użyj słownika, gdzie kluczem będzie nazwa kontaktu, a wartością będzie lista informacji o kontakcie (np. imię, nazwisko, numer telefonu).
"""


class Contact:

    def __init__(self, name: str, surname: str, phone_number: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __repr__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Phone: {self.phone_number}"


class PhoneBook:

    def __init__(self):
        self.phone_book = {}

    def add_contact(self, contact: Contact):
        self.phone_book[contact.name.lower()] = contact

    def show_contact(self):
        for contact in self.phone_book:
            print(contact)

    def find_contact(self, name: str):
        assert name.lower() in self.phone_book
        print(self.phone_book.get(name.lower()))

    def remove_contact(self, name: str):
        assert name.lower() in self.phone_book
        self.phone_book.pop(name.lower())


my_phone_book = PhoneBook()
next = True

if __name__ == '__main__':

    while next:
        user_input = input("Podak komende: ")
        if user_input == "add":
            name = input("Podaj imie: ")
            surname = input("Podaj nazwisko: ")
            phone = input("Podaj numer: ")
            my_phone_book.add_contact(Contact(name, surname, phone))
        elif user_input == "delete":
            name = input("Podaj imie: ")
            my_phone_book.remove_contact(name)
        elif user_input == "show":
            my_phone_book.show_contact()
        elif user_input == "find":
            name = input("Podaj imie: ")
            my_phone_book.find_contact(name)
        elif user_input == "exit":
            next = False
        else:
            print("unknown commend")
