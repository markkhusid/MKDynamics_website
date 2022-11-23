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
# # Free Store Operators **new** and **delete**

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates the free store operators *new* and *delete* in C++

# ```c++
# #include <iostream>
# #include <assert.h>
# using namespace std;
# 
# double avg_arr(const int a[], int size)
# {
#     int sum = 0;
#     for (int i = 0; i < size; ++i)
#         sum += a[i];
#     return static_cast<double>(sum) / size;
# }
# 
# int main()
# {
#     int *   data;
#     int     size;
# 
#     for (int n_loop = 0; n_loop < 1; ++n_loop) {
#         cout << "\nEnter array size: ";
#         cin >> size;
#         assert(size > 0);
# 
#         data = new int[size];
#         assert (data != 0);
# 
#         for (int j = 0; j < size; ++j) {
#             cout << "\nEnter data at position " << j << " -> ";
#             cin >> data[j];
#         }
#         
#         cout << " average is " << avg_arr(data, size) << endl;
#         delete [] data;
#     }
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_19_Free_Store_Operators_new_and_delete"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ dynarray.cpp -w -o dynarray")


# In[5]:


exec_status = os.system("echo \"5 123 456 789 321 654\" | ./dynarray")


# In[ ]:




