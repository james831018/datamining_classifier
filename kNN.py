#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


f=open('輸出.csv')
df = pd.read_csv(f)
X=df.drop('可投資',axis=1)
y = df["可投資"]


# 切分訓練與測試資料
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3)

# 建立分類器
knn = KNeighborsClassifier()
knn.fit(train_X, train_y)

# 預測
test_y_predicted = knn.predict(test_X)
#print(test_y_predicted)

# 標準答案
print(classification_report(test_y,test_y_predicted))
#print(dtree.score(test_X,test_y))

