'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: sets

* If we pass a tuple with reappearing elements to the set function
    * no doublets will be seen in the resulting set: 
'''

cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print(cities)

'''
* Sets are implemented in a way, which doesn't allow mutable objects.
* The following example demonstrates that we cannot include for example lists as elements:
'''

cities1 = set((("Python","Perl"), ("Paris", "Berlin", "London")))
print(cities1)

'''
* Lists provided as set elements gives error
    * unhashable type - list
* Tuples provided as set elements accepted
    * tuples are immutable as so are hashable
'''
# cities2 = set((["Python","Perl"], ["Paris", "Berlin", "London"]))

# print("{}\n{}".format(cities1, cities2))


