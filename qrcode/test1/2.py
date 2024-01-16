import PyPDF2

stamp = PyPDF2.PdfReader("1-1.pdf").pages[0]

writer = PyPDF2.PdfWriter("1-12.pdf")

for page in writer.pages:
    page.merge_page(stamp)

writer.write("ou.pdf")