#!/usr/bin/env python
# coding: utf-8

# # MULTIPLE FUNCTIONS (ASSIGNMENT-1 : PROBLEM 2)

# In[13]:


#1)FACTORIAL USING RECURSIVE FUNCTION

def factorial_recursive(n):
    if n>1:
        return (n*factorial_recursive(n-1))
    else:
        return 1
        
    
#2)CALCULATION OF x**n/n!

def calculate_ratio(x,n):
    upper=float(x)**n
    lower=factorial_recursive(n)
    result=upper/lower
    return result



#3)ITERATIVE SUM OF THE ABOVE SERIES FROM CALCULATION FUNCTION/ TAYLOR SERIES

def iterative_sum(x,N):                                          
    total=1
    for i in range(1,N+1):
        total=total+calculate_ratio(x,i)
    return total



#4)ITERATIVE SUM OF x**n/n! from n=1 to a chosen value N' such that F(x,N')-F(x,N'-1)<epsi (x is real and eps is small & positive)
#let N'=y

def compute_epsilon(x,epsilon):
    sums=1
    var=epsilon
    i=1
    while var>=epsilon:
        var=calculate_ratio(x,i)
        sums=sums+var
        i=i+1
    return sums




#METHOD 2

def comp_epsilon1(x,epsilon):
    sums=1
    i=1
    while True:
        var=calculate_ratio(x,i)
        sums=sums+var
        i=i+1
        if var<epsilon:
            break
    return sums

print(comp_epsilon1(2,0.01))


#5) compute v1 and v2 (v1-v2)

p=2.1
q=1.3

v1=iterative_sum(p,100)*iterative_sum(q,100)
v2=iterative_sum(p+q,100)

result=v1-v2

print(result)


# In[ ]:





# In[ ]:




