'''
Created on Oct 21, 2016

@author: Noor Jahan Mukammel

Program: dictionary

* Python's dictionaries are kind of hash table type.
* They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
* A dictionary key can be almost any Python type, but are usually numbers or strings. 
* Values, on the other hand, can be any arbitrary Python object.
* Dictionaries are enclosed by curly braces ({ })
* values can be assigned and accessed using square braces ([]).
* The keys can be accessed by .keys() method
* The values can be accessed by .values() method
* Dictionaries have no concept of order among elements.
        * It is incorrect to say that the elements are "out of order";
        * they are simply unordered.

'''
dic = {}
dic['one'] = 1
dic['2'] = "two"
dic[3] = 3.333
dic[5] = 110

newdic = {'a': 'first', 'b': 2, 3: 2.41, 3.44: '110'}

print(dic)
print(dic['one'])
print(dic['2'])
print(dic[3])
print(newdic)
# print(dic+newdic)        You cannot add dictionaries like list and tuple
print(dic.keys())
print(newdic.values())

