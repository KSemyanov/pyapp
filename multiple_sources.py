#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('display.max_rows', None)
data_unempl = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=';',na_values="NA",
                         usecols=["Year", "UnemployedMen", "Period"])
data_unempl = data_unempl.rename(columns={"UnemployedMen":"UneMen", "Period":"Month"})
data_unempl.set_index(['Year','Month'], inplace=True, drop=True)
data_unempl = data_unempl.sort_index()

data_firecall = pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=';',na_values="NA",
                         usecols=["Year", "Month", "Calls", "AdmArea"])
data_firecall = data_firecall[data_firecall["AdmArea"] == 'Центральный административный округ']
data_firecall = data_firecall.drop(["AdmArea"], axis=1)
data_firecall.set_index(['Year','Month'], inplace=True, drop=True)

data_merged = pd.merge(data_unempl, data_firecall,  left_index=True, right_index=True)  #how='outer',
print(data_merged["Calls"].min())
data_min = data_merged[data_merged["Calls"] == data_merged["Calls"].min()]
print(data_min["UneMen"])


# In[ ]:




