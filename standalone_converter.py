from converter import Converter
import os
from tqdm import tqdm
import optparse

# Options
parser = optparse.OptionParser()
parser.add_option('-p', '--pdf', help="Path to result pdf")
parser.add_option('-o', '--output', help=f"Output Path for csv (default={os.getcwd()}/output.csv)", default=f'{os.getcwd()}/output.csv')
parser.add_option('-s', '--skip', help="Pages to be skipped [Ex: \'1,2,3,4\'])", default = [])
(options, args) = parser.parse_args()

# Check if result pdf is given
if not options.pdf:
    print('Error: Please provide the result pdf')
    parser.print_help()
    exit()

# Set values
pdfpath = options.pdf
pages_to_be_skipped = options.skip

# Converter object
csvpath = options.output
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
