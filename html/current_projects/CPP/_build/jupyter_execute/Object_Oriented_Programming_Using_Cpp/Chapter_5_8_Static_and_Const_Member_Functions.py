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
# # **STATIC** and **CONST** Member Functions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates the **STATIC** and **CONST** member functions in C++

# ```c++
# #include <iostream>
# 
# using namespace std;
# 
# // Calculate salary using static members
# class salary {
# public:
#     void init(int b) {
#         b_sal = b;
#         your_bonus = 0;
#     }
# 
#     void calc_bonus(double perc) {
#         your_bonus = b_sal * perc;
#     }
# 
#     static void reset_all(int p) {
#         all_bonus = p;
#     }
# 
#     int comp_tot() const {
#         return (b_sal + your_bonus + all_bonus);
#     }
# 
# private:
#     int         b_sal;
#     int         your_bonus;
#     static int  all_bonus;      // declaration
# };
# 
# // declaration and definition
# int salary::all_bonus = 100;
# 
# int main() {
#     salary w1, w2;
# 
#     w1.init(1000);
#     w2.init(2000);
# 
#     w1.calc_bonus(0.2);
#     w2.calc_bonus(0.15);
# 
#     salary::reset_all(400);
# 
#     cout    << " w1 "
#             << w1.comp_tot() 
#             << " w2 " 
#             << w2.comp_tot() 
#             << endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_5_8_Static_and_Const_Member_Functions"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ salary.cpp -w -o salary")


# In[5]:


exec_status = os.system("./salary")

