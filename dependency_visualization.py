#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

marathon = pd.read_csv("https://video.ittensive.com/python-advanced/marathon-data.csv")
def convert_time(a):
    return sum(x*int(t) for x,t in zip([3600, 60, 1], a.split(":")))

marathon["split"] = marathon["split"].apply(convert_time)
marathon["final"] = marathon["final"].apply(convert_time)

sns.pairplot(marathon, hue="gender", height=4)
print('Коэффициент корреляции = ', round(stats.pearsonr(marathon["split"],marathon["final"])[0],2))
sns.jointplot(data=marathon, x="split", y="final", height=12, kind="kde")
plt.show()

