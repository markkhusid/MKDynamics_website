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
# # Function Definitions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates function definitions in C++

# ```c++
# // Repeated bell ringing
# #include <iostream>
# 
# const char BELL = '\a';
# 
# void ring(int k)
# {
#     int i;
# 
#     for (i=0; i<k; ++i) {
#         std::cout << BELL;
#         std::cout << "Ring!" << std::endl;
#     }
# }
# 
# int main ()
# {
#     int n;
#     std::cout << "\nInput a small positive integer: " << std::endl;
#     std::cin >> n;
#     ring(n);
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_2_Function_Definition"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ bellmltl.cpp -w -o bellmltl")


# In[5]:


exec_status = os.system("echo \"10\" | ./bellmltl")


# In[ ]:




