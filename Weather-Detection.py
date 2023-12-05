#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\ravi\Downloads\Weather Data.csv")


# In[3]:


data 


# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.index


# In[7]:


data.columns


# In[8]:


data.dtypes


# In[9]:


data['Weather'].unique()


# In[10]:


data.nunique()


# In[11]:


data.count()


# In[12]:


data['Weather'].value_counts()


# In[13]:


data.info()


# In[14]:


data.head(2)


# In[15]:


data.nunique()


# In[16]:


data['Wind Speed_km/h'].nunique()


# In[17]:


data['Wind Speed_km/h'].unique()


# In[18]:


# value_counts()
data.Weather.value_counts()


# In[19]:


#Filtering
data.head(2)


# In[20]:


#Filtering
#data.head(2)
data.Weather == 'Clear'


# In[21]:


#Filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[22]:


#groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')


# In[23]:


data.head(2)


# In[24]:


data['Wind Speed_km/h']==4


# In[25]:


data[data['Wind Speed_km/h']==4] #Answer


# In[26]:


data.isnull()


# In[27]:


data.isnull().sum()


# In[28]:


data.notnull().sum()


# In[29]:


data.head(2)


# In[30]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# In[31]:


data.rename(columns = {'Weather' : 'Weather Condition'},inplace = True)


# In[32]:


data.head()


# In[33]:


data.head(2)


# In[34]:


data.Visibility_km.mean()


# In[35]:


data.Press_kPa.std()


# In[36]:


data['Rel Hum_%'].var()


# In[37]:


# value_counts()
data.head(2)


# In[38]:


# value_counts()
# data.head(2)
data['Weather Condition'].value_counts()


# In[39]:


#Filtering
data[data['Weather Condition']=='Snow']


# In[40]:


#str.constains
data[data['Weather Condition'].str.contains('Snow')]


# In[41]:


#str.constains
data[data['Weather Condition'].str.contains('Snow')].head(50)


# In[42]:


#str.constains
data[data['Weather Condition'].str.contains('Snow')].tail(50)


# In[43]:


data.head(2)


# In[44]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# In[45]:


data.head(2)


# In[46]:


data.groupby('Weather Condition').mean()


# In[47]:


data.head(2)


# In[48]:


data.groupby('Weather Condition').min() 


# In[49]:


data.groupby('Weather Condition').max()


# In[50]:


data[data['Weather Condition']=='Fog']


# In[51]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# In[52]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].head(50)


# In[53]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].tail(50)


# In[54]:


data.head(2)


# In[55]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%']>50) |(data['Visibility_km']>40)]


# In[ ]:




