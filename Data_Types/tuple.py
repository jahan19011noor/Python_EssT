'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: tuple

* A tuple is another sequence data type that is similar to the list.
* A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.
* The main differences between lists and tuples are:
        * Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed
        * tuples are enclosed in parentheses ( ( ) ) and cannot be updated.
* Tuples can be thought of as read-only lists.

'''
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
# tuple[0] = "askskhk"    # No updates allowed; this line will give an error
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 3)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple
