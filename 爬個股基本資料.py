#!/usr/bin/env python
# coding: utf-8

# In[136]:


import requests
import csv
import time
from bs4 import BeautifulSoup


file1=open('上市公司.csv',newline='',encoding = 'utf8')
reader=csv.reader(file1)
company=[]
for row in reader:
    #print(row[1])
    company.append(row[1])
    
    
#寫入個股基本資訊
file2= open('個股基本資訊6.csv','w',newline='',encoding = 'big5')
writer=csv.writer(file2)


# In[110]:


for c in company[1:2]:
    url="http://jsjustweb.jihsun.com.tw/z/zc/zca/zca_"+c+".djhtm"
    print(c,url)
    res=requests.get(url)
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(c)
    
    if c=='1101':
        print("in c")
        title=['公司代碼']
        for tag in soup.find_all("td", class_="t4t1"):
            title.append(tag.text)
        writer.writerow(title)
    
    data=[c]
    for tag in soup.find_all("td", class_="t3n1"):
        data.append(tag.text)
    writer.writerow(data)
    
    
    
    time.sleep( 5 )





file1.close()
file2.close()


# In[137]:


for c in company[1:]:
    url="http://jsjustweb.jihsun.com.tw/z/zc/zca/zca_"+c+".djhtm"
    print(c,url)
    res=requests.get(url)
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(c)
    
    if c=='1101':
        print("in c")
        title=['公司代碼']
        for tag in soup.find_all("td", class_="t4t1"):
            title.append(tag.text)
        writer.writerow(title)
    
    data=[c]
    for tag in soup.find_all("td", class_="t4t1"):
        data.append(tag.findNext('td').text.replace(u'\xa0', u' '))
        #print(tag.text,tag.findNext('td').text)
    writer.writerow(data)
    
    
    
    time.sleep( 5 )





file1.close()
file2.close()


# In[138]:


file1.close()
file2.close()


# In[ ]:




