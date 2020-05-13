#!/usr/bin/env python
# coding: utf-8

# # x^n/n!

# In[5]:


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return (n*factorial_recursive(n-1))

def calculation(x,n):
    upper=float(x)**n
    lower=factorial_recursive(n)
    result=upper/lower
    return result

print(calculation(3.5,4))


# In[ ]:




