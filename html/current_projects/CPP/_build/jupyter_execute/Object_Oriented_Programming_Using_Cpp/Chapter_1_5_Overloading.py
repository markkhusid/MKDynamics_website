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
# # Overloading the "+" Operator to Handle Strings

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates operator overloading in C++

# ```c++
# // Overloading the operator +
# #include <iostream>
# #include <string>
# #include <cstring>
# 
# using namespace std;
# 
# class my_string {
#     public:
#         my_string() { 
#             len = 0; s = new char[1]; 
#         }
# 
#         explicit my_string(int n) {
#             s = new char[n+1];
#             len = n;
#         }
# 
#         void assign(const char* str)
#         {
#             delete []s;
#             len = strlen(str);
#             s = new char[len + 1];
#             strcpy(s, str);
#         }
# 
#         int length() const {
#             return len;
#         }
# 
#         void print() const {
#             cout << s << "\nLength: " << len << endl;
#         }
# 
#         friend my_string& operator+ (const my_string& a, const my_string& b);
#     
#     private:
#         char* s;
#         int len;
# };
# 
# // Overload +
# my_string& operator+(const my_string& a, const my_string& b)
# {
#     my_string* temp = new my_string(a.len + b.len);
# 
#     strcpy(temp->s, a.s);
#     strcat(temp->s, b.s);
#     return *temp;
# }
# 
# void print(const char* c) // file scope print
# {
#     cout << c << "\nLength: " << strlen(c) << endl;
# }
# 
# int main()
# {
#     my_string one, two, both;
#     char three[40] = {"My name is Charles Babbage."};
# 
#     one.assign("My name is Alan Turing.");
#     two.assign(three);
#     print(three);   // file scope print called
# 
#     if (one.length() <= two.length())
#         one.print();
#     else
#         two.print();
# 
#     both = one + two;
# 
#     both.print();
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_1_5_Overloading"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ string4.cpp -w -o string4")


# In[5]:


exec_status = os.system("./string4")

