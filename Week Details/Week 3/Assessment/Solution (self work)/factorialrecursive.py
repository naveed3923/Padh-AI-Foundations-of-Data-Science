#!/usr/bin/env python
# coding: utf-8

# # FACTORIAL USING RECURSIVE FUNCTION

# In[4]:


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return (n*factorial_recursive(n-1))

print(factorial_recursive(6))


# In[ ]:




