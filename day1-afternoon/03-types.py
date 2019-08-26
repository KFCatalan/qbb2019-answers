#!/usr/bin/env python3


an_int = 42
a_float = 42.0
a_string = "42"

# Boolean
truthy = True
falsish = False

#Lists

#By **convention** lists are homogenupus and tuples homogenuous


a_list = [5, 10, 15, 20]

a_tuple = (1, True, "Seven", False)


#another_list = a_list
another_list = list(a_list)
a_list [3] = 4000

#print(a_list)
#print(another_list)


for value in an_int, a_float, a_string, a_list, a_tuple:
    print(value, type(value))
    