#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import math as m
data = pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter = ";",
                   dtype={"Calls": np.int32})
print(round(data['Calls'].mean()))


# In[ ]:




