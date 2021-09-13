#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    is_pair = True
    if len(str) % 2 == 0:
        is_pair = True
    else:
        is_pair = False
    return is_pair


def remove_third_char(string: str) -> str:
    new_string = str[0:3:] + str[4::]
    return new_string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return str.replace(old_char, new_char)


def get_nb_char(string: str, char: chr) -> int:
    counter = 0
    for letter in str:
        if letter == chr:
            counter += 1
    return counter


def get_nb_words(sentence: str) -> int:
    counter = 1
    for letter in str:
        if letter == "":
            counter += 1
    return counter


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
