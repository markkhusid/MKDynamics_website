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
# # The Traditional Conversions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates type conversion in C++

# ```c++
# // Miles are converted to kilometers
# #include <iostream>
# 
# const double m_to_k = 1.609;    // Conversion constant
# 
# inline double mi_to_km(int miles)
# {
#     return (miles * m_to_k);
# }
# 
# int main()
# {
#     int miles;
#     double kilometers;
# 
#     do {
#         std::cout << "\nEnter distance in miles: ";
#         std::cin >> miles;
# 
#         kilometers = mi_to_km(miles);
#         std::cout << "\nThis is approximately " << static_cast<int>(kilometers) 
#             << "km." << std::endl;
#     } while (miles > 0);
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_2_5_The_Traditional_Conversions"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ m_to_k.cpp -w -o m_to_k")


# In[5]:


exec_status = os.system("echo \"10 50 0\" | ./m_to_k")

