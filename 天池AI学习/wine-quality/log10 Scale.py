import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')

plt.style.use('ggplot')
acidityFeat = ['fixed acidity', 'volatile acidity', 'citric acid',
               'free sulfur dioxide', 'total sulfur dioxide', 'sulphates']
fig = plt.figure(figsize=(10,4))
for i in range(6):
    ax = plt.subplot(2,3,i+1)
    v = np.log10(np.clip(df[acidityFeat[i]].values,a_min=0.001,a_max= None))
    plt.hist(v,bins=50,color=color[0])
    plt.xlabel('log('+acidityFeat[i]+')',fontsize=12)
    plt.ylabel('Frequency')

plt.tight_layout()
print('\nFigure 3: Acidity Features in log10 Scale')
plt.show()

