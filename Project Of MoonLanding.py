#!/usr/bin/env python
# coding: utf-8

# # MoonLanding_Project:

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


mn = pd.read_csv('C:/Users/Ranje/OneDrive/Desktop/Excel/Moonlanding.csv')


# In[3]:


mn


# In[4]:


mn.shape


# In[5]:


mn.head()


# In[6]:


mn.head(10)


# In[7]:


mn.tail(10)


# In[8]:


mn.isnull()


# In[9]:


mn.isnull().sum()


# In[10]:


mn.isnull().count()


# In[11]:


mn.notnull()


# In[12]:


mn.dtypes


# In[13]:


#Access a particular column
mn.Mission


# In[14]:


mn.Mission.head(20)


# In[15]:


mn.Mission.tail(15)


# In[16]:


mn.Mission.tail(20).isnull()


# In[17]:


mn.Mission.tail(20).isnull().sum()


# In[18]:


#2nd method to access column 
mn['Spacecraft']


# In[19]:


mn['Spacecraft'].sample(30)


# In[20]:


mn['Spacecraft'].tail(30)


# In[21]:


mn['Spacecraft'].tail(30).notnull()


# In[22]:


mn['Spacecraft'].tail(30).notnull().sum()


# In[23]:


mn.iloc[20:50]


# In[24]:


mn.iloc[:,[0,5]]


# In[25]:


mn.iloc[:,[0,5]].head(30)


# In[26]:


mn.iloc[:,[0,5]].head(30).isnull().sum()


# In[27]:


mn.iloc[:,[0,5]].head(30).isnull().count()


# In[28]:


mn.iloc[:,[0,5]].head(30).isnull().mode()


# In[29]:


mn.head()


# In[30]:


mn.iloc[15:40,[0,2,5]]


# In[31]:


mn.iloc[15:40,[0,2,5]].notnull()


# In[32]:


mn.iloc[15:40,[0,2,5]].notnull().sum()


# In[33]:


mn.loc[:,['Launch Date','Mission Type','Mission']]


# In[34]:


mn.loc[:,['Launch Date','Mission Type','Mission']].head(10)


# In[35]:


mn.loc[:,['Launch Date','Mission Type','Mission']].isnull().sum()


# In[36]:


mn.loc[20:45,['Launch Date','Mission Type','Mission']]


# In[37]:


mn.loc[20:45,['Launch Date','Mission Type','Mission']].notnull()


# In[38]:


mn.loc[20:45,['Launch Date','Mission Type','Mission']].notnull().sum()


# In[39]:


#Access a particular rows uusing iloc...

mn.iloc[[10,15,20]]


# In[40]:


mn.iloc[10:15,0:3]


# In[41]:


mn.Spacecraft == 'Luna 2'


# In[42]:


mn.Spacecraft.loc[mn.Spacecraft == 'Luna 2'].count()


# In[43]:


mn.Spacecraft.loc[mn.Spacecraft == 'Luna 2'].isnull()


# In[44]:


mn.Spacecraft.loc[mn.Spacecraft == 'Luna 2'].isnull().sum()


# In[45]:


mn.Spacecraft.loc[mn.Spacecraft == 'Luna 2'].isnull().count()


# In[46]:


mn.Spacecraft.loc[(mn.Spacecraft == 'Luna 2') & (mn.Operator == 'Soviet Union OKB-1')]


# In[47]:


mn.Spacecraft.loc[(mn.Spacecraft == 'Luna 2') | (mn.Operator == 'Soviet Union OKB-1')]


# In[48]:


mn


# In[49]:


m1 = np.array([10,4,60,3,6,30,20,19,34,21,46,49,39,20,34,23,87])
print(m1)


# In[50]:


mn['Operator']


# In[51]:


mn['Operator'].head(30)


# In[52]:


mn = mn.loc[mn.Operator == 'United States NASA']


# In[53]:


mn


# In[54]:


mn = mn.loc[mn.Operator == 'United States NASA'].isnull().sum()
mn


# In[56]:


mn.loc[:,'Operator']


# In[ ]:


mn.iloc[:,4]


# In[ ]:





# In[4]:


plt.figure(figsize =(50, 50))
plt.plot(mn['Carrier Rocket'],mn['Spacecraft'],lw=10,color='b',marker='*')
plt.title('Carrier Rocket V/S Spacecraft',fontsize = 30,fontweight = 'bold')
plt.gca().set_facecolor('#000040')
plt.yticks(fontsize = 12,rotation=45)
plt.show()


# In[ ]:





# In[5]:


plt.figure(figsize =(50, 50))
plt.plot(mn['Mission'],mn['Outcome'],lw=10,color='c',marker='X')
plt.gca().set_facecolor('#000020')
plt.title('Mission V/S Outcome',fontsize = 40,fontweight = 'bold')
plt.yticks(fontsize = 30,rotation=45)
plt.show()


# In[6]:


plt.figure(figsize =(50, 40))
plt.plot(mn['Launch Date'],mn['Outcome'],lw=10,color='r',marker='X')
plt.gca().set_facecolor('#000090')
plt.title('Launch Date V/S Outcome',fontsize = 40,fontweight = 'bold')
plt.yticks(fontsize = 30,rotation=45)
plt.show()


# In[7]:


plt.figure(figsize =(50, 40))
plt.stem(mn['Mission'],mn['Outcome'],linefmt = 'c')
plt.gca().set_facecolor('#000000')
plt.title('Mission V/S Outcome',fontsize = 40,fontweight = 'bold')
plt.yticks(fontsize = 30,rotation=45)
plt.show()


# In[8]:


plt.figure(figsize =(60, 50))
plt.stem(mn['Operator'],mn['Mission'],linefmt = 'y')
plt.gca().set_facecolor('#000000')
plt.title('Operator V/S Mission',fontsize = 40,fontweight = 'bold')
plt.yticks(fontsize = 30,rotation=45)
plt.show()


# In[ ]:




