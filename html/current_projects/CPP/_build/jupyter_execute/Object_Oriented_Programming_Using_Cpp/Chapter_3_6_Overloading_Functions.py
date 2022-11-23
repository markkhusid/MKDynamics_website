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
# # Overloading Functions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates overloading functions in C++

# ```c++
# // Average the values in an array
# #include <iostream>
# 
# using namespace std;
# 
# double avg_arr(const int a[], int size)
# {
#     int sum = 0;
# 
#     for (int i = 0; i < size; ++i)
#         sum += a[i];        // performs int arithmetic
#     return (static_cast<double>(sum) / size);
# }
# 
# double avg_arr(const double a[], int size)
# {
#     double sum = 0.0;
# 
#     for (int i = 0; i < size; ++i)
#         sum += a[i];
#     return (sum / size);
# }
# 
# int main()
# {
#     int w[5] = { 1, 2, 3, 4, 5 };
#     double x[5] = { 1.1, 2.2, 3.3, 4.4, 5.5 };
# 
#     cout << avg_arr(w, 5) << " int average" << endl;
#     cout << avg_arr(x, 5) << " double average" << endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_6_Overloading_Functions"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ avg_arr.cpp -w -o avg_arr")


# In[5]:


exec_status = os.system("./avg_arr")

