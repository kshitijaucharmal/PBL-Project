import PyPDF2
import re
from tqdm import tqdm

# Read the pdf file
a = PyPDF2.PdfReader('files/students.pdf')

two_sem_prob = []
sgpa_prob = []

subject_set = []
s=''
for i in tqdm(range(0,len(a.pages))):
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

    # Add to pages
    s += page

    # Identify Subject Group
    sme = re.findall(r'101011 ENGINEERING MECHANICS', page)
    subject_set.append(len(sme) == 0)

# Actual Finding
sr_no = re.findall(r'F1900\S*', s)
m = re.findall(r'[0-9]*/[0-9]*', s)

# Report errors
print('These Pages have been skipped due to faults:')
print(f'SGPA is NaN:', sgpa_prob)
print(f'Two Semesters result given', two_sem_prob)

with open('output.csv','w') as e:
    e.write('Rollno,EM_ISE,EM_ESE,EM_THEORY_TOT,EM_TW,SME_ISE,SME_ESE,SME_THEORY_TOT,SME_TW,BEE_ISE,BEE_ESE,BEE_THEORY_TOT,BEE_TW,EM1_ISE,EM1_ESE,EM1_THEORY_TOT,EM1_TW,EP_ISE,EP_ESE,EP_THEORY_TOT,EP_TW,BXE_ISE,BXE_ESE,BXE_THEORY_TOT,BXE_TW,EC_ISE,EC_ESE,EC_THEORY_TOT,EC_TW,PPS_ISE,PPS_ESE,PPS_THEORY_TOT,PPS_TW\n')    
    for i in range(len(sr_no)):
        if subject_set[i]:
            e.write(sr_no[i]+',')
            #First subject SME
            e.write(','*4)
            e.write(m[1+22*i][:3] +',')
            e.write(m[2+22*i][:3] +',')
            e.write(m[3+22*i][:3] +',')
            e.write(m[4+22*i][:3]+',')
            
            #Third subject em1
            e.write(','*4)
            e.write(m[9+22*i][:3]+',')
            e.write(m[10+22*i][:3]+',')
            e.write(m[11+22*i][:3]+',')
            e.write(m[12+22*i][:3]+',')
            
            #Second subject BXE
            e.write(','*4)
            e.write(m[5+22*i][:3]+',')
            e.write(m[6+22*i][:3]+',')
            e.write(m[7+22*i][:3]+',')
            e.write(m[8+22*i][:3]+',')
            
            #Fourth object ec
            e.write(m[13+22*i][:3]+',')
            e.write(m[14+22*i][:3]+',')
            e.write(m[15+22*i][:3]+',')
            e.write(m[16+22*i][:3]+',')
            
            #Fifth subject pps
            e.write(m[17+22*i][:3]+',')
            e.write(m[18+22*i][:3]+',')
            e.write(m[19+22*i][:3]+',')
            e.write(m[20+22*i][:3]+',\n')
            
        else :
            e.write(sr_no[i]+',')
            e.write(m[1+22*i][:3] +',')
            e.write(m[2+22*i][:3] +',')
            e.write(m[3+22*i][:3] +',')
            e.write(m[4+22*i][:3]+',')
            
            #Second subject sme
            e.write(m[5+22*i][:3]+',')
            e.write(m[6+22*i][:3]+',')
            e.write(m[7+22*i][:3]+',')
            e.write(m[8+22*i][:3]+',')
            
            #Third subject BEE
            e.write(m[9+22*i][:3]+',')
            e.write(m[10+22*i][:3]+',')
            e.write(m[11+22*i][:3]+',')
            e.write(m[12+22*i][:3]+',')
            
            #Fourth object em1
            e.write(m[13+22*i][:3]+',')
            e.write(m[14+22*i][:3]+',')
            e.write(m[15+22*i][:3]+',')
            e.write(m[16+22*i][:3]+',')
            
            #Fifth subject ep
            e.write(m[17+22*i][:3]+',')
            e.write(m[18+22*i][:3]+',')
            e.write(m[19+22*i][:3]+',')
            e.write(m[20+22*i][:3]+',\n')
