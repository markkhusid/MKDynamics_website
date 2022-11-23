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
# # Hello World!

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program to Display Hello World!

# ```c++
# // Hello world in C++
# #include <iostream>
# #include <string>
# 
# using namespace std;
# 
# inline void pr_message(string s = "Hello World!")
# {
#     cout << s << endl;
# }
# 
# int main()
# {
#     pr_message();
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Hello"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ hello.cpp -w -o hello")


# In[5]:


exec_status = os.system("./hello")

