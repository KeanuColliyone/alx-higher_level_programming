#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
        return num_chars_written


nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
