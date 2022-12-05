#!/usr/bin/python3
def no_c(my_string):
    newstring= ""
    for i in range(len(my_string)):
        if my_string[i] == 'c':
            continue
        newstring+=my_string[i]
    return newstring
