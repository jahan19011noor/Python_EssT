'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: if_else
'''
a, b = 8, 6

if a<b:
    print("this is the if block")
    print("a = {} is smaller than b = {}".format(a, b))
else:
    print("this is the else block")
    print("a = {} is greater than b = {}".format(a, b))


a, b = 8, 8
if a<b:
    print("this is the if block")
    print("a = {} is smaller than b = {}".format(a, b))
elif a==b:
    print("this is the else-if block")
    print("a = {} is equal to b = {}".format(a, b))
else:
    print("this is the else block")
    print("a = {} is greater than b = {}".format(a, b))