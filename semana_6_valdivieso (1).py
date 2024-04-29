#!/usr/bin/env python
# coding: utf-8

# # SEMANA 05
# Valdivieso Sanchez, Jheremy Victor
# 
# Temas
# 
# 1. Colecciones de datos
# 2. Estructuras Decisivas y Estructuras Repetitivas
# 3. Clases y Objetos
# 4. Funciones

# 1. Colecciones
# 

# In[1]:


# 1.1. Listas
# Es una colección de elementos que puede ser ordenada, modificada, etc..
# Se identifica por los corchetes
# Ejemplo:
aula = ['Bernaola','Chipana','Gomez','Navarro']
print(aula)


# In[2]:


# Tambien se puede imprimir con solo mencional la lista
aula


# In[3]:


# Podemos extraer cada elemento por su posición
print(aula[0])
print(aula[1])


# In[4]:


# Puedo asignar un valor a una posición de la lista
aula[1] = 'Chavez'
aula[1]


# In[5]:


# Mostramos como quedó la lista
aula


# In[6]:


# Para agregar un elemento utilizamos append
aula.append("Hermitaño")
aula.append("Gomez")
aula


# In[7]:


# Para eliminar elementos utilizamos remove[]
aula.remove("Bernaola")
aula


# In[8]:


# Si hubiera varios elementos de valores iguales se elimina la primera coincidencia
aula.remove("Gomez")
aula


# In[9]:


# para obtener el tamaño utilizamos len()
len(aula)


# In[10]:


# para recorrer podemos utilizar una estructura repetitiva
# en java es {, en python es :
for alumno in aula:
    print(alumno)


# In[11]:


# para invertir la lista utilizamos reverse()
# invertir no significa ordenar en forma descendente sin invertir la lista
aula.reverse()
aula


# In[12]:


# para ordenar una lista utilizamos sort()
aula.sort()
aula


# In[15]:


# 1.2 Tuplas
# es una coleccion de elementos ordenada (ordenado significa que tiene un indice)
# no se pueden agregar elementos ni eliminar
# se identifica por los parentesis
tupla_aula = ('Huertas','Bravo','Bonifacio','Caballero')
tupla_aula


# In[16]:


# Se puede extraer un elemento por su posición
tupla_aula[2]


# In[17]:


# Para saber la cantidad de elementos de una tupla utilizamos len()
len(tupla_aula)


# In[14]:


# 1.3 conjuntos
# es una coleccion de elementos que no esta ordenado
# (significa que no tiene un indice)
conjunto_aula = {'Huertas','Bravo','Bonifacio','Caballero'}
conjunto_aula


# In[18]:


# se puede recorrer utilizando una estructura repetitiva
# ejemplo: for
for alumno in conjunto_aula:
    print(alumno)


# In[19]:


# observacion no se puede acceder por posicion pues no considera indexacion # EXAMEN
# por ejemplo:
conjunto_aula[2] # devolveria un mensaje de error


# In[21]:


# para saber la cantidad de elementos utilizamos len()
len(conjunto_aula)


# In[22]:


# para agregar utilizamos la funcion add()
conjunto_aula.add("paye")
conjunto_aula


# In[24]:


# para eliminar elementos utilizamos la funcion remove()
conjunto_aula.remove("Bravo")
conjunto_aula


# In[27]:


# 1.4 diccionarios
# es una coleccion de elementos, que estan indexados,
# no estan ordenados y se pueden modificar
# son escritos entre llaves y estan formados por pares de elementos
# indice:valor
diccionario_aula={2:'Huertas','1':'Bravo','dos':'Bonifacio','3':'Caballero','0':'Paye'}
diccionario_aula


# In[28]:


# Del Diccionario: diccionario_aula extraer el valor cuyo índice sea cero en String:
diccionario_aula['0']


# In[29]:


diccionario_aula[2]


# In[30]:


diccionario_aula["1"]


# In[31]:


diccionario_aula["dos"]


# In[33]:


# Para añadir un par de elementos al diccionario hacemos:
diccionario_aula['20'] = "Velez"
diccionario_aula


# In[34]:


# Para eliminar un valor se utiliza pop()
# Por ejemplo,eliminar el elmento de índice dos.ejemplo: Para eliminar a Bernaola que tendríamos que hacer:
diccionario_aula.pop(2)
diccionario_aula


# In[35]:


# Tambien se puede eliminar utilizando del()
del(diccionario_aula["dos"])
diccionario_aula


# In[ ]:


# Para recorrer todos los elementos podemos utilizar for
# En este ejemplo devuelve los índices
for indice in diccionario_aula:
    print(indice)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:


aux = input("Ingrese el nombre del alumno a buscar: ") 
grupo = ["AMES", "ARTEAGA" , "BARRIOS" , "BONIFACIO", "BRAVO", "CABALLERO" , "CAÑAZACA", "FERNANDEZ" , "FLORES" , "GARCIA" , "HERRERA" , "HUERTA" , "HUERTAS", "JIMENEZ" , "MAMANI" , "MANCILLA", "PABLO" , "PAYE" , "PEÑA" , "PIZANGO", "RAMOS", "SANCHEZ", "SEVILLANO", "TINOCO", "TORRES" , "VALDIVIESO", "VELEZ" , "VILLANUEVA" , "ZUÑIGA"]

encontrado = False
for estudiante in grupo:
    if estudiante == aux:
        print('El alumno ' + aux + ' pertenece al grupo')
        encontrado = True
        break

if not encontrado:
    print('El alumno ' + aux + ' no pertenece al grupo')


# In[ ]:





# In[ ]:





# In[ ]:




