#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    text (str): Text input.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_sentence = ['.', '?', ':']
    start = 0
    for i, char in enumerate(text):
        if char in end_sentence:
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    if start < len(text):
        print(text[start:].strip())
