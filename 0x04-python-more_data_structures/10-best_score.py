#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        best_key = [key for key, value in a_dictionary.items()
                if value == max_value][0]
        return best_key
    return None
