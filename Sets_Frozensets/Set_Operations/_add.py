'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: add()

* Method: add(element)
    *A method which adds an element, which has to be immutable, to a set.
    * Of course, an element will only be added,
        * if it is not already contained in the set.
        * If it is already contained, the method call has no effect.
'''

# colors = set(["red", "green"])    or
colors = {"red", "green"}
colors.add("pink")
print(colors)

'''
colors.add(["blue","white","yellow", "bloack"])
print(colors)

This gives an error as the list is mutable and thus cannot be added to set - immutable
'''