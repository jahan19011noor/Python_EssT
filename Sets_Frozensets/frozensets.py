'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: frozensets

* Though sets can't contain mutable objects, sets are mutable: 
'''
cities = set(["Frank", "fasel", "Freiburg"])
cities.add("Strasbourg")
print(cities)


'''
* Frozensets are like sets except that they cannot be changed
* i.e. they are immutable:
'''
cities = frozenset(["Frank", "fasel", "Freiburg"])
# cities.add("Strasbourg")        # this line produces an error as frozenset cannot take in any more data
print(cities)

'''
* We can define sets (since Python2.6) without using the built-in set function.
* We can use curly braces instead:
'''
adjectives = {"cheap","expensive","inexpensive","economical"}
print(adjectives)