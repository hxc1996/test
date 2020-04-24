import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')
# print(df.info())
# print(df.head(5))
# print(df.describe())

plt.style.use('ggplot')
#获取列
colnm = df.columns.tolist()
fig = plt.figure(figsize=(10,6))

for i in range(12):
    #绘制2*6的子图
    plt.subplot(2,6,i+1)
    sns.boxenplot(df[colnm[i]],orient='v',width=0.5,color=color[0])
    plt.ylabel(colnm[i],fontsize=12)

#自动调整子图参数，使之填充整个图像区域
plt.tight_layout()
print('\nFigure 1: Univariate Boxplots')
plt.show()

