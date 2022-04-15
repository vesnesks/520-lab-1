# python_intro.py

""".Python Essentials: Introduction to Python.
Sarah Vesneske
MTH 520
April 2022
This file was created for the first assignment of Python Essentials. Problem two for this lab gives instructions to find or create this file.
"""

print("Hello, world!")

import numpy as np

sphere_constant = 4/3
pi = 3.14159
def sphere_volume(r):
    return sphere_constant * pi * r**3

def prob4():
    A = np.array([ [3,-1,4],[1,5,-9] ])
    B = np.array([ [2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3] ])
    return np.dot(A,B)


def calories(food):
    if food == "apple":
        return("72 calories")
    elif food == "banana" or food == "carrot":
        return("105 calories")
    else:
        return("calorie count unavailable")

def tax_liability(income):
    if income <= 9875:
        return income * 0.1
    elif income <= 40125:
        return (income - 9875) * 0.12 + 9875*0.1
    else:
        return (income - 40125) * 0.22 + (40125-9875) * 0.12 + 9875*0.1

def prob6a():
    A = list(range(1,8))
    B = [5]*7
    print A
    print B
    P = [0]*7
    S = [0]*7
    F = [0]*7
    for i in range(7):
        P[i]=A[i]*B[i]
        S[i]=A[i]+B[i]
        F[i]=5*A[i]
    return P,S,F

def prob6b():
    A = np.array([1,2,3,4,5,6,7])
    B = np.array([5,5,5,5,5,5,5])
    return A*B, A+B, 5*A 
 


if __name__ == '__main__':
    print("This is printed if the module is run as a script")
    print(sphere_volume(10))
    print(prob4())
    print(calories("banana"))
    print(tax_liability(63000))
    print(prob6a())
    print(prob6b())

