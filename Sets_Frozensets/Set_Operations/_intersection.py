'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: intersection(s)

* Returns the intersection of the instance set and the set s as a new set.
* In other words:
    * A set with all the elements
    * which are contained in both sets is returned.
'''

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
print(x.intersection(y))    # Returns the intersection set of both sets

'''
* This can be abbreviated with the ampersand operator "&":
'''
print(x  & y)