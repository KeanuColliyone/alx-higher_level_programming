#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val_1 = my_list_1[i] if i < len(my_list_1) else 0
            val_2 = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(val_1, (int, float)) and isinstance(val_2, (int, float)):
                if val_2 == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(val_1 / val_2)
            else:
                raise TypeError("wrong type")

        except ZeroDivisionError as e:
            print(e)
            result.append(0)
        except TypeError as e:
            print(e)
            result.append(0)
        except IndexError as e:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result

# Test cases
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
