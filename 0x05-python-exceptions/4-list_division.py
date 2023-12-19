#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i] if i < len(my_list_1) else 0
            val2 = my_list_2[i] if i < len(my_list_2) else 0
            if not isinstance(val1, (int, float))
            or not isinstance(val2, (int, float)):
                raise TypeError("wrong type")
            if val2 == 0:
                raise ZeroDivisionError("division by 0")
            division = val1 / val2
            result.append(division)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
