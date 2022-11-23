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
# # Program Structure

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates program structure in C++

# ```c++
# // Greatest common divisor program.
# #include <iostream>
# #include <assert.h>
# 
# int gcd(int m, int n)   // function declartion
# {                       // block
#     int r;              // declaration of remainder
# 
#     while (n != 0) {    // not equal
#         r = m % n;      // modulo operator
#         m = n;          // assignment
#         n = r;
#     }                   // end while loop
# 
#     return m;           // exit gcd with value m
# }
# 
# int main()
# {
#     int x, y, g;
# 
#     std::cout << "\nProgram GCD C++";
#     do {
#         std::cout << "\nEnter two integers: ";
#         std::cin >> x >> y;
#         assert(x * y != 0); // precondition on GCD
#         std::cout << "\nGCD(" << x << ", " << y << ") = "
#              << (g = gcd(x, y)) << std::endl;
#         assert(x % g == 0 && y % g ==0); // postcondition
#     } while (x != y);
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_2_3_Program_Stucture"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ gcd.cpp -w -o gcd")


# In[5]:


exec_status = os.system("echo \"20 10 50 4 60 30 100 100\" | ./gcd")


# In[ ]:




