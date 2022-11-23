#!/usr/bin/env python
# coding: utf-8
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# # Arrays and Pointers

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates arrays and pointers in C++

# ```c++
# // Simple array processing
# #include <iostream>
# 
# using namespace std;
# 
# const int SIZE = 5;
# 
# int main()
# {
#     int a[SIZE];    // get space for a[0], ....., a[4]
#     int i, sum = 0;
# 
#     for (i = 0; i < SIZE; ++i) {
#         a[i] = i * i;
#         cout << "a[" << i << "] = " << a[i] << "   ";
#         sum += a[i];
#     }
#     cout << "\nsum = " << sum << endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_12_Arrays_and_Pointers"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ sum_arr1.cpp -w -o sum_arr1")


# In[5]:


exec_status = os.system("./sum_arr1")

