import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')

plt.style.use('ggplot')
df['total acid'] = df['fixed acidity'] + df['volatile acidity'] + df['citric acid']

plt.figure(figsize=(10,8))
plt.subplot(121)
plt.hist(df['total acid'],bins=50,color=color[0])
plt.xlabel('total acid')
plt.ylabel('Frequency')

plt.subplot(122)
plt.hist(np.log(df['total acid']),bins=50,color=color[0])
plt.xlabel('log(total acid)')
plt.ylabel('Frequency')
plt.tight_layout()
print('\nFigure 5: Total Acid Histogram')
plt.show()

