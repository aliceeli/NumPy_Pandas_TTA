#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:09:17 2020

@author: alicehoyle
"""

import numpy as np

# Create 1D array of numbers 0-9
array1 = np.array([0,1,2,3,4,5,6,7,8,9])
print("1D array: ", array1)
print()

#Create a 3x3 array of all Trues
array_true = np.ones((3,3))
print("""2D array: 
""", array_true == 1)
print()

#Extract odd numbers from array 1-10
array2 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Evens array: ", array2[1:10:2])
print()

#Subract 1 from each of the numbers in the above array
print("Array -1: ", array2 - 1)
print()

#Covert a 1D array to a 2d array with 2 rows
new_array = array1.reshape(2,5)
print("""1D -> 2D: 
""", new_array)
print()

#Create 2 arrays a, b stack them vertically using np.dot and np.sum to cal tot
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

vstack = np.vstack([a,b])
hstack = np.hstack([a,b])

c = np.dot(a,b)
d = np.sum(a+b)
print(f"n.dot = {c}, n.sum = {d}")
print()

#Create the following array without hardcoding. Use only numpy func
#and the below input array #>array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3])
a = np.ones(3)
b = np.array([1,2,3])

stack = np.hstack([a,a+1,a+2,b,b,b])
print("H stack: ", stack)
print()

#In 2 arrays a(1,2,3,4,5) and b(4,5,6,7,8,9) remove all repeating items in array b
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8,9])
c = np.delete(b, [0,1])
print(f"Removing duplicates: a{a}b{b} -> a{a}b{c}")
print()

#Get all integers between 5-10 from arrays a and b and sum together
sum1 = np.sum(a) + np.sum(c)
print("Sum: ", sum1)