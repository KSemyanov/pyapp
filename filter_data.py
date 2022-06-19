#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('display.max_rows', None)
data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=';',na_values="NA",
                         usecols=["Year", "UnemployedTotal", "UnemployedDisabled"])
data["Ratio"] = data.apply(lambda x: 100*x[1]/x[2], axis=1)
data = data[data["Ratio"]<2]
data.set_index('Year',inplace=True)
data = data.sort_index()
print(data.index[0:1])


# In[ ]:




