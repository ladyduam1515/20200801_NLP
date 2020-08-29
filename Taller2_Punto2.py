#!/usr/bin/env python
# coding: utf-8

# In[72]:


import bs4 as bs
import urllib.request


# In[73]:


link = "https://es.wikipedia.org/wiki/Julio_Cort%C3%A1zar"
#link = "https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python"


# In[74]:


# Descargar página web en Python
request = urllib.request.urlopen(link)
fuente = request.read()
request.close()


# In[88]:


soup = bs.BeautifulSoup(fuente, "html.parser")
soup.find("link rel").contents


# In[86]:


for respuesta in soup.find(id='script').find_all(class_="client-js"):
    # En cada respuesta buscar la clase post-text
    for texto in respuesta.find_all(class_="wgPageName"):
        for parrafo in texto.find_all('p'):
            print(parrafo.contents)
    print("*"*100)
    print()


# In[ ]:




