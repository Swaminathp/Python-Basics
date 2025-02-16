#!/usr/bin/env python
# coding: utf-8

# # Python Basics Assignment

# Q1. Using Python script as a calculator
# Create the variables n, r, p and assign them values 10, 5, and 100 respectively. Then
# evaluate the following expression in the Python console.
# 𝐴 = 𝑝 (1 + 𝑟/ 100)n
# a. 100
# b. 162.89
# c. 189
# d. None of the above

# In[1]:


# Given values
n = 10
r = 5
p = 100

# Calculate A
A = p * (1 + r / 100) ** n

# Print the result
print(A)


# Answer : The computed value of 
# 𝐴
# A is 162.89 (rounded to two decimal places).
# Thus, the correct answer is:
# (b) 162.89 

# Q2. In a given string format operation, how will you print the given string.
# A = 10
# B = 20
# Str = "There are {} students in the class, with {} who play at least one sport."
# a. print(string.format(a,b))
# b. print(string+a+b)
# c. print(string.format(b,a))
# d. None of the above
# 

# In[2]:


A = 10
B = 20
Str = "There are {} students in the class, with {} who play at least one sport."

print(Str.format(B, A))


# Answer : c. print(string.format(b,a))

# Q3. In a given sample string, How do you print a double quoted string in between a
# regular
# string using the escape character?
# Sample output = It goes without saying, “Time is Money”, and none can deny it.
# a. print(“It goes without saying, \“Time is Money\”, and none can deny it.”)
# b. print(“It goes without saying, \Time is Money\, and none can deny it.”)
# c. print(“It goes without saying” + “Time is Money” + “and none can deny it.”)
# d. None of the above.

# In[3]:


print("It goes without saying, \"Time is Money\", and none can deny it.")


# Answer : a. "It goes without saying, \"Time is Money\", and none can deny it."

# Q4. What will be the output of the following code?
# x = lambda a,b: a//b
# x(10,3)
# a. 3.3333333333
# b. 3
# c. 30
# d. 1000
# 

# In[4]:


x = lambda a,b: a//b
x(10,3)


# Answer : b.3

# Q5. What will be the output of the following code?
# A = 10
# B = 12
# print("Smaller") if A == B else print("Greater") if A < B else print("True")
# a. True
# b. Smaller
# c. Greater
# d. None of the above

# In[5]:


A = 10
B = 12
print("Smaller") if A == B else print("Greater") if A < B else print("True")


# Answer : c. Greater

# Q6. What will be the output of the following code?
# 
# import os
# import numpy as np
# my_list1 = [2,7,3,5,4,6]
# print(my_list1)
# arr1 = numpy.array(my_list1, dtype = int)
# print(arr1)
# 
# a. [2 7 3 5 4 6]
# b. TypeError
# c. NameError: name 'numpy' is not defined
# d. None of the above
# 

# In[6]:


import os
import numpy as np
my_list1 = [2,7,3,5,4,6]
print(my_list1)
arr1 = numpy.array(my_list1, dtype = int)
print(arr1)


# Answer : c. NameError: name 'numpy' is not defined 

# Q7. Create a string called ‘string’ with the value as “Machine Learning”. Which code(s)
# is/are appropriate to slice the substring “Learn”?
# a. string[slice(13,8,1)]
# b. string[slice(1,8,1)]
# c. string[8:14]
# d. string[slice(8,13,1)]

# In[ ]:


string = "Machine Learning"

string[slice(8,13,1)]


# Answer : d.string[slice(8,13,1)]

# Q8. Create a sequence of numbers from 10 to 25 and increment by 4. What is the index
# of the
# value 18?
# a. 3
# b. 2
# c. 0
# d. 1

# In[ ]:


sequence = list(range(10, 26, 4))
print(sequence)

sequence.index(18)


# Answer : b.2

# Q9. Which of the following is true with respect to the below codes?
# 
# num1 = 5**4
# num2 = pow(5,4)
# print(num1,num2)
# 
# 
# 
# a. num1 = num2
# b. num1 ≠ num2
# c. num1 < num2
# d. num1 > num2

# In[ ]:


num1 = 5**4
num2 = pow(5,4)
print(num1,num2)


# Answer : a.num1 = num2 

# Q10.A Python NameError exception is raised when: -
#     
# a. Trying to access a variable which has not been defined
# 
# b. Trying to access a key in a dictionary that does not exist
# 
# c. Accessing a column with misspelled column name
# 
# d. Accessing the function from a module that has not been imported

# Answer : a. Trying to access a variable which has not been defined

# Q11.What type of exception will be raised for the code given below?
# 
# x = "String"
# 
# int(x)
# 
# a. NameError
# b. KeyError
# c. ValueError
# d. AttributeError
# 

# In[ ]:


x = "String"

int(x)


# Answer : c. ValueError

# Q12.A FileNotFoundError exception is raised by operating system errors when: -
# 
# a. Trying to create a file or directory which already exists
# 
# b. A file or directory is requested but does not exist in the working directory
# 
# c. Trying to run an operation without the adequate access rights
# 
# d. A directory operation, os.listdir() is requested on something which is not a
# directory

# Answer : b. A file or directory is requested but does not exist in the working directory

# Q13.Consider a variable Z. The value of Z is "ID-5632". Data type of Z is: -
# a. Complex
# b. Character
# c. Integer
# d. Boolean

# Answer : b. Character (str)

# Q14.Which of the following variable(s) are character data type?
# a. K= “4”
# b. J= “Welcome”
# c. L= “?”
# d. All of the above

# Answer : d. All of the above

# Q15.Choose the symbol/s that does not have the ability to convert any values to string?
# a. ( )
# b. “ ”
# c. {}
# d. #

# Answer : d. #

# Q16.Create a dictionary ‘Country’ that maps the following countries to their capitals
# respectively
# 
# Country   India   China   Japan   Qatar   France
# 
# State   Delhi   Beijing   Tokyo   Doha   Marseilles
# 
# Find 2 commands to replace “Marseilles” with “Paris” is:

# In[ ]:


Country = {'India' : 'Delhi', 'China' : 'Beijing', 'Japan' : 'Tokyo', 'Qatar' : 'Doha', 'France' : 'Marseilles'}
Country


# In[ ]:


Country["France"] = "Paris"
print(Country)


# In[ ]:


Country.update({"France": "Paris"})
print(Country)


# Q17. Create the tuples given below
# 
# tuple_1 = (1,5,6,7,8)
# 
# tuple_2 = (8,9,4)
# 
# Identify which of the following code does not work on a tuple.
# 
# a. sum(tuple_1)
# b. len(tuple_2)
# c. tuple_2 + tuple_1
# d. tuple_1[3] = 45

# In[ ]:


tuple_1 = (1,5,6,7,8)

tuple_2 = (8,9,4)


# Answer : d. tuple_1[3] = 45 (TypeError: 'tuple' object does not support item assignment)

# Q18. How many elements in the following data structure?
# 
# S = {1,2,3,4,4,4,5,6}

# In[ ]:


S = {1,2,3,4,4,4,5,6}
S


# In[ ]:


len(S)


# Answer : 6

# Q19.Write a function which finds all pythagorean triplets of triangles whose sides are no
# greater than a natural number N.

# In[ ]:


def find_pythagorean_triplets(N):
    triplets = []
    
    for a in range(1, N+1):
        for b in range(a, N+1):  
            c = (a**2 + b**2) ** 0.5  
            if c.is_integer() and c <= N: 
                triplets.append((a, b, int(c)))
    
    return triplets

# Example Usage:
N = 20
print(find_pythagorean_triplets(N))


# In[ ]:




