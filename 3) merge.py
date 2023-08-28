#File #3s

import PyPDF2
import os

def merge_all_files():
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

def merge_for_pages():
    merger = PyPDF2.PdfMerger()

    files = os.listdir("./pdf's/")

    for file in files:
        doc = PyPDF2.PdfReader("./pdf's/" + file)
        if (len(doc.pages)) != 1:
            print('Para extraer un archivo se necesita una página de inicio y una página final')
            pp1 = int(input(f"Para el archivo {file} cuál es la página de inicio: "))-1
            pp2 = int(input(f"Para el archivo {file} cuál es la página final: "))-1
            merger.append(fileobj= doc, pages= (pp1,pp2))
            print()
        else:
            merger.append(doc)
            

    # Creamos el archivo, el parametro es el nombre del nuevo archivo.
    merger.write("merged.pdf")
    # Se cierra el archivo.
    merger.close()
merge_for_pages()