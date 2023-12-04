#!/usr/bin/python3
def max_integer(my_list=[]):
    len1 = len(my_list)

    if len1 == 0:
        return (None)
    max_int = my_list[0]

    for i in range(1, len1):
        if my_list[i] > max_int:
            max_int = my_list[i]

    return (max_int)
