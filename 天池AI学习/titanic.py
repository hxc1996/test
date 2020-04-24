from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

#训练集交叉验证，得到平均值
#from sklearn.cross_validation import KFold
from sklearn.model_selection import KFold

pd.set_option('display.max_columns', None)
color = sns.color_palette()
pd.set_option('precision',3)

df_test = pd.read_csv('D:\\DataSet\\titanic_test.csv')
df_train = pd.read_csv('D:\\DataSet\\titanic_train.csv')

df_train["Age"] = df_train['Age'].fillna(df_train['Age'].median())

predictors = ["Pclass","Age","SibSp","Parch","Fare"]
alg = LinearRegression()
#样本平均分成3份，3折交叉验证
#kf = KFold(data_train.shape[0],n_folds=3,random_state=1)
kf = KFold(n_splits=3,shuffle=False,random_state=1)

predictions = []
for train,test in kf.split(df_train):
	train_predictors = (df_train[predictors].iloc[train,:])
	train_target = df_train["Survived"].iloc[train]
	alg.fit(train_predictors,train_target)
	test_predictions = alg.predict(df_train[predictors].iloc[test,:])
	predictions.append(test_predictions)

predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes(only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <= .5] = 0
accuracy = sum(predictions == df_train["Survived"]) / len(predictions)
print("准确率为: ", accuracy)