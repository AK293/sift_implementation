#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt


# In[2]:


img = cv.imread('images/eiffel_tower.JPG')
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
dimensions = img.shape
print('Image Dimensions:',dimensions)


# In[3]:


img = cv.imread('images/eiffel_tower.JPG')
dimensions = img.shape
print('Image Dimensions:',dimensions)


# In[4]:


img = cv.imread('/eiffel_tower.JPG')
dimensions = img.shape
print('Image Dimensions:',dimensions)


# In[5]:


img = cv.imread('/eiffel_tower.JPG')
dimensions = img.shape
print('Image Dimensions:',dimensions)


# In[6]:


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt


# In[11]:


img = cv.imread('eiffel_tower.JPG')
dimensions = img.shape
print('Image Dimensions:',dimensions)


# In[12]:


#Defining the default parameter values
k = sqrt(2)
oct_max = 8 #number of octaves
spo = 3 #scales per octave
sigma_input = 0.5
sigma_min = 0.8


# In[15]:


get_ipython().run_line_magic('notebook', '"Coding/sift/sift_implementation/implementation.ipynb"')

