#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
import json
req_header = {
    "Content-Type": "application/json",
    "Accept": "application/json; charset=UTF-8"
}
url = "https://geocode-maps.yandex.ru/1.x/?apikey=9d52d8e1-40c5-463e-839a-4b51899feacf&geocode=Россия,+Самарская+область+Самара+город&format=json"
response = requests.get(url, headers=req_header)
print ("Код ответа:", response.status_code)
response = json.loads(response.text)
geoobject = response["response"]["GeoObjectCollection"]["featureMember"][0]
data = geoobject["GeoObject"]["Point"]["pos"].split(" ")[0]
print(data)
#print(response["response"]["GeoObjectCollection"]["featureMember"]) #["pos"]
geoobject = response["response"]["GeoObjectCollection"]["featureMember"][0]
data = json.dumps(geoobject["GeoObject"]["Point"]["pos"])
print(data.split(' ')[0].replace('"',''))


# In[35]:





# In[ ]:




