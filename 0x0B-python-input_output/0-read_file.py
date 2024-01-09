#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


read_file("my_file_0.txt")
