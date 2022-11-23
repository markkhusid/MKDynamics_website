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
# # Assertions and Program Correctness

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates the *ASSERT* statement in C++

# ```c++
# // FInding a minimum element in an array slice.
# #include <iostream>
# #include <assert.h>
# 
# using namespace std;
# 
# void order (int & p, int & q)
# {
#     int temp = p;
#     if (p > q) {
#         p = q;
#         q = temp;
#     }
# }
# 
# int place_min(int a[], int size, int lb = 0)
# {
#     int i, min;
#     assert(size >= 0);   // precondition
# 
#     for (i = lb; i < lb + size; ++i)
#         order(a[lb], a[i + 1]);
#     return a[lb];
# }
# 
# int main()
# {
#     int a[9] = { 6, -9, 99, 3, -14, 9, -33, 8, 11 };
# 
#     cout << "Minimum = " << place_min(a, 3, 2) << endl;
#     assert(a[2] <= a[3] && a[2] <= a[4]);   // postcondition
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_16_Assertions_and_Program_Correctness"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ order.cpp -w -o order")


# In[5]:


exec_status = os.system("./order")

