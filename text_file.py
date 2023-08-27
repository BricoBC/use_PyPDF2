import PyPDF2

#Accedemos a la página que se necesita.
reader = PyPDF2.PdfReader("documento.pdf")
page = reader.pages[5];

#Se imprime la información se la página
#print(page.extract_text())

#Método paea extraer el texto de una página
doc_text = page.extract_text()
#print(doc_text)

#Se obtienen las frases del documento
phrase = ''
arr = []

for text in doc_text:
    phrase = phrase + text
    if('\n'==text):
        arr.append(phrase)
        phrase=''
print(arr, end=' ')


