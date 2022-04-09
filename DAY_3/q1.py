#! /usr/bin/python3

######################## Reverse a List Array  ######################



# using pre created method: reverse()
def method1():
    arr = [ 55, 66, 77, 88, 99]
    print(arr)

    print("array after reverse using method: ")
    arr.reverse()
    print(arr)


# Using reversed() Method
def method2():
    x = [ 5, 6, 7, 8, 9]
    print("Acrual List: ", x)
    y = list(reversed(x))
    print("after reverse: ", y)


# using slicing
def method1():
    b = [ 55, 66, 77, 88, 99]
    print("Acrual List: ", b)
    c = b[::-1]
    print("after reverse: ", c)





############################ Reversing a NumPy Array in Python  #################
import numpy as np


# using flip() of Numpy
def narr1():
    new_arr = np.array([1,2,3,4,5,6,7,8])
    print(new_arr)
    rev_arr = np.flip(new_arr)
    print(rev_arr)


narr1()


# using flipud() of Numpy (flip up down)
def narr2():
    new_arr = np.array(['a','b','c','d','e'])
    print(new_arr)
    rev_arr = np.flipud(new_arr)
    print(rev_arr)


narr2()


# using slicing

def narr3():
    new_arr = np.array([1,2,3,4,5,6,7,8])
    print(new_arr)
    rev_arr = new_arr[::-1]
    print(rev_arr)


narr3()