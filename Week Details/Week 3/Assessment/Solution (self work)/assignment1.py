#!/usr/bin/env python
# coding: utf-8

# In[5]:


weight=input('enter your weight (kgs): ')
pref=input('Preferred unit of height: ')
if pref=='M':
    hyt=input("What's your height in meters: ")
    height=float(hyt)
else:
    a=input('You will enter your height given as feet and inches: ')
    b=input('Enter inches: ')
    height=(float(a)*0.3048) + (float(b)*0.0254)
              
height_i=(height)**2
bmi=(float(weight))/height_i

if bmi<18.5:
    print('UNDERWEIGHT')
elif bmi>=18.5 and bmi<25:
    print('NORMAL')
    print('YOUR BMI is: ',bmi)
elif bmi>=25 and bmi<30:
    print('OVERWEIGHT')
else:
    print('VERY OVERWEIGHT')


# In[ ]:




