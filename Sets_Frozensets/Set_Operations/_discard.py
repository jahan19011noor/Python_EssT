'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: discard(el)

* An element el will be removed from the set, if it is contained in the set.
* If el is not a member of the set, nothing will be done.
'''
x = {"a", "2", "4.5", "ab3", "aksk.22"}
print(x.discard("a"))                   # difference_update() function returns "None"
print(x)                                # prints the updated set() x with "a" removed
print(x.discard("x"))                   # difference_update() function returns "None"
print(x)                                # If el is not a member of the set, nothing will be done.