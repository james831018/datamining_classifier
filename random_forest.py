#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
from sklearn import cross_validation, ensemble, preprocessing, metrics

f_test = open('輸出.csv')
df=pd.read_csv(f_test)

# 建立訓練與測試資料
X = df.drop('可投資',axis=1)
y = df["可投資"]
train_X, test_X, train_y, test_y = cross_validation.train_test_split(X, y, test_size = 0.3)

# 建立 random forest 模型
forest = ensemble.RandomForestClassifier(n_estimators = 100)
forest_fit = forest.fit(train_X, train_y)

# 預測
test_y_predicted = forest.predict(test_X)

# 績效
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print(metrics.classification_report(test_y,test_y_predicted))
print("accuracy：",accuracy)

