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
# # Bit Fields

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates bit field manipulation in C++

# ```c++
# #include <iostream>
# 
# using namespace std;
# 
# struct word {
#     unsigned    w0:1, w1:1, w2:1, w3:1, w4:1, w5:1, w6:1, w7:1,
#                 w8:1, w9:1, w10:1, w11:1, w12:1, w13:1, w14:1, w15:1,
#                 w16:1, w17:1, w18:1, w19:1, w20:1, w21:1, w22:1, w23:1, 
#                 w24:1, w25:1, w26:1, w27:1, w28:1, w29:1, w30:1, w31:1;
# };
# 
# union set {
#     word        m;
#     unsigned    u;
# };
# 
# int main()
# {
#     set x, y;
# 
#     x.u = 0x0f100f10;
#     y.u = 0x01a1a0a1;
#     x.u = x.u | y.u;    // set union
# 
#     cout    << "\nelement 9 = " 
#             << ((x.m.w9) ? "true" : "false") << endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_4_7_Bit_Fields"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ set.cpp -w -o set")


# In[5]:


exec_status = os.system("./set")

