'''
Created on Jan 7, 2017

@author: Jahan
'''
def optionalParameter(arg3, arg1 = "Name", arg2 = "Hi"):
    print(arg2+" "+arg1)
    print(arg3)
    
optionalParameter(arg3="111")

def my_function(**kwargs):
    print(kwargs)
my_function(a=12, b="abc")
