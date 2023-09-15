#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df=pd.read_csv("archive\CarPrice_Assignment.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df["car_ID"].count()


# In[6]:


df=df.drop("car_ID",axis=1)


# In[7]:


df["symboling"].isna().sum()


# In[8]:


df["symboling"].unique()


# In[9]:


df["CarName"].isna().sum()


# In[10]:


df["CarName"].unique()


# In[11]:


df["carname"]=(df["CarName"].str.split(" ").str[0])


# In[12]:


df["carname"].unique()


# In[13]:


df[df["carname"]=="porcshce"]


# In[14]:


names=({"Nissan":"nissan","maxda":"mazda","porcshce":"porsche","toyouta":"toyota","vokswagen":"volkswagen","vw":"volkswagen"})


# In[15]:


df["carname"]=df["carname"].replace(names)


# In[16]:


df["carname"].unique()


# In[17]:


df.head()


# In[18]:


df=df.drop("CarName",axis=1)


# In[19]:


df["fueltype"].isna().sum()


# In[20]:


df["fueltype"].unique()


# In[21]:


df["aspiration"].unique()


# In[22]:


df["aspiration"].isna().sum()


# In[23]:


df["doornumber"].isna().sum()


# In[24]:


df["doornumber"].unique()


# In[25]:


df["carbody"].isna().sum()


# In[26]:


df["carbody"].unique()


# In[27]:


df.isna().sum()


# In[28]:


df.describe()


# In[29]:


df.info()


# In[30]:


df["cylindernumber"].value_counts()


# In[31]:


df["aspiration"].value_counts()


# In[32]:


df["fueltype"].value_counts()


# In[33]:


df["enginetype"].value_counts()


# In[34]:


df["fuelsystem"].value_counts()


# In[35]:


df["boreratio"].value_counts()


# In[36]:


df["doornumber"].value_counts()


# In[37]:


df["carbody"].value_counts()


# In[38]:


df["carname"].value_counts()


# In[39]:


cleanup_nums = {"aspiration":     {"std": 0, "turbo": 1},
                "fueltype": {"gas": 0, "diesel": 1},
               "doornumber": {"four":4, "two":2},
               "carbody": {"sedan":0, "hatchback":1 ,"wagon" :2,"hardtop":3,"convertible":4}}


# In[40]:


df=df.replace(cleanup_nums)


# In[41]:


df.head()


# In[42]:


from sklearn.preprocessing import LabelEncoder


# In[43]:


le=LabelEncoder()


# In[44]:


df["carname"] = le.fit_transform(df["carname"])
df.head()


# In[45]:


df["drivewheel"] = le.fit_transform(df["drivewheel"])


# In[46]:


df["enginelocation"] = le.fit_transform(df["enginelocation"])


# In[47]:


df["enginetype"] = le.fit_transform(df["enginetype"])


# In[48]:


df["fuelsystem"] = le.fit_transform(df["drivewheel"])


# In[49]:


df["cylindernumber"] = le.fit_transform(df["cylindernumber"])


# In[50]:


df.head()


# In[51]:


df.info()


# In[52]:


df=df.astype(float)


# In[53]:


y=df["price"]


# In[54]:


y=y.astype("int")


# In[55]:


y.head()


# In[56]:


x=df.drop("price",axis=1)


# In[57]:


x.head()


# In[58]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=10)


# In[59]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[60]:


from sklearn.preprocessing import StandardScaler


# In[61]:


scaler=StandardScaler()


# In[62]:


x_train=scaler.fit_transform(x_train)


# In[63]:


x_test=scaler.transform(x_test)


# In[64]:


from sklearn.tree import DecisionTreeRegressor


# In[65]:


regressor=DecisionTreeRegressor()


# In[66]:


regressor.fit(x_train,y_train)


# In[67]:


y_pred_test=regressor.predict(x_test)


# In[68]:


y_pred_test


# In[69]:


from sklearn.metrics import mean_squared_error,mean_absolute_error


# In[70]:


mse=mean_squared_error(y_test,y_pred_test)
mae=mean_absolute_error(y_test,y_pred_test)
rmse=np.sqrt(mse)


# In[71]:


mse,mae,rmse


# In[72]:


from sklearn.metrics import r2_score


# In[73]:


score=r2_score(y_test,y_pred_test)


# In[74]:


score


# In[ ]:




