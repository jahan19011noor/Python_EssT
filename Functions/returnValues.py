'''
Created on Jan 7, 2017

@author: Jahan
'''
def no_return(x,y):
    c = x + y

res = no_return(4,5)
print(res)

def empty_return(x,y):
    c = x + y
    return

res = empty_return(4,5)
print(res)

def return_sum(x,y):
    c = x + y
    return c

res = return_sum(4,5)
print(res)
