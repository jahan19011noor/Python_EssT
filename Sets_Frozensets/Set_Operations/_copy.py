'''
Created on Oct 24, 2016

@author: Noor Jahan Mukammel

Program: set_method: copy()

* copy() - Creates a shallow copy, which is returned.
'''

more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup)

more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities
more_cities.clear()
print(cities_backup)        #This prints out "set()"

'''
* The assignment "cities_backup = more_cities" just creates a pointer
* i.e. another name, to the same data structure.
'''