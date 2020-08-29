#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Punto 1
#Descomprimir el archivo .zip de los poemas
import os
from zipfile import ZipFile


# In[18]:


direccion =  "C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/poemas.zip"


# In[21]:


# Descomprimir el archivo zip en el computador
with ZipFile(direccion) as archivo:
    archivo.extractall("C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/")


# In[22]:


#Para ver la estructura: El directorio = ruta y cada uno de los archivos que está en el directorio
for file in os.walk('C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/poemas'):
    print(file)


# In[38]:


for raiz, dirs, archivos in os.walk('C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/poemas'):
    for archivo in archivos:
        print(archivo)


# In[39]:


#Parte 2
#Leer cada uno de sus archivos

with open("C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/poemas/A un general (Julio Cortazar).txt") as archivo:
    data = archivo.read()
    


# In[40]:


print (data)


# In[41]:


with open("C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/poemas/Aqui (Octavio Paz).txt") as archivo:
    data2 = archivo.read()
    


# In[42]:


print (data2)


# In[43]:


with open("C:/Users/PC/OneDrive - Grupo Procaps/Documentos/Konrad Lorenz/Semetre_II/NLP/20200822/archivos/poemas/Sindrome (Mario Benedetti).txt") as archivo:
    data3 = archivo.read()
    


# In[44]:


print (data3)


# In[90]:


#Parte 3
#Responder: ¿Cuál archivo tiene el mayor número de palabras?
palabras = data.split()
num_palabras = len(palabras)
print("El archivo Data  contiene " + str(num_palabras)+" palabras")

palabras2 = data2.split()
num_palabras2 = len(palabras2)
print("El archivo Data2 contiene " + str(num_palabras2)+" palabras")

palabras3 = data3.split()
num_palabras3 = len(palabras3)
print("El archivo Data3 contiene " + str(num_palabras3)+" palabras")
print("")
print ("RESPUESTA: El archivo que más palabras contiene es el Data3 que corresponde a Sindrome (Mario Benedetti)")
print("")
print("")
print("")
print (data3)


# In[ ]:





# In[ ]:




