'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: membership
'''
a, b, c = 10, 20, 30

list_a = [1, 5, 10, 15, 20, 25]

if a in list_a:
    print("a = ", a, " is in list_a", list_a)
else:
    print("a = ", a, " is not found")

if c not in list_a:
    print("c = ", c, " is not in list_a", list_a)