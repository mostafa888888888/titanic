#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


data=pd.read_csv('D:\program\python\Titanic-Dataset.csv')
data.head()


# In[50]:


data.info()


# In[51]:


sns.countplot('Sex',data=data)


# In[52]:


data.drop(['PassengerId','Name'],axis='columns', inplace=True)


# In[53]:


data


# In[54]:


sns.countplot('Age',data=data)


# In[81]:


def male_female(passenger):
    age,sex=passenger
    
    if age<16:
        return 'child'
    else:
        return sex


# In[82]:


data['person']=data[['Age','Sex']].apply(male_female,axis=1)


# In[87]:


data.head(10)


# In[88]:


sns.countplot('Pclass',data=data,hue='person')


# In[91]:


data['Age'].hist(bins=90)


# In[92]:


data['Age'].mean()


# In[93]:


data['person'].value_counts()


# In[94]:


sns.countplot('Embarked',data=data)


# In[95]:


data.head()


# In[ ]:


data['alone']=data['SibSp']+data['Parch']


# In[117]:


data


# In[118]:


data['alone'].loc[data['alone']>0]='with family'
data['alone'].loc[data['alone']==0]='ALONE'


# In[119]:


data


# In[120]:


sns.countplot('alone',data=data)


# In[121]:


data['Survived'].loc[data['Survived']>0]='life'
data['Survived'].loc[data['Survived']==0]='died'


# In[122]:


data


# In[123]:


sns.countplot('Survived',data=data)


# In[124]:


sns.countplot('Survived',data=data,hue='Pclass')


# In[ ]:




