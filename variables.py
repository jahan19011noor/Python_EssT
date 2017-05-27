'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: variables
'''
# integer value assignment
a = 0
b = 4
print(a+b)

# string value assignment
a = "2"
b = "4"
print(a+b)

# typecasting from string to integer
a = 0
b = "4"
# print(a+b)        error
print(a+int(b))

# multiple variable assignment and printing
a, b, c = 2, 5.6, "new_string"
print("The value of a = {}\nThe value of b = {}\nThe value of c = {}".format(a,b,c))