#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
get_ipython().run_line_magic('matplotlib', '')

f = open('輸出.csv')
df = pd.read_csv(f)


# 切分訓練與測試資料
X = df.drop('可投資',axis=1)
y = df['可投資']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=101)


# 建立分類器
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)


# 預測
predictions = dtree.predict(X_test)


# 標準答案
print(classification_report(y_test,predictions))
print(dtree.score(X_test,y_test))

#產生可視圖
from sklearn import tree
with open("iris.dot", 'w') as f2:
    f2 = tree.export_graphviz(dtree, out_file=f2)

