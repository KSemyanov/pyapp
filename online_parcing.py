#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
head = {"User-Agent": "ittensive-python-scraper/1.0 (+https://www.ittenasive.com)"}
r = requests.get("https://market.yandex.ru/catalog--kholodilniki/71639/list?glfilter=7893318%3A152776&cpa=1&hid=15450081&rs=eJwzYgpgBAABcwCG&suggest_text=Холодильники%20Саратов&suggest=1&suggest_type=categories_vendors&was_redir=1&rt=8&onstock=0&local-offers-first=0", headers=head)
html = BeautifulSoup(r.content)
search_result = html.find_all("div", {"class": "_37suf"}) # div class="_37suf" class="cia-vs" data-node-name="SearchResults" noframes class="apiary-patch"
volume_263 = 0
volume_452 = 0

def find_volume(sr):
    if sr.find("ul", {"data-tid": "6aaad15e 258b22d7"})!=None:
        volume = int( ''.join(i for i in sr.find_all("li")[1].get_text() if i.isdigit()))
    else:
        volume = 0
    return volume

for sr in search_result:
    sname = sr.find("span", {"data-tid": "2e5bde87"}).get_text()  
    if sname.find("Саратов 263") > -1:
        volume_263 = find_volume(sr)
    if sname.find("Саратов 452") > -1:
        volume_452 = find_volume(sr)
diff = max(volume_263,volume_452) - min(volume_263,volume_452)
print(diff)


# In[ ]:




