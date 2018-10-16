
# coding: utf-8

# # Basics of NumPy with Jupyter

# ## What is Jupyter?
# Jupyter is a web application that allows you to create and share code
# 
# ### Why do we use Jupyter?
# 1. Science
# 2. With Jupyter hubs you can write, edit, and run code from any device with a web browser
# 3. Teaching and Sharing

# ## Basics of Jupyter

# This is a markdown cell you can put pictures, words, and links in here
# ![image.png](attachment:image.png)

# In[4]:


print('This is python code')


# # What is NumPy
# 
# NumPy is a library for python for scientific computing

# ### Why do we use NumPy?
# 1. Arrays
# 2. Statistical Operations
# 3. Sorting
# 4. Much more stuff I don't even know about yet but its awesome

# In[5]:


import numpy as np


# ### Basics of NumPy arrays

# In[93]:


time = np.arange(1,24,1)
print(time)
number_line = np.linspace(1,10,100)
print(number_line)


# In[35]:


np_array = np.random.rand(10)*10+1
print(np_array)


# In[36]:


np_array = np_array.astype(int)
print(np_array)


# In[38]:


print(np_array * 2)
print(np_array / 2)
print(np_array + 5)
print(np_array - 10)


# In[41]:


arr1 = np_array
arr2 = np.random.rand(10)*10 +1
arr2 = arr2.astype(int)
print(arr1)
print(arr2)


# In[42]:


print(arr1 + arr2)


# In[43]:


print(arr1*arr2)


# In[45]:


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [10,9,8,7,6,5,4,3,2,1]


# In[46]:


print(list1 + 1)


# In[47]:


print(list1 * 2)


# In[48]:


print(list1 / 2)


# In[49]:


print(list1 + list2)


# ### Lets work with some data

# In[56]:


import pandas as pd
data = np.array(pd.read_csv('populationbycountry19802010millions.csv'))
print(data)


# In[71]:


murica = data[0,1:]
murica = murica.astype(float)


# In[76]:


print('Mean = ', np.mean(murica))
print('Median = ', np.median(murica))
print('Max = ', np.amax(murica))


# ### Data Visualization

# In[78]:


import matplotlib.pyplot as plt


# In[86]:


time = np.arange(1980,2011,1)
plt.plot(time,murica)
plt.title('Population of North America 1980 - 2016')
plt.xlabel('Year')
plt.ylabel('Population in Millions')


# ### Quick Math Solving Ordinary Differential Equations(ODE's)

# An ordinary differential equation (ODE) is an equation containing an unknown function of one real or complex variable x, its derivatives, and some given functions of x. The unknown function is generally represented by a variable (often denoted y), which, therefore, depends on x

# In[95]:


from scipy.integrate import odeint


# ### Lotka-Voltera predator prey model
# ![image.png](attachment:image.png)

# In[127]:


def f(current, time, a, b, c, d):
    R = current[0]
    F = current[1]
    dR = a*R - b*R*F
    dF = -c*F + d*R*F
    return [dR,dF]


# In[146]:


initial_populations = [100, 20]
a = 7 #rabbit population growth rate
b = .5 #effectiveness of foxes preying on rabbits
c = 2 #intensity of competition between foxes for prey
d = .1 #overall benefit of catching a rabbit for foxes
args = (a,b,c,d)
time = np.arange(0,50,.5)


# In[147]:


populations = odeint(f, initial_populations, time, args)
rabbit_population = populations[:,0]
fox_population = populations[:,1]


# In[148]:


plt.plot(time, rabbit_population, label = 'rabbit')
plt.plot(time,fox_population, label = 'fox')
plt.legend()

