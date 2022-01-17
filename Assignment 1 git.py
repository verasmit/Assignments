#!/usr/bin/env python
# coding: utf-8

# <img src="images/logo.jpeg">

# # Assignment 1: Introduction to Python
# 
# This assignment tests the Python skills you have learnt in the per-course Datacamp lectures.
# 
# Notes:
# - You should not hardcode a solution to any of the questions below. Doing so will result in a mark of 0 for the question.

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import collections
from scipy import spatial


# ## Collections, NumPy and Matplotlib

# Answer the next few questions using the list created in the following code block:

# In[94]:


my_list = list(np.random.randint(low=-5, high=10, size=20))
print(my_list)


# 1.) Display the given list in reverse order. [1 point]

# In[96]:


reversed_list = my_list[::-1]
print(reversed_list)


# 2.) Square every element in the list [1 point]

# In[98]:


square_list = list(np.array(my_list)**2)
print(square_list)


# 3.) Remove all of the negatigve values from the list [1 point]

# In[100]:


positive = []

for i in my_list:
    if i >= 0:
        positive.append(i)
    if i <=0:
        positive.append(-i)
print(positive)


# 4.) Find the index of the largest element in the list [1 point]

# In[101]:


max_element = max(my_list)
max_index = print(my_list.index(max_element))


# 5.) Print out the number of occurrences of each of the element in the list, using the following format: [1 point]
# 
# "x occurs y times in the list"

# In[116]:


from collections import Counter

repeats = collections.Counter(my_list)
collect_repeats = dict(repeats)

print(str(collect_repeats) + "occurs" + str(repeats) + "times in the list") ##?


# In[ ]:





# Use the following data for the next few questions:

# In[67]:


names = ["Northern Cape", "Eastern Cape", "Western Cape"]
areas = [372889, 168966, 129462]
provinces = {'Free State': 129825, 'Limpopo': 125755, 'North West': 104882, 'KwaZulu-Natal': 94361, 'Mpumalanga': 76495, 'Gauteng': 18178}


# xx.) Create a dictionary, `cape`, of the the Cape province names and their corresponding areas [1 point]

# In[70]:


zip_cape = zip(names, areas)
cape = dict(zip_cape)
print(cape)


# xx.) Update the `provinces` dictionary to include the `cape` data using an appropriate built-in dictionary function [1 point]

# In[72]:


provinces.update(cape)
print(provinces)


# xx.) Print out the sum of the areas of all of the provinces [1 point]

# In[79]:


print(sum(provinces.values()))


# xx.) Display the provinces and their corresponding areas in alphabetical order [1 point]

# In[80]:


print(sorted(provinces))


# Using `matplotlib`, plot a barplot of the sizes of the provinces. 
# 
# The sizes should be on the y-axis, and the province names on the x-axis. Specify an appropriate title, add an x- and y-label, and rotate the x-axis labels.
# [5 points]

# In[91]:


import matplotlib.pyplot as mpl

bar = plt.figure()
y_lab = str(provinces.keys)
area = provinces.values


# Use the following matrices and vectors for the next few questions:

# In[8]:


A = np.random.randint(low=0, high=10, size=(3, 3))
B = np.random.randint(low=0, high=10, size=(3, 3))
vec1 = np.random.randint(low=0, high=10, size=3)
vec2 = np.random.randint(low=0, high=10, size=3)
print(f"A = \n{A}\n")
print(f"B = \n{B}\n")
print(f"vec1 = \n{vec1}\n")
print(f"vec2 = \n{vec2}\n")


# xx.) Find the average of the entries in `vec1` and print the result. [1 point]

# In[18]:


# Insert code
vec_1 = np.array(vec1)
vec_1_mean = np.mean(vec_1)
print(vec_1_mean)


# xx.) Find the element-wise difference between `vec1` and `vec2`, and print the result. [1 point]

# In[22]:


# insert code here

vec_2 = np.array(vec2)
difference = vec_2-vec_1
print(difference)


# xx.) Find the Euclidean distance between `vec1` and `vec2`. [1 point]

# In[120]:


# insert code here
eu_dist = np.linalg.norm(vec1 - vec2)
print(eu_dist)


# In[ ]:





# xx.) Find the cosine distance between `vec1` and `vec2`. [1 point]

# In[25]:


# insert code here

cosine_dist = spatial.distance.cosine(vec1,vec2)
print(cosine_dist)

# if rounded for clarity

print(cosine_dist.round(2))


# In[ ]:





# xx.) Scale (multiply) all the entries of `vec1` by its mean, and print the result. [1 point]

# In[39]:


# insert code here

