import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#plt.rcParams["figure.figsize"] = (20,10)

from sklearn.model_selection import KFold, train_test_split,cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder

path_dataset=r'dataset/indian_liver.csv'
models=[('Logistic Regression', LogisticRegression()), 
          ('Support Vector Machine', SVC()), 
          ('Decision Tree', DecisionTreeClassifier()),
          ('K-Nearest Neighbors', KNeighborsClassifier()),
          ('Linear Discrimination', LinearDiscriminantAnalysis()),
          ('Gaussian Naive Bayes', GaussianNB())]
random_seed = 12

def DeleteColumns(dataframe,columns):
	for column in columns:
		del dataframe[column]
	return dataframe

def CleanData(dataframe):
	dataframe.dropna(inplace=True)
	dataframe['Liver_disease'] = dataframe['Liver_disease'] - 1 
	label=LabelEncoder()
	label.fit(dataframe['Is_male'])
	dataframe['Is_male'] = label.transform(dataframe['Is_male'])
	return dataframe,label

def ToDataframe(file):
	dataframe=pd.read_csv(file)
	dataframe=dataframe.rename(columns={'Dataset':'Liver_disease','Gender':'Is_male'})
	print(dataframe.columns)
	return dataframe

def GetColumns(dataframe):
	return list(dataframe.columns)

def setX_setY(dataframe,columnY):
	Y=dataframe[[columnY]]
	del dataframe[columnY]
	X=dataframe
	return X,Y

def GetModelsAvailable():
	mod_av=[]
	for model in models:
		mod_av.append(model[0])
	return mod_av

def TrainModel(ch_model,per_test,X,y):
	fun=None
	for model in models:
		if model[0]==ch_model:
			fun=model[1]
	X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=per_test, random_state=42)
	modelo=fun.fit(X_train,y_train)
	y_pred=modelo.predict(X_test)
	accuracy=accuracy_score(y_test,y_pred)
	return modelo,accuracy

def Predict(model,X):
	result=model.predict(X)
	return result

def KfoldValidation():
	outcome=[]
	model_names=[]
	for model_name, model in models:
	    k_fold_validation = KFold(n_splits=10, random_state=random_seed)
	    results = cross_val_score(model, X, Y, cv=k_fold_validation, scoring='accuracy')
	    outcome.append(results)
	    model_names.append(model_name)
	    output_message = "%s| Mean=%f STD=%f" % (model_name, results.mean(), results.std())
	    print(output_message)

def GetMetrics():
	return False


# values = data_to_use.values
# Y = values[:,9]
# X = values[:,0:9]
# random_seed = 12

# outcome=[]
# model_names=[]
# models=[('LogReg', LogisticRegression()), 
#           ('SVM', SVC()), 
#           ('DecTree', DecisionTreeClassifier()),
#           ('KNN', KNeighborsClassifier()),
#           ('LinDisc', LinearDiscriminantAnalysis()),
#           ('GaussianNB', GaussianNB())]

#print(models[0])
# for model_name, model in models:
#     k_fold_validation = KFold(n_splits=10, random_state=random_seed)
#     results = cross_val_score(model, X, Y, cv=k_fold_validation, scoring='accuracy')
#     outcome.append(results)
#     model_names.append(model_name)
#     output_message = "%s| Mean=%f STD=%f" % (model_name, results.mean(), results.std())
#     print(output_message)

# fig = plt.figure()
# fig.suptitle('Machine Learning Model Comparison')
# ax = fig.add_subplot(111)
# plt.boxplot(outcome)
# ax.set_xticklabels(model_names)
# plt.show()

#test fucntions
# df=ToDataframe(path_dataset)
# df=DeleteColumn(df,'Gender')
# df_clean=CleanData(df)
# print(GetColumns(df_clean))
# columnY='Dataset'
# X,Y=setX_setY(df_clean,columnY)
# modelos=['LogReg','SVM','DecTree','KNN','LinDisc','GaussianNB']
# for modelo in modelos:
# 	TrainModel('DecTree',0.3,X,Y)
# 	print('\n')
