#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max = ""
    ma = 0
    for k, v in a_dictionary.items():
        if v > ma:
            ma = v
            max = k
    return max
