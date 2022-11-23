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
# # Pointer Types

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates pointer types in C++

# ```c++
# // Pointer - based call - by - reference
# #include <iostream>
# 
# using namespace std;
# 
# void order (int *, int *);
# 
# int main()
# {
#     int i = 7, j = 3;
# 
#     cout << i << '\t' << j << endl; // 7 3 is printed
#     order(&i, &j);
#     cout << i << '\t' << j << endl; // 3 7 is printed
# }
# 
# void order(int * p, int * q)
# {
#     int temp;
# 
#     if (*p > *q) {
#         temp = *p;
#         *p = *q;
#         *q = temp;
#     }
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_10_Pointer_Types"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ call_ref.cpp -w -o call_ref")


# In[5]:


exec_status = os.system("./call_ref")

