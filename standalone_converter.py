from converter import Converter
import os
from tqdm import tqdm

# Manually giving this for now
pdfpath = './students.pdf'
pages_to_be_skipped = [2, 3, 4]

# Converter object
csvpath = f'{os.getcwd()}/output.csv'
converter = Converter(pdfpath, csvpath)

n = converter.n_pages

# Convert page by page
for i in tqdm(range(n)):
    if (i+1) in pages_to_be_skipped:
        continue
    converter.step(i)

# Write to csv file
converter.write()

error = converter.report_errors()
    
info = f'Saved file {csvpath}'
info += f'\nManually Skipped Pages: {pages_to_be_skipped}'

print(error)
print(info)
