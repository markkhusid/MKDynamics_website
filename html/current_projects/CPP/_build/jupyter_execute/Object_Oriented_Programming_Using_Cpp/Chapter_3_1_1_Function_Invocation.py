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
# # Function Invocations

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates function invocations in C++

# ```c++
# // Ring the bell using '\a' literal for the alarm.
# 
# #include <iostream>
# 
# const char BELL = '\a';
# 
# void ring()
# {
#     std::cout << BELL;
#     std::cout << "Hello from function ring!" << std::endl;
# }
# 
# int main()
# {
#     ring();
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_1_1_Function_Invocation"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ bell.cpp -w -o in_the_bell")


# In[5]:


exec_status = os.system("./in_the_bell")

