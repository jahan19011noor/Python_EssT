'''
Created on Jan 8, 2017

@author: Jahan
'''
def f(**kwargs):
    print(kwargs)
 
f()
# {}
f(de="German",en="English",fr="French")
# {'fr': 'French', 'de': 'German', 'en': 'English'}
