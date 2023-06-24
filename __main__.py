# Imports
import PyPDF2 # To convert pdf to text
import re # Use regex
from tqdm import tqdm # Progress bar

# Read the pdf file
a = PyPDF2.PdfReader('files/students.pdf')

# Pages with errors
two_sem_prob = []
sgpa_prob = []

subject_set = []
document = ''
all_marks = []

# Loop though pages
for i in tqdm(range(len(a.pages)-1)):
    # Extract text
    page = a.pages[i].extract_text()

    # Check if Sem2 exists 
    sem2 = re.findall('SEM\.:2', page)

    # Check if SGPA is not present
    no_SGPA = re.findall('SGPA1 : --', page)

    # Skip Either way
    if len(sem2) > 0:
        two_sem_prob.append(i+1)
        continue
    if len(no_SGPA) > 0:
        sgpa_prob.append(i+1)
        continue

    # Identify Subject Group
    sme = re.findall(r'101011 ENGINEERING MECHANICS', page)
    subject_set.append(len(sme) == 0)
    
    # Get all marks
    marks = re.findall(r'[0-9]*[#$]?/[0-9]*', page)
    all_marks.append(marks)

    # Add to pages
    document += page

    pass

# Actual Finding With Regex
sr_no = re.findall(r'F1900\S*', document)
# marks = re.findall(r'[0-9]*/[0-9]*', document)

# Find SGPA
sgpa_match = re.findall(r'SGPA1 : [0-9]\.?[0-9]*', document)
sgpa = []
for s in sgpa_match:
    s = s.split()[2]
    sgpa.append(s)

# Report errors
print('These Pages have been skipped due to faults:')
print(f'SGPA is NaN:', sgpa_prob)
print(f'Two Semesters result given', two_sem_prob)

# Write to csv
with open('output.csv','w') as e:
    # Write all subject names
    e.write('Rollno,\
        EM_ISE,EM_ESE,EM_THEORY_TOT,EM_TW,\
        SME_ISE,SME_ESE,SME_THEORY_TOT,SME_TW,\
        BEE_ISE,BEE_ESE,BEE_THEORY_TOT,BEE_TW,\
        EM1_ISE,EM1_ESE,EM1_THEORY_TOT,EM1_TW,\
        EP_ISE,EP_ESE,EP_THEORY_TOT,EP_TW,\
        BXE_ISE,BXE_ESE,BXE_THEORY_TOT,BXE_TW,\
        EC_ISE,EC_ESE,EC_THEORY_TOT,EC_TW,\
        PPS_ISE,PPS_ESE,PPS_THEORY_TOT,PPS_TW,SGPA\n')
    for i in range(len(sr_no)):
        current_marks = all_marks[i]
        if subject_set[i]:
            e.write(sr_no[i]+',')

            #First subject SME
            e.write(',' * 4)
            e.write(current_marks[1][:3] + ',')
            e.write(current_marks[2][:3] + ',')
            e.write(current_marks[3][:3] + ',')
            e.write(current_marks[4][:3] + ',')
            
            #Third subject em1
            e.write(',' * 4)
            e.write(current_marks[9][:3] + ',')
            e.write(current_marks[10][:3] + ',')
            e.write(current_marks[11][:3] + ',')
            e.write(current_marks[12][:3] + ',')
            
            #Second subject BXE
            e.write(',' * 4)
            e.write(current_marks[5][:3] + ',')
            e.write(current_marks[6][:3] + ',')
            e.write(current_marks[7][:3] + ',')
            e.write(current_marks[8][:3] + ',')
            
            #Fourth object ec
            e.write(current_marks[13][:3] + ',')
            e.write(current_marks[14][:3] + ',')
            e.write(current_marks[15][:3] + ',')
            e.write(current_marks[16][:3] + ',')
            
            #Fifth subject pps
            e.write(current_marks[17][:3] + ',')
            e.write(current_marks[18][:3] + ',')
            e.write(current_marks[19][:3] + ',')
            e.write(current_marks[20][:3] + ',')
            
        else :
            e.write(sr_no[i] + ',')

            # First Subject
            e.write(current_marks[1][:3]  + ',')
            e.write(current_marks[2][:3]  + ',')
            e.write(current_marks[3][:3]  + ',')
            e.write(current_marks[4][:3] + ',')
            
            #Second subject sme
            e.write(current_marks[5][:3] + ',')
            e.write(current_marks[6][:3] + ',')
            e.write(current_marks[7][:3] + ',')
            e.write(current_marks[8][:3] + ',')
            
            #Third subject BEE
            e.write(current_marks[9][:3] + ',')
            e.write(current_marks[10][:3] + ',')
            e.write(current_marks[11][:3] + ',')
            e.write(current_marks[12][:3] + ',')
            
            #Fourth object em1
            e.write(current_marks[13][:3] + ',')
            e.write(current_marks[14][:3] + ',')
            e.write(current_marks[15][:3] + ',')
            e.write(current_marks[16][:3] + ',')
            
            #Fifth subject ep
            e.write(current_marks[17][:3] + ',')
            e.write(current_marks[18][:3] + ',')
            e.write(current_marks[19][:3] + ',')
            e.write(current_marks[20][:3] + ',')
            e.write(',' * 12)
        e.write(sgpa[i])
        e.write('\n')
