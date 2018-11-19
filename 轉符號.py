#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import pandas as pd


# In[11]:


f1=open('轉符號.csv', 'r',newline='')
f2=open('轉符號1.csv','w',newline='')
#f2=open('iris.csv', newline='','r')
rows=csv.reader(f1)
writer = csv.writer(f2)
for row in rows:
    newrow=[]
    for j in row:
        #print(j)
        if j!='':
            j=j.replace(',','')
            j=j.replace('%','')
            j=j.replace('N/A','0')
            j=float(j)
        else:
            j=0
        #j=j.replace(',','')
        newrow.append(j)
    print(newrow)
    writer.writerow(newrow)
    #print(row)


# In[12]:


f1.close()
f2.close()


# In[ ]:




