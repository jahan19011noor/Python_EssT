'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: remove(el)

* works like discard()
    * but if el is not a member of the set
        * a KeyError will be raised.
'''

x = {"a","b","c","d","e"}
print(x.remove("a"))          # difference_update() function returns "None"
print(x)
# x.remove("z")               # This gives an error because "z" is not an element of set x