import PyPDF2

# Specify the path to your PDF file
pdf_file = r'c:\Users\ADMIN\Downloads\Applicationform.pdf.pdf'


# Open the PDF file in read binary mode
with open(pdf_file, 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Get the current page
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        text = page.extract_text()

        # Print the extracted text
        print(text)
