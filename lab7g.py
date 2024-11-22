#!/usr/bin/env python3
# Student ID: [seneca_id]

def function1():
    # This object 'a' is completely unrelated to the object 'a' in function2():
    a = 'object_function1'
    print('print() call in function1 on a:', a)

def function2():
    # This variable 'a' is completely unrelated to the variable 'a' in function1():
    a = 'object_function2'
    print('print() call in function2 on a:', a)

# Main script
a = 'object_in_main'
print('print() call in main on a:', a)
function1()
print('print() call in main on a:', a)
function2()
print('print() call in main on a:', a)
