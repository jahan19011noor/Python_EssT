'''
Created on Jan 8, 2017

@author: Jahan
'''
def f():
    print(s)
s = "Python"
f()

def g():
    s = "Perl"
    print(s)

s = "Python"
g()
print(s)

def h():
    print(s)
    s = "Perl"
    print(s)

s = "Python"
h()
print(s)
