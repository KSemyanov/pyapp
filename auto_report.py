#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfkit
import pandas as pd
import matplotlib.pyplot as plt
import binascii
from jinja2 import Template
from io import BytesIO
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv", delimiter=";"
                   , usecols=["EDU_NAME", "AdmArea", "PASSES_OVER_220", "YEAR"] )
data = data[data["YEAR"]=="2018-2019"]
data.head(3)
data_best=data.sort_values('PASSES_OVER_220',ascending=False)
eduname_max = data_best.iloc[0]['EDU_NAME']
print(eduname_max)
data["AdmArea"] = data["AdmArea"].apply(lambda x: x.split(" ")[0])
data_adm = data.groupby("AdmArea").sum()["PASSES_OVER_220"].sort_values()
all_over_220 = data_adm.sum()
print(all_over_220)
fig = plt.figure(figsize=(11,6))
area = fig.add_subplot(1,1,1)
explode = [0]*len(data_adm)
explode[0] = 0.4
explode[1] = 0.4
data_adm.plot.pie(ax = area,
                 labels=[""]*len(data_adm),
                 label="Отличники по ЕГЭ",
                 cmap="tab20",
                 autopct=lambda x:int(round(all_over_220 * x/100)),
                 pctdistance=0.9,
                 explode=explode)
plt.legend(data_adm.index, bbox_to_anchor=(1.5,1,0.1,0))
img = BytesIO()
plt.savefig(img)
img = 'data:image/png;base64,'+ binascii.b2a_base64(img.getvalue(), newline=False).decode("UTF-8")
plt.show()

html = '''<html>
<head>
    <title>Результаты ЕГЭ Москвы: отличники</title>
    <meta charset="utf-8"/>
</head>
<body>
    <h1>Результаты ЕГЭ Москвы: отличники в 2018-2019 году</h1>
    <p>Всего: ''' + str(all_over_220) + '''</p>
    <img src="''' + img + '''" alt="Отличники по округам"/>
    <p>Лучшая школа: ''' + str(eduname_max) + '''</p>
</body>
</html>'''
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(html, 'ege_best.pdf',
                   configuration=config, options=options)

message = MIMEMultipart()
message["From"] = "Константин Семьянов"
message["Subject"] = "Результаты по ЕГЭ в Москве"
message["Content-Type"] = "text/html; charset=utf-8"
message["To"] = "ks@medsoftservice.ru"
message.attach(MIMEText(html,"html"))
attachment = MIMEBase("application","pdf")
attachment.set_payload(open("ege_best.pdf", "rb").read())
attachment.add_header("Content-Disposition", 'attachment; filename="ege_best.pdf"')
encoders.encode_base64(attachment)
message.attach(attachment)
user = "*********"
password = "***********"
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#server.starttls()
server.login(user, password)
server.sendmail("xxxxxx@gmail.com", "xxx@ya.ru", message.as_string())
server.quit()


# In[ ]:




