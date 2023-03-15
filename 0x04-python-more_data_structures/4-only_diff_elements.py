#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only_set_1 = set_1.difference(set_2)
    only_set_2 = set_2.difference(set_1)
    only_diff = only_set_1.union(only_set_2)
    return only_diff
