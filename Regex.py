import PyPDF2


pdf_file1 = r'Downloads/python_reg_expressions.pdf'

with open(pdf_file1,'rb') as F:
    
    reader = PyPDF2.PdfReader(F)
    
    for p in range(len(reader.pages)):
        
        current_page = reader.pages[p]
        
        text = current_page.extract_text()
        
print(text)
no_pages = len(reader.pages)
print("Number of pages are:",no_pages)

