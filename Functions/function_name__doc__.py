'''
Created on Jan 7, 2017

@author: Jahan
'''
def Hello(name="everybody"):
    string1 = "test string"
    """                     very new docstring              nnn"""
    print("Hello " + name + "!")

print("The docstring of the function Hello: " + Hello.__doc__)
