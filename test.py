import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import pystan
df = pd.read_csv('我的数据')

# 数据必须是两列，ds为时间序列，y为指标列
labels = ['ds', 'y']
df = pd.DataFrame.from_records(data, columns=labels)
m = Prophet(changepoint_prior_scale=0.001, n_changepoints=0).fit(df)

future = m.make_future_dataframe(periods=50, freq='H')
fcst = m.predict(future)
fig = m.plot(fcst)
plt.show()

# Prophet还提供了组成成分分析，通过下述可得到月份、星期、更细粒度天级别等的分析
# fig = m.plot_components(fcst)
# plt.show()

