# -*- coding: utf-8 -*-
"""DecisionTree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UdtBaHwYqPsppJalq-dNSt9k2xq2lhqB
"""

import pandas as pd
df=pd.read_csv("diabetes.csv")

df.head()

df.shape

df.isnull().sum()

X=df.iloc[:,:-1].to_numpy()
y=df.iloc[:,-1].to_numpy()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(random_state=0)
clf.fit(X_train,y_train)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.tree import plot_tree

plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()

clf.set_params(max_depth=3)

clf.fit(X_train,y_train)
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()

predictions=clf.predict(X_test)

clf.predict([[90,20],[200,30]])

from sklearn.model_selection import cross_val_score

scores=cross_val_score(clf,X_train,y_train,cv=5,scoring='accuracy')
accuracy=scores.mean()
accuracy

from sklearn import metrics
cf=metrics.confusion_matrix(y_test,predictions)
cf

tp=cf[1][1]
tn=cf[0][0]
fp=cf[0][1]
fn=cf[1][0]
print(f"tp:{tp}, tn:{tn},fp:{fp},fn:{fn}")

print("accuracy",metrics.accuracy_score(y_test,predictions))

print("Precision",metrics.precision_score(y_test,predictions))

print("Recall",metrics.recall_score(y_test,predictions))

feature_importances = clf.feature_importances_
print("Feature importances:",feature_importances)

