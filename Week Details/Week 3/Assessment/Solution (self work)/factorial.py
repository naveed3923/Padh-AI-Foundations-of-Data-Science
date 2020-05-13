#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True:
    x=input('enter number: ')
    if x=='done' or x=='DONE':
        break
    try:
        n=int(x)
    except:
        print('please enter valid number')
        continue
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)


# In[ ]:





# In[ ]:





# In[ ]:




