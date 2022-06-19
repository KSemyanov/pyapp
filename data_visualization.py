#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv", delimiter=';',
                  usecols = ["AdmArea", "YEAR", "PASSES_OVER_220", "District"] )
data = data.dropna(axis=1)
data = data[data["YEAR"]=="2018-2019"]
data["AdmArea"] = data["AdmArea"].apply(lambda x: x.split(" ")[0])
data["District"] = data["District"].apply(lambda x: x.replace("район ",""))
data_adm = data.groupby("AdmArea").sum()
data_nw = data[data["AdmArea"]=="Северо-Западный"]
data_nw = data_nw.groupby("District").sum()

data_adm = data_adm.reindex(["Новомосковский","Восточный","Зеленоградский","Западный","Северный","Северо-Восточный",
                             "Северо-Западный","Троицкий","Центральный","Юго-Восточный","Юго-Западный","Южный"])
fig = plt.figure(figsize = (12,12))
area = fig.add_subplot(1,2,1)
area.set_title("ЕГЭ Москвы", fontsize=16)
total_adm = sum(data_adm["PASSES_OVER_220"])
data_adm["PASSES_OVER_220"].plot.pie(ax=area, label="", autopct=lambda x: int(total_adm * x/100))
area = fig.add_subplot(1,2,2)
area.set_title("ЕГЭ Северо-Западного округа", fontsize=16)
total_nw = sum(data_nw["PASSES_OVER_220"])
data_nw["PASSES_OVER_220"].plot.pie(ax=area, label="", autopct=lambda x: int(total_nw * x/100))
plt.show()


# In[ ]:




