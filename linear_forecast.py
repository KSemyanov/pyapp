#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
from sklearn.linear_model import LinearRegression
data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";",
                  usecols = ["Year", "UnemployedDisabled", "UnemployedTotal", "Period"])
data["DTRatio"] = data["UnemployedDisabled"]/data["UnemployedTotal"]*100
data = data.groupby("Year").filter(lambda x: x["UnemployedDisabled"].count() >= 6)
data_avg = data.groupby("Year").mean()
cnt = len(data_avg.index)
x = np.array(data_avg.index).reshape(cnt,1)
y = np.array(data_avg["DTRatio"]).reshape(cnt,1)
model = LinearRegression()
model.fit(x,y)
plt.scatter(x, y, color="orange")
x = np.append(x, [2020]).reshape(len(data_avg.index)+1, 1)
plt.plot(x, model.predict(x), color="blue", linewidth=3)
plt.show()
print (model.predict(np.array(2020).reshape(1, 1)).round(2))


# In[ ]:




