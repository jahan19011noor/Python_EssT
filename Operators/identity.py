'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: identity

* Python built-in function id() returns a unique integer as identity of object. 
* Identity operators compare the memory locations of two objects.
* There are two Identity operators explained below:
    * is    ture if the variables on either side of the operator point to the same object
    * is not    false if the variables on either side of the operator point to the same object
'''

a, b = 10, 10

print("a = ", a, "has id = ", id(a), "\nb = ", b, "has id = ", id(b))

if a is b:
    print("a = ", a, " and b = ", b, " have same identity")

if id(a) == id(b):
    print("a = ", a, " and b = ", b, " have same identity")

print("id(a) = ", id(a), " and id(b) = ", id(b))

b = 20

if a is not b:
    print("a = ", a, " and b = ", b, " have different identity")
    
if id(a) != id(b):
    print("a = ", a, " and b = ", b, " have different identity")
    
print("id(a) = ", id(a), " and id(b) = ", id(b))