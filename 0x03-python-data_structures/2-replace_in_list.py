#!/usr/bin/python3

# function that replaces an element of a list at a specific position

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    length = len(my_list)

    if idx > lenghth - 1:
        return (my_list)

    my_list[idx] = element

    return (my_list)

   