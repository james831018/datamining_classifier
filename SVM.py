#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[54]:


import numpy as np
import pandas as pd
from sklearn import cross_validation, svm, preprocessing, metrics
#from sklearn.metrics import classification_report,confusion_matrix

# 載入資料
f=open('輸出.csv')
df = pd.read_csv(f)

# 切分訓練與測試資料
X=df.drop('可投資',axis=1)
y = df["可投資"]
train_X, test_X, train_y, test_y = cross_validation.train_test_split(X, y, test_size = 0.3)

# 建立 SVC 模型
svc = svm.SVC()
svc_fit = svc.fit(train_X, train_y)

# 預測
test_y_predicted = svc.predict(test_X)

# 績效
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print(accuracy)
print(classification_report(test_y,test_y_predicted))