def scale(x): 
    for i in vec_1:
        i*vec_1_mean
        return(i*vec_1_mean)  

print(scale(vec1))    


# xx.) Normalize `vec1` and print the result. [1 point]

# In[41]:


# insert code here

normalised = vec_1/np.linalg.norm(vec_1) #square root of added squared entries if hard code

print(normalised)


# xx.) Find the matrix product of `A` and `B` [1 point]

# In[43]:


# insert code here
matrixAB = A*B
print(matrixAB)


# xx.) Given the matrix, `A`, subtract the column mean of `A` from each entry. This has the effect of zero-centering the data and is often done in algorithms such as principal components analysis or when running computer vision models. [1 point]

# In[50]:


# Insert code
A_mean = A.mean(axis=0)
print(A - A_mean)


# xx.) Given a vector `vec1`, compute the softmax scores of the vector. [1 point]
# 

# In[61]:


# Insert code

def softmax(x):
    exp = np.exp(x-np.max(x))
    print(exp/exp.sum())
    
soft_vec = softmax(vec1)

scores = vec1


# In[ ]:





# # Functions

# Write a function named `sign`, which returns a string `positive`, `negative`, or `zero`, given an interger value as input to the function [3 points].

# In[30]:


#define the function
def sign(x):
    if x >0:
        return "positive"
    if x<0:
        return "negative"

    if x==0:
        return "zero"

#testing the code
    for x in [-5,0,5]:
    print(sign(x))


# Write a fuction that returns the minimum value given an arbitrary number of integers as input paramters. [4 points]

# In[122]:


# Insert function 

min_number = [0]
def min_value(arb):
    min_number = arb[0]
    for i in arb:
        if i < min_number:
            min_number = i
    
    return min_number


# Write a recursive function to display the Fibonacci sequence using recursion. 
# 
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms i.e. the n-th term is the sum of (n-1)-th and (n-2)-th term. [4 points]

# In[65]:


#define function

def fibonacci_rec(n):
    if n <=1:
        return 1
    else:
        return(fibonacci_rec(n-1)+fibonacci_rec(n-2))

#test code
for i in range(10):
    print(fibonacci_rec(i))


# # Classes
# 
# 

# Create a class called `Circle`.
# You are required to implement the following:
# * The constructor of the class should take two floats that specify the `x` and `y` coordinates of the circle, a float specifying the `radius` of the circle. [2 points]
# * A function, `str_circle`, which prints properties of a circle as follow: [2 points]
#             Circle at location x = ___ and y = ___ with radius = ___
# * A function, `dist`, which returns the euclidean distance between two circles' centers. [4 points]
# * A function,`overlap`, which returns `True` if two circles overlap and `False` otherwise. [3 points]
# * A function, `area`, which calculates the area of the circle. [3 point].
# * A function, `overlap_area`, which calculates the area of the overlapping portion of two circles. [6 points]
# 
# The formula for calculating the overlapping area between two circles is provided below:
# 
# \begin{equation}
# \small
# A = 
# r^2\text{cos}^{-1}(\frac{d^2+r^2-R^2}{2dr}) + R^2\text{cos}^{-1}(\frac{d^2+R^2-r^2}{2dR}) -
# \frac{1}{2}\sqrt{(-d+r+R)(d+r-R)(d-r+R)(d+r+R)}
# \end{equation}
# 
# where
# 
# $\;\;\;\;\;\;\;\;$A = area of overlapping <br>
# $\;\;\;\;\;\;\;\;$r = radius of circle 1 <br>
# $\;\;\;\;\;\;\;\;$R = radius of circle 2 <br>
# $\;\;\;\;\;\;\;\;$d = distance between the circles <br>

# In[127]:


import math

class Circle(x,y,r):
    x = Circle[0]
    y = Circle[1]
    r = Circle[2]

def area_circle():
    math.pi*r**2
    
def str_circle():
    print("Circle at location x ="+(x)+"and y ="+(y)+" with radius ="(r))


def dist(x,y):
    return(sqrt(x)+sqrt(y))


def area_circle():
    math.pi*r**2
    
    







# The next few snippets of code can be used to verify that your implementation of the functions of `Circle` is working correctly.

# Create the following two circles: [1 point]
# * `circle1`: x = 2, y = 1, rad = 1
# * `circle2`: x = -1, y = -2, rad = 3 

# In[ ]:





# Print out the circles using `str_circle`

# In[ ]:





# Print the distance between circle 1 and 2.

# In[ ]:





# Check if `circle1` and `circle2` overlap.

# In[131]:


0


# Print out the area of `circle1` and `circle2`.

# In[ ]:





# Print out the overlapping area of `circle1` and `circle2`. 

# In[ ]:




