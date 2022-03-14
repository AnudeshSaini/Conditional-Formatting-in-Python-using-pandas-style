#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[5]:


detail = pd.read_csv("Sales Details.csv")


# In[8]:


order = pd.read_csv("Sales Orders.csv")


# In[9]:


# Merge both detail & order dataset on the basis of there order ID
sales = pd.merge(detail, order, on='Order ID', how='left')


# In[12]:


sales15 = sales.head(15)


# In[129]:


amount15 = sales15[["Amount","Profit","Quantity"]]


# ### 1. Change background color

# In[126]:


sales15.style.set_properties(**{"background-color":"aquamarine"} )


# ### 2. Change font color

# In[128]:


sales15.style.set_properties(**{"color":"darkblue"})


# ### 3. Change color of border

# In[42]:


sales15.style.set_properties(**{"border":"5px solid orange"} )


# ### 4. Hightlight maximum values ?

# In[101]:


amount15.style.highlight_max(color= "aqua")


# ### 5. Hightlight minimum values ?

# In[103]:


amount15.style.highlight_min(color= "aqua")


# ### 6. Create heatmap within dataframe

# In[110]:


amount15.style.background_gradient()


# ### 7. Create bar charts

# In[115]:


amount15.style.bar(subset=["Amount","Profit","Quantity"], color="pink")


# ### 8. Add captions

# In[122]:


sales15.style.set_caption("This is Anudesh Saini Blog")


# In[ ]:




