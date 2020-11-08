#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:02:04 2020

@author: alicehoyle
"""

import pandas as pd

# How many rows and columns are in your file?
data = pd.read_csv("destinations.csv", index_col=[0])
print("Shape: ", data.shape)
print()



# Print rows3-8 using iloc/loc
print("""iloc: 
""", data.iloc[3:9])
print()



# Find the mean number of all inclusive hotels
print("Mean: ", data["Inclusive"].mean())
print()



# Find the lowest scoring destination
data.sort_values("Score", ascending=True)
highest = data.head(1)
print("Highest scoring: ", highest)
print()



# Find the highest scoring destination
lowest = data.tail(1)
print("Lowest scoring: ", lowest)
print()



# Find all the destinations where there are more than 9 all inclusive hotels
all_incl = data["Inclusive"] > 9
all_incl9 = data[all_incl]
print("""9+ All inclusive hotels: 
""", all_incl9)
print()



# Filter the data by destination and score above 8
high_score = data["Score"] > 8
high_score8 = data[high_score]
print("""Score+8: 
""", high_score8)
print()



# Filter the data by destination and score below 2
low_score = data["Score"] < 2
low_score2 = data[low_score]
print("""Score-2:
""",low_score2)
print()



# Is there a correlation between number of all inc hotels and score
correlation = data.corr(method = "pearson") 
print("""Correlation: 
""",correlation)
print(""""There is a higher correlation between Rating/5 and number
of all inclusive hotels.""")
print()


      
# Create a data visualisation diagram to show destination and highest score
