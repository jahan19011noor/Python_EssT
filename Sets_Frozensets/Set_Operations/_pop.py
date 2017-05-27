'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: pop()

* pop() removes and returns an arbitrary set element.
* The method raises a KeyError if the set is empty
'''
x = {"a","b","c","d","e"}
print(x.pop())
print(x.pop())

x = {}
# print(x.pop())            # This gives an error as the set is empty 