import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

Analysis = '/Users/cwchang/Documents/Python_Coding/Bigdata/AAPL.csv'
data = pd.read_csv(Analysis, parse_dates=True, index_col ='Date')   #parse dates?
#print(data)
price = data['Close']    #2017/5 ~ 2018/5  收盤價
price.head()    #找出收盤價數據

moving_avg = price.rolling(20).mean()
moving_avg_mstd = price.rolling(20).std()
#平均移動線ＭＶ(均線)   rolling 20?
#20日均線 表示最近20天交易日的平均收盤價格。
# 若 Price > 20日均線 表示過去20天進場的人都是賺錢的
plt.plot(price, color='b', label='Price')
plt.plot(moving_avg, color = 'r', label='MA(20)')
plt.fill_between(moving_avg.index, moving_avg-2*moving_avg_mstd, moving_avg+2*moving_avg_mstd, color ='b', alpha =0.2)
# alpha: 線的透明度，0.9愈深
plt.legend()
plt.show()
