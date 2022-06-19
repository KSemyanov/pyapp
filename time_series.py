#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("https://video.ittensive.com/python-advanced/rts-index.csv", usecols=["Date","Max", "Close"])
data["Date"]= pd.to_datetime(data["Date"], dayfirst=True)
dates = pd.date_range(min(data["Date"]),max(data["Date"]))
data = data.set_index("Date")
data = data.reindex(dates).ffill()
data["Day"] = pd.to_datetime(data.index).dayofyear
data.index.name = "Date"
data = data.sort_index()

fig = plt.figure(figsize=(12,7))
area = fig.add_subplot(1,1,1)

data_2019 = data.loc["2019"].reset_index().set_index("Day")
data_2017_maxexpm = data.loc["2017"].reset_index().set_index("Day")["Max"].ewm(span=20).mean()

data_fall = data_2019[data_2019["Close"] < data_2017_maxexpm[0:len(data_2019)]]
data_fall.set_index("Date", inplace=True)
data_fall = data_fall.sort_index(ascending=False)
print(data_fall.head(1).index)

data.loc["2017"].reset_index().set_index("Day")["Close"].plot(ax=area, color="grey", label="2017", lw=3)
data.loc["2018"].reset_index().set_index("Day")["Close"].plot(ax=area, color="blue", label="2018", lw=3)
data_2019["Close"].plot(ax=area, color="red", label="2019", lw=3)
data_2017_maxexpm.plot(ax=area, color="orange", label="Exp2017", lw=3)
plt.legend(loc='upper left')
plt.show()     


