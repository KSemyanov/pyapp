#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd
import binascii
import pdfkit
from jinja2 import Template
import matplotlib.pyplot as plt

r = requests.get("https://video.ittensive.com/python-advanced/data-107235-2019-12-02.utf.json")
data = pd.DataFrame(json.loads(r.content), columns = ["CourseName", "CoursesTimetable", "NameOfPark"])
data["NameOfPark"] = data["NameOfPark"].apply(lambda x: x["value"])
data.columns = ["Активность", "Расписание", "Парк"]

tiz = data[data["Активность"].str.contains("Тайцзицюань")]["Активность"].count()
print("Тайцзицюань ", tiz)
fig = plt.figure(figsize=(12,8))
area = fig.add_subplot(1,1,1)
activity = data.groupby("Парк").count().sort_values("Активность", ascending = False)
activity["Активность"].head(10).plot.pie(ax=area,label="")
plt.savefig('activity.png')
with open('activity.png', 'rb') as f:
    img = 'data:image/png;base64,' + binascii.b2a_base64(f.read(), newline=False).decode("UTF-8")
    
html_template = '''<html>
<head>
    <title>Активности в парках Москвы</title>
    <meta charset="utf-8"/>
</head>
<body>
    <h1>Топ 10 активностей парков Москвы</h1>
    <img src="{{data.image}}" alt="Топ 10">
    <h2>Активности в парках Москвы</h2>
    {{data.table}}
</body>
</html>'''

html = Template(html_template).render(data = {
    'image': img,
    'table': data.to_html()
})

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(html, 'activity.pdf',
                  configuration=config, options = options)
with open("activity.html", "w", encoding="utf-8") as file:
    file.write(html)
plt.show()


# In[ ]:




