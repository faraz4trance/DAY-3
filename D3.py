#!/usr/bin/env python
# coding: utf-8

# In[6]:


#q1
import numpy as np
np.arange(2,50,3)


# In[27]:


#Q2
x = np.arange(5)
y = np.arange(5,10)
print(x)
print(y)
np.sort(x)
np.sort(y)
np.sort((x,y))


# In[32]:


#Q3
x = np.arange(4)
z = x.reshape(2,2)
print(z)
print(z.shape)
print(z.ndim)


# In[33]:


#Q5
x = np.arange(4)
y = np.arange(4,8)
print(x)
print(y)
np.hstack((x,y))
np.vstack((x,y))


# In[42]:


#Q6
x = np.arange(9)
y = np.arange(9,18)
print(x)
print(y)
np.concatenate((x, y))
np.concatenate((x,y),axis=1)


# In[46]:


#Q4
x = np.arange(4)
y = np.reshape(x, (2,2))
print(y)

