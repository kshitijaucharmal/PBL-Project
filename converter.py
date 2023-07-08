# Imports
import PyPDF2 # To convert pdf to text
import re # Use regex

class Converter:
    def __init__(self, pdfpath, csvpath):
        # Store paths
        self.pdfpath = pdfpath
        self.csvpath = csvpath

        # Pages with errors
        self.two_sem_prob = []
        self.write_error = False

        self.subject_set = []
        self.document = ''
        self.all_marks = []
        self.sgpa = []

        # Read the pdf file
        self.converted_doc = PyPDF2.PdfReader(pdfpath)
        
        # Number of pages (The last is empty so skip it)
        self.n_pages = len(self.converted_doc.pages)
        pass

    # This is the main process (Call this to instantly do everything)
    def convert(self):
        # Convert page by page
        for i in range(self.n_pages):
            self.step(i)

        # Write to csv file
        self.write()

        # Report errors
        self.report_errors()
        pass

    def step(self, i):
        # Extract text
        page = self.converted_doc.pages[i].extract_text()

        # Check if Sem2 exists 
        sem2 = re.findall('SEM\.:2', page)

        # Skip this page if 2 sems
        if len(sem2) > 0:
            self.two_sem_prob.append(i+1)
            return

        # Identify Subject Group
        sme = re.findall(r'101011 ENGINEERING MECHANICS', page)
        self.subject_set.append(len(sme) == 0)
        
        # Get all marks
        marks = re.findall(r'[0-9]*[#$]?/[0-9]*', page)

        # Get SGPA
        sgpa_match = re.findall(r'SGPA1 : [0-9]\.?[0-9]*', page)
        s = ''
        # If sgpa is present
        if len(sgpa_match) > 0:
            s = sgpa_match[0].split()[2]
        else:
            s = '-'
            # This means student is absent in some subject, so find absentees
            for i in range(len(marks)):
                if marks[i][0] == '/':
                    marks[i] = 'AB'

        self.sgpa.append(s)
        self.all_marks.append(marks)

        # Add to pages
        self.document += page
        pass

    def report_errors(self):
        # Report errors
        s = ''
        if self.write_error:
            s += '!!! File is already open, Please try again after closing. !!!\n'
            return s
        s += 'These Pages have been skipped due to faults: \n'
        s += str(self.two_sem_prob)
        return s

    def write(self):
        # Finding Sr nos. With Regex
        sr_nos = re.findall(r'F1900\S*', self.document)


        try:
            e = open(self.csvpath, 'w')
        except Exception:
            self.write_error = True
            return

        # Write to csv
        with e:
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

            # Loop over all students
            for i in range(len(sr_nos)):
                # Temporarily store current marks
                current_marks = self.all_marks[i]
                # Write based on subjects
                if self.subject_set[i]:
                    self.subject_set1(e, current_marks, sr_nos[i])
                else:
                    self.subject_set2(e, current_marks, sr_nos[i])

                # Write the sgpa
                e.write(self.sgpa[i])
                # Newline at the end
                e.write('\n')
        pass

    def subject_set1(self, e, current_marks, sr_no):
        e.write(sr_no+',')

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
        pass

    def subject_set2(self, e, current_marks, sr_no):
        e.write(sr_no + ',')

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
        pass
