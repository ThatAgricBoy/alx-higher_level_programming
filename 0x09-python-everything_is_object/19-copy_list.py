#!/usr/bin/python3

def copy_list(l):
    # Use slicing to create a shallow copy of the input list
    # The [:] notation specifies a slice that includes all elements of the list from the beginning to the end
    # This effectively creates a new list with the same elements as the original list
    return l[:]

