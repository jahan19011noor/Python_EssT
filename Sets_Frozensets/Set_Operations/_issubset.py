'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: issubset()

* x.issubset(y) returns True
    * if x is a subset of y.
* "<=" is an abbreviation for "Subset of"
* and ">=" for "superset of" 
* "<" is used to check if a set is a proper subset of a set.
'''
x = {"a","b","c","d","e"}
y = {"c","d"}
print(x.issubset(y))
print(x < y)
print(y.issubset(x))
print(y < x)
print(x < x)                # a set can never be a proper subset of oneself.
print(x <= x )
