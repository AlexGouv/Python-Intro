# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# create a series from a list
arr = [0, 1, 2, 3, 4]
s1 = pd.Series(arr)
s1

order = [1, 2, 3, 4, 5]
s2 = pd.Series(arr, index = order)
s2

import numpy as np

n = np.random.randn(5) # create random Ndarray
index = ['a', 'b', 'c', 'd', 'e']
s3 = pd.Series(n, index = index)
s3

# create a series from a dictionary
d = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s4 = pd.Series(d)
s4

# change index
s1.index = ['A', 'B', 'C', 'D', 'E']
s1

# series operations
arr1 = [0, 1, 2, 3, 4, 5, 7]
arr2 = [6, 7, 8, 9, 5]

s5 = pd.Series(arr2)
s5
s6 = pd.Series(arr1)
s6

s5.add(s6)
s5+s6

s5.sub(s6)
s5 - s6

s7 = s5.div(s6)
s7

s7.median()
s7.max()
round(s7.mean(), 2)

# create dataframe
dates = pd.date_range('today', periods = 6)
num_arr = np.random.randn(6, 4)
columns = ['A', 'B', 'C', 'D']

df1 = pd.DataFrame(num_arr, index = dates, columns = columns)
df1

data = {'animal' : ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age' : [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits' : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority' : ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(data, index = labels)
df2

# explore data
df2.dtypes
df2.head()
df2.tail()
df2.index
df2.columns
df2.values
df2.describe()

# manipulating data
df2.T                               # transpose
df2.sort_values(by = 'age')         # sort
df2[1:3]                            # slice
df2.sort_values(by = 'age')[1:3]    # sort and slice
df2[['age', 'visits']]              # select certain columns 
df2.iloc[1:3]                       # query rows 2 and 3







