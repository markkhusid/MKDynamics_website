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
# # The *THIS* Pointer

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates the use of the *this* pointer in C++

# ```c++
# #include <iostream>
# 
# using namespace std;
# 
# // The this pointer
# 
# class c_pair {
#     public:
#         void init(char b) { c2 = 1 + (c1 = b); }
#         c_pair increment() { c1++; c2++; return (*this); }
#         c_pair* where_am_I() { return this; }
#         void print() { cout << c1 << c2 << '\t'; }
#     private:
#         char c1, c2;
# };
# 
# int main()
# {
#     c_pair a, b;
# 
#     a.init('A');
#     a.print();
#     cout << " is at " << a.where_am_I() << endl;
# 
#     b.init('B');
#     b.print();
#     cout << " is at " << b.where_am_I() << endl;
#     b.increment().print();
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_5_7_The_this_Pointer"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ c_pair.cpp -w -o c_pair")


# In[5]:


exec_status = os.system("./c_pair")

