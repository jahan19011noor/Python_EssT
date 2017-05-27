'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: issuperset()

* x.issuperset(y) returns True, if
    * x is a superset of y.
* ">=" is an abbreviation for "issuperset of" 
* ">" is used to check if a set is a proper superset of a set.
'''
x = {"a","b","c","d","e"}
y = {"c","d"}
print(x.issuperset(y))
print(x > y)
print(x >= y)
print(x >= x)
print(x > x)
print(x.issuperset(x))
