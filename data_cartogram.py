#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import descartes

data_cult = pd.read_csv("data-44-structure-4.csv", usecols=["Объект","Регион"])
data_cult["Регион"] = data_cult["Регион"].str.upper()
data_cult = data_cult.groupby("Регион").count()

map_data = gpd.read_file("russia.json")
map_data = map_data.to_crs('epsg:3857')
map_data["NL_NAME_1"] = map_data["NL_NAME_1"].str.upper()

map_data = map_data.replace({
    "ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ": "ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ - ЮГРА",
    "РЕСПУБЛИКА АДЫГЕЯ": "РЕСПУБЛИКА АДЫГЕЯ (АДЫГЕЯ)",
    "ЧУВАШСКАЯ РЕСПУБЛИКА": "ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ",
    "РЕСПУБЛИКА МАРИЙ-ЭЛ": "РЕСПУБЛИКА МАРИЙ ЭЛ",
    "РЕСПУБЛИКА СЕВЕРНАЯ ОСЕТИЯ": "РЕСПУБЛИКА СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ",
    "РЕСПУБЛИКА ТАТАРСТАН": "РЕСПУБЛИКА ТАТАРСТАН (ТАТАРСТАН)"
})
map_data = pd.merge(left=map_data, right=data_cult, left_on="NL_NAME_1", right_on="Регион", how="left")
#print(map_data[map_data["Объект"].isnull()])
fig = plt.figure(figsize=(18,10))
area = plt.subplot(1,1,1)
map_data.plot(ax=area,legend=True, column="Объект", cmap="Blues")
area.set_xlim(2e6, 2e7)
for _, reg in map_data.iterrows():
    area.annotate(reg["Объект"],
                 xy=(reg.geometry.centroid.x,
                    reg.geometry.centroid.y), fontsize=8)
print ("АЛТАЙСКИЙ КРАЙ ",map_data[map_data["NL_NAME_1"] == "АЛТАЙСКИЙ КРАЙ"]["Объект"])
print ("НОВОСИБИРСКАЯ ОБЛАСТЬ ", map_data[map_data["NL_NAME_1"] == "НОВОСИБИРСКАЯ ОБЛАСТЬ"]["Объект"])
plt.show

