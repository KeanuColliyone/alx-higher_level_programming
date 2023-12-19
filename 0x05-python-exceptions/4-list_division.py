#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val_1 = float(my_list_1[i])
                    if isinstance(my_list_1[i], (int, float))
                    else "wrong type"
            val_2 = float(my_list_2[i])
                    if isinstance(my_list_2[i], (int, float))
                    else "wrong type"

            try:
                division = val_1 / val_2 if val_2 != 0 else "division by 0"
            except ZeroDivisionError:
                division = "division by 0"

        except IndexError:
            division = "out of range"

        finally:
            if division == "wrong type":
                print("wrong type")
            elif division == "division by 0":
                print("division by 0")
            elif division == "out of range":
                print("out of range")
            else:
                result.append(division)

    return result
