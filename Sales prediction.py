#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[3]:


df=pd.read_csv("archive (2)\Advertising.csv")


# In[4]:


df.head()


# In[5]:


df.drop("Unnamed: 0",axis=1,inplace=True)


# In[6]:


df.head()


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


ax = sns.boxplot(df['TV'])


# In[10]:


ax = sns.boxplot(df['Radio'])


# In[11]:


ax = sns.boxplot(df['Newspaper'])


# In[12]:


df[df["Newspaper"]>=100]


# In[13]:


df[0:17][:]


# In[14]:


df=df.reset_index()


# In[15]:


df[0:17][:]


# In[16]:


ax=sns.boxplot(df["Newspaper"])


# In[17]:


df.isna().sum()


# In[18]:


df.head()


# In[19]:


df.drop("index",axis=1,inplace=True)


# In[20]:


df.head()


# In[21]:


y=df["Sales"]


# In[22]:


x=df.drop("Sales",axis=1)


# In[23]:


x.head()


# In[24]:


y.head()


# In[25]:


from sklearn.model_selection import train_test_split


# In[26]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=43)


# In[27]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[28]:


from sklearn.preprocessing import StandardScaler


# In[29]:


ss=StandardScaler()


# In[30]:


x_train=ss.fit_transform(x_train)


# In[31]:


x_test=ss.transform(x_test)


# In[32]:


from sklearn.tree import DecisionTreeRegressor


# In[33]:


dt=DecisionTreeRegressor()


# In[34]:


model=dt.fit(x_train,y_train)


# In[35]:


y_predicted=dt.predict(x_test)


# In[36]:


from sklearn.metrics import r2_score


# In[37]:


score=r2_score(y_test,y_predicted)


# In[38]:


score


# In[ ]:




