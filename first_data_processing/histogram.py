import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

data = pd.read_csv("D:\\baidu.csv")
data_list = data.groupby('year').apply(lambda x:x.count())
print(data_list.shape)
count_data =data_list['title'].values
year_data = list(range(1989,2020))
print(data_list)
print(len(count_data))
print(len(year_data))

# plt.figure(figsize=(20,8),dpi=80)
# plt.plot(year_data,count_data)
# plt.title('year')
# plt.show()