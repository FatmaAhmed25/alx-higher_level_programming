#!/usr/bin/python3
def no_c(my_string):
    s1 = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            s1 += my_string[i]
    return s1
