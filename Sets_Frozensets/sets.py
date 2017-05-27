'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: sets

* A set contains an unordered collection of unique and immutable objects.
    * Each object as a whole must not be mutable
    * The elements associated with the objects might be mutable
* So, set cannot contain immutable objects but itself is mutable
* The function set() accepts only one argument
* The set data type is, as the name implies, a Python implementation of the sets as they are known from mathematics.
* This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.

* To create a set call the built-in set() function with a sequence or another iterable object
    * Common formula:        set([iterable])
        * Where the iterable = list, tuple, dictionary or string
* In case of any of the iterable objects
    * each of the individual elements
    * are represented as a separate member of the set

'''
x = set("A Python Tutorial")
y = set((1, 2, 3, 4, 5))
z = set([1, 2, 3, 4, 5])
d = set({1: 'a', 2: 'b', 'c': 55})
print("{}\n{}\n{}\n{}".format(x, y, z, d))
print(type(y))

