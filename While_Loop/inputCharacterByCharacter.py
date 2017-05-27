'''
Created on Jan 4, 2017

@author: Jahan
'''
import sys 

text = ""
while 1:
    c = sys.stdin.read(1)
    text = text + c
    if c == '\n':
        break

print("Input: %s" % text)
