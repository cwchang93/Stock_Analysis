from mpl_finance import candlestick_ohlc
from matplotlib import pyplot as plt
from matplotlib import style

import matplotlib.dates as mdates
import pandas as pd
import numpy as np

style.use('dark_background')

Analysis = "/Users/cwchang/Documents/Python_Coding/Bigdata/AAPL.csv"

data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')

price = data['Close']   #收盤價
price.head()

top = plt.subplot2grid((12, 9), (0, 0), rowspan=9, colspan=9)
bottom = plt.subplot2grid((12, 9), (10, 0), rowspan=2, colspan=9)

moving_avg = price.rolling(20).mean()
moving_avg_mstd = price.rolling(20).std()

data["20d"] = np.round(data["Close"].rolling(window=20, center=False).mean(), 2)
data["50d"] = np.round(data["Close"].rolling(window=50, center=False).mean(), 2)

data["20d-50d"] = data["20d"] - data["50d"]

data["Regime"] = np.where(data['20d-50d'] > 0, 1, 0)
data["Regime"] = np.where(data['20d-50d'] < 0, -1, data["Regime"]) #訊號
#計算多頭或空頭

data["Regime"].value_counts()

regime_orig = data.ix[-1, "Regime"]  #排序功能
data.ix[-1, "Regime"] = 0
data["Signal"] = np.sign(data["Regime"] - data["Regime"].shift(1))
#交叉均線分析  訊號總結
data.ix[-1, "Regime"] = regime_orig

data["Signal"].plot(ylim=(-2, 2))

top.plot(data["20d"], color='b', linewidth=1, alpha=0.7, label='MA5')
top.plot(data["50d"], color='r', linewidth=1, alpha=0.7, label='MA20')

top.grid(which='both', alpha=0.3)

data = data.reset_index()
data['Date'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
candlestick = [tuple(x) for x in data[['Date','Open','High','Low','Close']].values]
candlestick_ohlc(top, candlestick, width=0.5,colorup='r',colordown='green',alpha=0.7)

top.fill_between(moving_avg.index, moving_avg-2*moving_avg_mstd, moving_avg+2*moving_avg_mstd, color='white', alpha=0.1)

top.legend()
plt.show()
