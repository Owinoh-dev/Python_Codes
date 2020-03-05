# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:07:00 2020

@author: pc-owinoh
"""
num = int(input("Enter the Number :"))

fact = 1

if num < 0:
    print("Factorial of negative number is not defined")
else:
    for i in range(1,num+1):
        fact *= i
    print("Factorial of {} is {}".format(num, fact))
    
    #The same program can be implemented using a while loop as follows,
    num = int(input("Enter the Number :"))

fact = 1
i = 1

if num < 0:
    print("Factorial of negative number is not defined")
else:
    while(i<=num):
        fact *= i
        i += 1
    print("Factorial of {} is {}".format(num, fact))

#Since Python always has a better way of doing things, 
#it comes with a built-in solution for computing factorial of a number.

from math import factorial

num = int(input("Enter the Number :"))

fact = factorial(num)

if num < 0:
    print("Factorial of negative number is not defined")
else:
    print("Factorial of {} is {}".format(num, fact))