import PyPDF2
import os

#Una variable que tiene propiedades para combinar los archivos
merger = PyPDF2.PdfMerger()

#Se crea una variable de tipo lista para almacenar los nombres de la ubicación que pasamos en el parametro
files = os.listdir("./pdf's/")

#Se hace el recorrido de cada archivo que existe en la lista
for file in files:
    #Se lee el archivo de una ubicación en especifico
    doc = PyPDF2.PdfReader("./pdf's/" + file)
    #Se empieza a pilar los archivos.
    merger.append(doc)

#Creamos el archivo, el parametro es el nombre del nuevo archivo.
merger.write("merged.pdf")
#Se cierra el archivo.
merger.close()
