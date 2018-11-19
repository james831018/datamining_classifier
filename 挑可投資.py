#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
#f=open('個股基本資訊4.csv','r',newline='')
#f2=open('個股基本資訊5.csv','w',newline='')


# In[5]:


f_test = open('轉符號1.csv')
df=pd.read_csv(f_test)


# In[ ]:





# In[6]:


df


# In[7]:


print(df.mean())


# In[8]:


print(df['本益比'].mean())


# In[14]:


count=0
for i in range(0,len(df)):
    if df['本益比'][i]<=df['本益比'].mean() and df['貝他值'][i]<=df['貝他值'].mean() and df['殖利率'][i]<=df['殖利率'].mean()and df['今年以來'][i]<=df['今年以來'].mean()and df['營業毛利率'][i]<=df['營業毛利率'].mean():
        print(df[i:i+1])
        count+=1
        df['可投資'][i]='是'
    else:
        df['可投資'][i]='否'
    #print(df['本益比'].mean())
print(count)
#df['新']=1


# In[15]:


df.to_csv('輸出.csv',index=False,encoding='big5')


# In[ ]:




