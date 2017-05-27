'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: list

* A list contains items separated by commas and enclosed within square brackets ([]).
* To some extent, lists are similar to arrays in C.
* One difference between them is that all the items belonging to a list can be of different data type.

'''
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
list[0] = "aksksk"
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
