#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df=pd.read_csv("archive (1)\Iris.csv")


# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.drop("Id",axis=1,inplace=True)


# In[7]:


df.tail()


# In[8]:


ax = sns.boxplot(df['SepalLengthCm'])


# In[9]:


ax = sns.boxplot(df['SepalWidthCm'])


# In[10]:


df[df["SepalWidthCm"]>4]


# In[11]:


df[df["SepalWidthCm"]<=2]


# In[12]:


df.drop(index=[15,32,33,60],inplace=True)


# In[13]:


df[0:16][:]


# In[14]:


df=df.reset_index()


# In[15]:


df[0:16][:]


# In[16]:


df=df.reset_index()


# In[17]:


df[0:16][:]


# In[18]:


df.drop("index",axis=1,inplace=True)


# In[19]:


ax = sns.boxplot(df['SepalWidthCm'])


# In[20]:


ax=sns.boxplot(df['PetalLengthCm'])


# In[21]:


ax=sns.boxplot(df['PetalWidthCm'])


# In[22]:


df.isna().sum()


# In[23]:


df.head()


# In[24]:


y=df["Species"]


# In[25]:


x=df.drop("Species",axis=1)


# In[26]:


x.head()


# In[27]:


y.head()


# In[28]:


from sklearn.model_selection import train_test_split


# In[29]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=43)


# In[30]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[31]:


from sklearn.preprocessing import StandardScaler


# In[32]:


ss=StandardScaler()


# In[33]:


x_train=ss.fit_transform(x_train)


# In[34]:


x_test=ss.transform(x_test)


# In[35]:


from sklearn.svm import SVC


# In[36]:


sv=SVC()


# In[37]:


model=sv.fit(x_train,y_train)


# In[38]:


y_predicted=sv.predict(x_test)


# In[39]:


from sklearn.metrics import accuracy_score


# In[40]:


score=accuracy_score(y_test,y_predicted)


# In[41]:


score


# In[ ]:




