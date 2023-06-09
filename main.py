import math
from math import sqrt, ceil, floor

print(floor(6.6))
print(sqrt(11))
print(ceil(6.6))

import PyPDF2
from PyPDF2 import PdfReader
reader  = PdfReader("Applicationform.pdf")
print(len(reader.pages))
page = reader.pages[0]
text = page.extract_text()
print(text)