from pprint import pprint
import re
import pdftotext

seat_nos = []

# special case page 20

with open('students.pdf', 'rb') as f:
    content = list(pdftotext.PDF(f))
    content = content[:-1]

    # Special Case
    # print(content[19])

    for i,page in enumerate(content):
        page = list(page.split('\n'))
        
        # Get seat_no on line 8(7)
        seat_no = re.search('F\S*', page[7])[0]
        seat_nos.append(seat_no)

pprint(seat_nos)
