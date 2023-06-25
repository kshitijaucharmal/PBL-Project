import csv
import PyPDF2

pdf_file = r'fe-2019 course-Dec21.pdf'
csv_file = r'Book1.xlsx' # Create a csv file in which the text is to be extracted


# Open the PDF file in read binary mode

with open(pdf_file, 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)

    extracted_text = []

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Get the current page
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        text = page.extract_text()
        
        extracted_text.append(text)

try:      
    with open(csv_file,'w',newline='') as csvfile: # open empty csv file in 'write' mode
        
        csv_write = csv.writer(csvfile)
        
        for text in extracted_text:
            
            csv_write.writerow([text])
    print('Conversion successful')
except FileExistsError:
    print("Fcuk of niga")
        
