#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


ms = pd.read_csv ('AAPL.csv')


# In[3]:


ms.head()


# In[4]:


ms['Close'].plot(label="Closing Price")
plt.legend
plt.plot


# In[5]:


ms['MA10']=ms['Close'].rolling(10).mean()
ms['MA60']=ms['Close'].rolling(60).mean()


# In[6]:


ms.tail()


# In[7]:


ms['Close'].plot(label='Close')
ms['MA60'].plot(label='MA60')
ms['MA10'].plot(label='MA10')
plt.show
plt.legend()


# In[8]:


ms['Shares']=[1 if ms.loc[ei,'MA10']>ms.loc[ei,'MA60'] else 0 for ei in ms.index]


# In[9]:


ms['Close1']=ms['Close'].shift(-1)


# In[10]:


ms['Profit']=[ms.loc[ei,'Close1']-ms.loc[ei,'Close'] if ms.loc[ei,'Shares']==1 else 0 for ei in ms.index]


# In[11]:


ms['Profit'].plot(label='Profit')
plt.legend()
plt.show()


# In[12]:


ms['wealth']=ms['Profit'].cumsum()


# In[13]:


print('Total wealth created is',ms.loc[ms.index[-2],'wealth'])


# In[14]:


print('Total investment is',ms.loc[ms.index[0],'Close'])


# In[ ]:




