import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import numpy as np
import pandas as pd
from sklearn import linear_model


df = pd.read_csv('titanic2.csv')
numeric_df = df.select_dtypes(include=[float, int])
mat=numeric_df.corr()



x=df[['PassengerId']]
y=df['Survived']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.9)



print("Random Forest")
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
model=RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train,y_train)
print("predict data:",model.predict(x_test))
print("actual data",list(y_test))
print('model accuracy',model.score(x_test,y_test))



print("SVM")
model=sklearn.svm.SVC()
model.fit(x_train,y_train)
print("predict data:",model.predict(x_test))
print("actual data",list(y_test))
print('model accuracy',model.score(x_test,y_test))


print("Decision Tree")
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
print("predict data:",model.predict(x_test))
print("actual data",list(y_test))
print('model accuracy',model.score(x_test,y_test))


print("Logistic Regression")
model=linear_model.LogisticRegression()
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("predict data:",model.predict(x_test))
print("actual data",list(y_test))
print('model accuracy',model.score(x_test,y_test))



print("KNN")
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3, metric='euclidean')
model.fit(x_train,y_train)
print("predict data:",model.predict(x_test))
print("actual data",list(y_test))
print('model accuracy',model.score(x_test,y_test))




sns.heatmap(mat, annot=True, cmap='coolwarm')
plt.show()
