import numpy as np
import pandas as pd
import pdfplumber
import csv

# converting pdf to csv
def pdf_to_csv(input_pdf, output_csv):
    with pdfplumber.open(input_pdf) as pdf:
        with open(output_csv, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for page in pdf.pages:
                lines = page.extract_text().split('\n')
                for line in lines:
                    writer.writerow([line])

input_pdf = "RN1.pdf"
output_csv = "output.csv"
pdf_to_csv(input_pdf, output_csv)

df = pd.read_csv("output.csv")
print(df)
