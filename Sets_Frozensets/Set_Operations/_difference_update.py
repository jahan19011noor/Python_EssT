'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: difference_update()

* The method difference_update removes all elements of another set from this set. 
* x.difference_update(y) is the same as "x = x - y"
'''
x = {"a","b","c","d","e"}
y = {"b","c"}
print(x.difference_update(y))       # difference_update() function returns "None"
print(x)                            # prints the updated set() x

x = {"a","b","c","d","e"}
y = {"b","c"}
x = x-y                             # assigns the new set resulting from x-y into x
print(x)                            # prints the new set x