'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: difference()

* This method returns the difference of two or more sets as a new set.
'''

x = {"a", "b", "c", "d", "e"}
y = {"b", "x", "p", "e"}
z = {"b", "p", "e", "d"}

print(x.difference(y))
print(x.difference(y).difference(z))

'''
* Instead of using the method difference, we can use the operator "-":
'''
print(x-y)
print(x-y-z)