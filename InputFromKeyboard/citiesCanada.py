'''
Created on Jan 3, 2017

@author: Jahan
'''
cities_canada = input("Largest cities in Canada: ")
print(cities_canada, type(cities_canada))
print(cities_canada)

cities_canada = eval(input("Largest cities in Canada: "))
'''# input: ["Toronto", "Montreal", "Calgara", "Ottawa"]'''
print(cities_canada, type(cities_canada))
'''# eval automatically casts to list as the input is given in list format.'''

cities_canada = eval(input("Largest cities in Canada: "))
'''# input: ("Toronto", "Montreal", "Calgara", "Ottawa")'''
print(cities_canada, type(cities_canada))
'''# eval automatically casts to tuple as the input is given in tuple format.'''

cities_canada = eval(input("Largest cities in Canada: "))
'''# input: {'Toronto': 2615060, 'Ottawa': 883391, 'Los Angeles': 3792621, 'Chicago': 2695598}'''
print(cities_canada, type(cities_canada))
'''# eval automatically casts to dictionary as the input is given in dictionary format.'''

population = input("Population of Toronto? ")
print(population, type(population))

population = int(input("Population of Toronto? "))
print(population, type(population))