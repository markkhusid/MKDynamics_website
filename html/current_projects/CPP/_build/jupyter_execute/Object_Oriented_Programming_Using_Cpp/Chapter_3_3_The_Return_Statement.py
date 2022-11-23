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
# # The Return Statement

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates the *RETURN* statement in C++

# ```c++
# // Find the minimum of two ints.
# #include <iostream>
# 
# int min(int x, int y)
# {
#     if (x < y)
#         return x;
#     else
#         return y;
# }
# 
# int main()
# {
#     int j, k, m;
# 
#     std::cout << "Input two integers: ";
#     std::cin >> j >> k;
#     m = min(j, k);
#     std::cout << '\n' << m << " is the minimum of " << j
#               << " and " << k << std::endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_3_The_Return_Statement"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ min_int.cpp -w -o min_int")


# In[5]:


exec_status = os.system("echo \"10 20\" | ./min_int")


# In[6]:


exec_status = os.system("echo \"89 27\" | ./min_int")

