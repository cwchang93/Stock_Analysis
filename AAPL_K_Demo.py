from mpl_finance import candlestick_ohlc
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

style.use('dark_background')

Analysis = "/Users/cwchang/Documents/Python_Coding/Bigdata/AAPL.csv"
data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = data['Close']
price.head()

#算出一段時間的（平均）值、標準差
moving_avg = price.rolling(20).mean()
moving_avg50 = price.rolling(50).mean()
moving_avg80 = price.rolling(80).mean()

moving_avg_mstd = price.rolling(20).std()

#將圖面分成兩塊並切分等分
top = plt.subplot2grid((12, 9), (0, 0), rowspan=9, colspan=9)
bottom = plt.subplot2grid((12, 9), (10, 0), rowspan=2, colspan=9)

# 顯示網格(原本黑色沒網格)
top.grid(which='both', alpha=0.3)
#重新排序日期（），空日期屏除，轉換時間格式功能
data = data.reset_index()
data['Date'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))

# 將需要的資料（開高低收日期）放進candlestick [[]]直接把數字給 x，pandas[[]]雙重list，values 表示數字
candlestick = [tuple(x) for x in data[['Date','Open','High','Low','Close']].values]

# 把功能顯示出來及畫Ｋ線
candlestick_ohlc(top, candlestick, width=0.5,colorup='r',colordown='green',alpha=0.7)

# top.plot(price, color='b')
top.plot(moving_avg, color='b', linewidth=1, alpha=0.7, label='MA20')
top.plot(moving_avg50, color='r', linewidth=1, alpha=0.7, label='MA50')
top.plot(moving_avg80, color='g', linewidth=1, alpha=0.7, label='MA80')

# 畫出標準差區域並顯示
top.fill_between(moving_avg.index, moving_avg-2*moving_avg_mstd, moving_avg+2*moving_avg_mstd, color='white', alpha=0.1)
bottom.bar(data.index, data['Volume'])

top.legend()
plt.show()
