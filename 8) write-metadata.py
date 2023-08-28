#File #8
from PyPDF2 import *

doc = PdfReader("meta-modify.pdf")
writer = PdfWriter()

for page in doc.pages:
    writer.add_page(page)

writer.add_metadata(
    {
        "/Creator": "BricoBC"
    }
)


with open("meta-pdf.pdf", "wb") as f:
    writer.write(f)