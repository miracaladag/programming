# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 01:19:11 2020

@author: mirac
"""
import math
def isprime(n):
    var1 = True
    limit = int(math.sqrt(n)) + 1
    if n == 1:
        return False
    elif n == 2:
        return True
    
    for i in range(2,limit+1):
        if n % i == 0:
            var1 = False
            return var1
        
    return var1

def summation(n2):
    result = 0
    for i in range(1,n2 + 1):
        if isprime(i):
            result += i
        
    return result

myvalue = int(input("Number:  "))
print(summation(myvalue))