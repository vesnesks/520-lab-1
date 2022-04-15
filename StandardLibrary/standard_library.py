# standard_library.py
"""Python Essentials: The Standard Library.
Sarah Vesneske
MTH520 Gibson
April 15, 2022
"""

import calculator as cc
from itertools import combinations

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return min(L), max(L), (sum(L)/len(L))


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    my_number = 10
    my_other_number = my_number
    my_other_number = 8
    #return my_number == my_other_number
    my_string = "aeiou"
    my_other_string = my_string
    my_other_string = "aeiouy"
    #return my_string == my_other_string
    my_list = list(range(10))
    my_other_list = my_list
    my_other_list = list(range(5))
    #return my_list == my_other_list
    my_tuple = (0,0,0)
    my_other_tuple = my_tuple
    my_other_tuple = (1,1,1)
    #return my_tuple == my_other_tuple 
    my_set = {"red","yellow","blue"}
    my_other_set = my_set
    my_other_set = {"red", "green", "blue"}
    return my_number == my_other_number, my_string == my_other_string, my_list == my_other_list, my_tuple == my_other_tuple, my_set == my_other_set


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.
    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return cc.sqrt(cc.sum(cc.product(a,a),cc.product(b,b)))


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.
    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.
    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    for i in range(len(A)+1):
        print(list(combinations(A,i)))



# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")


if __name__ == "__main__":
    print(prob1(list(range(1,10))))
    print(prob2())
    print(hypot(3, 4))
    print(power_set(["red","yellow","blue"]))


