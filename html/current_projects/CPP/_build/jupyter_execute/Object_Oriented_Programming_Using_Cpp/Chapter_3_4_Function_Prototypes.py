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
# # Function Prototypes

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates function prototypes in C++

# ```c++
# // Add three ints - illustrating function prototypes
# #include <iostream>
# 
# int add3(int, int, int);
# double average(int);
# 
# using namespace std;
# 
# int main()
# {
#     int score_1, score_2, score_3, sum;
# 
#     cout << "\nEnter 3 scores: ";
#     cin >> score_1 >> score_2 >> score_3;
#     sum = add3(score_1, score_2, score_3);
#     cout << "\nTheir sum is " << sum;
#     cout << "\nTheir average is " << average(sum);
#     sum = add3(1.5 * score_1, score_2, 0.5 * score_3);
#     cout << "\nTheir weighted sum is " << sum << ".";
#     cout << "\nTheir weighted average is " << average(sum) << "." << endl;
# }
# 
# int add3(int a, int b, int c)
# {
#     return (a + b + c);
# }
# 
# double average(int s)
# {
#     return (s / 3.0);
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_3_4_Function_Prototypes"


# In[3]:


ch_dir_stat = os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ add3.cpp -w -o add3")


# In[5]:


exec_status = os.system("echo \"10 20 30\" | ./add3")


# In[6]:


exec_status = os.system("echo \"1210 8750 54360\" | ./add3")

