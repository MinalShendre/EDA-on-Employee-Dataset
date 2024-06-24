#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


dataset=pd.read_excel('c:\\users\\Employee_Data.xls')


# In[5]:


dataset.isnull().sum()


# In[6]:


dataset


# In[7]:


x=dataset.iloc[:,3:6].values


# In[8]:


x


# In[9]:


from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values="NaN",strategy='mean')
imputer=SimpleImputer().fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)


# In[10]:


from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values="NaN",strategy='median')
imputer=SimpleImputer().fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)


# In[11]:


from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values="NaN",strategy='most_frequent')
imputer=SimpleImputer().fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


data=pd.read_csv('c:\\users\\Placement.csv')


# In[7]:


data


# In[8]:


data.head() #snapshot of the data (starting ke 5 rows)


# In[9]:


print(data.columns.values) #heading of the column


# In[10]:


print('='*50)
print("Describe data")
print('='*50)
print(data.describe())


# In[ ]:


#as it is clear that we dont need sl_no in training model or in EDA.thus I am


# In[11]:


data=data.drop(['sl_no'],axis=1) #1=column 0=row


# In[ ]:


#Exploring important features


# In[12]:


sns.countplot(x='status', data=data)


# In[13]:


data['gender'].value_counts()


# In[14]:


df=pd.DataFrame(data.groupby(['gender','status'])['status'].count())
df


# In[15]:


sns.countplot(x='gender',hue='status',data=data) #hue is used to introduced additional categorical variable


# In[ ]:


#conclusion: male have higher chances of getting placed compared to females


# In[ ]:


#ssc percentage


# In[16]:


sns.distplot(data['ssc_p'])
plt.title('Distribution of ssc percentage')
plt.xlabel('SSC %')


# In[17]:


sns.catplot(y='ssc_p',x='status',data=data)
plt.xlabel('Employment Status')
plt.ylabel('SSC %')


# In[18]:


data['ssc_b'].value_counts()


# In[39]:


df=pd.DataFrame(data.groupby(['ssc_b','status'])['status'].count())
df


# In[40]:


sns.countplot(x='ssc_b',hue='status',data=data)


# In[ ]:


#from the above analysis ,ssc board is not that important to recriters when it come to hiring candidate.


# In[ ]:


#HSC percentage


# In[42]:


sns.distplot(data['hsc_p'],kde=False)
plt.title('Distribution of HSC percentage')
plt.xlabel('HSC %')


# In[46]:


sns.catplot(y='hsc_p',x='status',data=data)
plt.xlabel('Employment Status')
plt.ylabel('HSC %')


# In[19]:


data['hsc_b'].value_counts()


# In[20]:


df=pd.DataFrame(data.groupby(['hsc_b','status'])['status'].count())
df


# In[21]:


sns.countplot(x='hsc_b',hue='status',data=data)


# In[22]:


data['hsc_s'].value_counts()


# In[23]:


df=pd.DataFrame(data.groupby(['hsc_s','status'])['status'].count())
df


# In[24]:


sns.countplot(x='hsc_s',hue='status',data=data)


# In[ ]:


#Degree percentage


# In[25]:


sns.displot(data['degree_p'],kde=False)
plt.title('Distribution of Degree Percentage')
plt.xlabel('Degree %')


# In[ ]:


#work experience


# In[26]:


data['workex'].value_counts()


# In[27]:


df=pd.DataFrame(data.groupby(['workex','status'])['status'].count())
df


# In[28]:


sns.countplot(x='workex',hue='status',data=data)


# In[ ]:


#corelation between features


# In[32]:


sns.pairplot(data=data[['ssc_p','hsc_p','degree_p','salary','status']],hue='status',diag_kind='hist')


# In[44]:


data.drop(['ssc_b','hsc_b','hsc_s','degree_t','salary'],axis=1,inplace=True)


# In[41]:


data["gender"]=data.gender.map({"M":0,"F":1})
data["workex"]=data.workex.map({"No":0,"Yes":1})
data["status"]=data.status.map({"Not Placed":0,"Placed":1})
data["specialisation"]=data.specialisation.map({"Mkt&HR":0,"Mkt&Fin":1})


# In[42]:


data.columns


# In[43]:


data.head()


# In[ ]:





# In[ ]:





# In[ ]:




