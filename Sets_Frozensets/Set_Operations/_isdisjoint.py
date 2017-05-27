'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: isdisjoint()

* This method returns True if two sets have a null intersection.
'''
x = {"a","b","c"}
y = {"c","d","e"}
print(x.isdisjoint(y))

x = {"a","b","c"}
y = {"d","e","f"}
print(x.isdisjoint(y))
