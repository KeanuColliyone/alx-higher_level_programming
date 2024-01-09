#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)


nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
