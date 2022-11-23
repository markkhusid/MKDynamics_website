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
# # Access: Private and Public

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates private and public access of object items in C++

# ch_stac3.cpp

# ```c++
# // Reverse a string with a ch_stack.
# #include <iostream>
# #include "ch_stac3.h"
# 
# using namespace std;
# 
# int main ()
# {
#     ch_stack s;
#     char str[40] = {"My name is Don Knuth!"};
#     int i = 0;
# 
#     cout << str << endl;
#     s.reset();  // s.top = EMPTY would be illegal
# 
#     while (str[i] && !s.full())
#     {
#         s.push(str[i++]);
#     }
# 
#     while (!s.empty())      // print the reverse
#     {
#         cout << s.pop();
#     }
# 
#     cout << endl;
# }
# ```

# ch_stac3.h

# ```c++
# struct ch_stack {
#     public:
#         void reset ()       { top = EMPTY; }
#         void push (char c)  { top++; s[top] = c; }
#         char pop ()         { return s[top--]; }
#         char top_of ()      { return s[top]; }
#         bool empty ()       { return ( top == EMPTY ); }
#         bool full ()        { return ( top == FULL  ); }
# 
#     private:
#         enum 
#         {  
#             max_len = 100,
#             EMPTY = -1,
#             FULL = max_len-1
#                 
#         };
# 
#         char s[max_len];
#         int top;
# };
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_5_2_Access_Private_and_Public"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ ch_stac3.cpp -w -o ch_stac3")


# In[5]:


exec_status = os.system("./ch_stac3")

