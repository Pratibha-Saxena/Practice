#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pickle as pkl


# In[3]:


A = pd.read_csv("50_Startups.csv")


# In[4]:


X = A[["RND", "MKT"]]
y = A[["PROFIT"]]


# In[5]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model = lr.fit(X, y)


# In[6]:


pkl.dump(model, open("model.pkl", "wb"))


# In[7]:


model = pkl.load(open("model.pkl", "rb"))


# In[ ]:





# In[ ]:




