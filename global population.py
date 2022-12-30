#!/usr/bin/env python
# coding: utf-8

# In[27]:


"""
this is a data cleaning and data exploration protect on the global population
data set gotten from kaggle using python

"""

import numpy as np
import pandas as pd
import os


# In[28]:


os.getcwd()       #get current working directory


# In[29]:


os.listdir()     #a list of the elememnts on the directory.
os.listdir('C:\\Users\\DELL\\Desktop\\DA files')
global_pop = pd.read_csv('C:\\Users\\DELL\\Desktop\\DA files\\Global_annual_population.csv')   #read csv file


# In[35]:


global_pop
global_pop.head(7)


# In[36]:


global_pop.shape  # the dimension of the dataset


# In[37]:


# determine the various variable and what type of data they contain.
global_pop.info()


# In[38]:


# to get a summary statistics of every column 
global_pop.describe()

"""
    this shows that there are a total of 62 enteries(count)
    the min year being 1960,  max is 2021
    
   """


# In[39]:


del global_pop['Unnamed: 2']


# In[40]:


global_pop


# ## this data set have been cleaned and every unnecessary data have been deleted.

# In[ ]:




