#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


import matplotlib.pyplot as plt 


# In[4]:


air = pd.read_csv("C:/Users/eslam/Desktop/pandas-master/doc/data/air_quality_no2.csv", index_col=0, parse_dates=True)


# In[5]:


air


# In[6]:


air.plot()


# In[7]:


air["station_paris"].plot()


# In[8]:


air.plot.scatter(x="station_london" , y="station_paris" , alpha=0.5)


# In[9]:


air.plot(x="station_london" , y="station_paris" , alpha=0.5)


# In[10]:


[
    method_name
    for method_name in dir(air.plot)
    if not method_name.startswith("_")
]


# In[11]:


air.plot.box()


# In[12]:


axs = air.plot.area(figsize=(8 , 3) , subplots=True )


# In[13]:


axs = air.plot.area( subplots=True )
axs.set_ylabel("station")
axs.show()


# In[14]:


air


# In[15]:


air["station_cairo"]=air["station_paris"] *2.5487


# In[16]:


air


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




