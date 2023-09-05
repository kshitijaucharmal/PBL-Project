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

        self.mech_first = []

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

        # find sem2 location
        sem2_loc = re.search('SEM\.:2', page).span()[0]

        # Check which subject group is first
        self.mech_first.append(re.search(r'101011 ENGINEERING MECHANICS', page).span()[0] < sem2_loc)

        # Skip this page if 2 sems
        # if len(sem2) > 0:
            # self.two_sem_prob.append(i+1)
            # return

        # Identify Subject Group
        sme = re.findall(r'101011 ENGINEERING MECHANICS', page)
        self.subject_set.append(len(sme) == 0)
        
        # Get all marks
        marks = re.findall(r'[0-9]*[#$]?/[0-9]*', page)

        # Get SGPA
        sgpa_match = re.findall(r'SGPA[1]? : [0-9]\.?[0-9]*', page)
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
        except Exception as e:
            self.write_error = True
            print(e)
            return

        # Write to csv
        with e:
            # Write all subject names
            e.write('Rollno,\
EM_ISE,EM_ESE,EM_TOT,EM_PR,\
SME_ISE,SME_ESE,SME_TOT,SME_PR,\
BEE_ISE,BEE_ESE,BEE_TOT,BEE_PR,\
EM1_ISE,EM1_ESE,EM1_TOT,EM1_TW,\
EP_ISE,EP_ESE,EP_TOT,EP_PR,\
BXE_ISE,BXE_ESE,BXE_TOT,BXE_PR,\
EM2_ISE,EM2_ESE,EM2_TOT,EM2_TW,\
EC_ISE,EC_ESE,EC_TOT,EC_PR,\
PPS_ISE,PPS_ESE,PPS_TOT,PPS_PR,\
EG_ESE,EG_TOT,EG_TW,\
WS_PR,\
PBL_TW,PBL_PR,\
SGPA\n')

            # Loop over all students
            # for i in range(len(sr_nos)):
            # Just 2 for now
            for i in range(len(sr_nos)):
                # Temporarily store current marks
                current_marks = self.all_marks[i]
                # Write based on subjects
                if self.mech_first[i]:
                    self.mechanics_first(e, current_marks, sr_nos[i])
                else:
                    self.other_subjects(e, current_marks, sr_nos[i])

                # Write the sgpa
                # e.write(self.sgpa[i])
                # Newline at the end
                e.write('\n')
        pass

    def mechanics_first(self, e, current_marks, sr_no):
        e.write(sr_no + ',')

        # MECHANICS
        e.write(current_marks[1][:3] + ',')
        e.write(current_marks[2][:3] + ',')
        e.write(current_marks[3][:3] + ',')
        e.write(current_marks[4][:3] + ',')

        # SME
        e.write(current_marks[5][:3] + ',')
        e.write(current_marks[6][:3] + ',')
        e.write(current_marks[7][:3] + ',')
        e.write(current_marks[8][:3] + ',')

        # BEE
        e.write(current_marks[9][:3] + ',')
        e.write(current_marks[10][:3] + ',')
        e.write(current_marks[11][:3] + ',')
        e.write(current_marks[12][:3] + ',')

        # EM1
        e.write(current_marks[13][:3] + ',')
        e.write(current_marks[14][:3] + ',')
        e.write(current_marks[15][:3] + ',')
        e.write(current_marks[16][:3] + ',')

        # EP
        e.write(current_marks[17][:3] + ',')
        e.write(current_marks[18][:3] + ',')
        e.write(current_marks[19][:3] + ',')
        e.write(current_marks[20][:3] + ',')

        # BXE
        e.write(current_marks[25][:3] + ',')
        e.write(current_marks[26][:3] + ',')
        e.write(current_marks[27][:3] + ',')
        e.write(current_marks[28][:3] + ',')

        # EM2
        e.write(current_marks[29][:3] + ',')
        e.write(current_marks[30][:3] + ',')
        e.write(current_marks[31][:3] + ',')
        e.write(current_marks[32][:3] + ',')

        # EC
        e.write(current_marks[33][:3] + ',')
        e.write(current_marks[34][:3] + ',')
        e.write(current_marks[35][:3] + ',')
        e.write(current_marks[36][:3] + ',')

        # PPS
        e.write(current_marks[37][:3] + ',')
        e.write(current_marks[38][:3] + ',')
        e.write(current_marks[39][:3] + ',')
        e.write(current_marks[40][:3] + ',')

        # EG
        e.write(current_marks[22][:3] + ',')
        e.write(current_marks[23][:3] + ',')
        e.write(current_marks[24][:3] + ',')

        # WS
        e.write(current_marks[21][:3] + ',')

        # PBL
        e.write(current_marks[41][:3] + ',')
        e.write(current_marks[42][:3] + ',')
        pass

    def other_subjects(self, e, current_marks, sr_no):
        e.write(sr_no + ',')

        # MECHANICS
        e.write(current_marks[22][:3] + ',')
        e.write(current_marks[23][:3] + ',')
        e.write(current_marks[24][:3] + ',')
        e.write(current_marks[25][:3] + ',')

        # SME
        e.write(current_marks[1][:3] + ',')
        e.write(current_marks[2][:3] + ',')
        e.write(current_marks[3][:3] + ',')
        e.write(current_marks[4][:3] + ',')

        # BEE
        e.write(current_marks[29][:3] + ',')
        e.write(current_marks[30][:3] + ',')
        e.write(current_marks[31][:3] + ',')
        e.write(current_marks[32][:3] + ',')

        # EM1
        e.write(current_marks[9][:3] + ',')
        e.write(current_marks[10][:3] + ',')
        e.write(current_marks[11][:3] + ',')
        e.write(current_marks[12][:3] + ',')

        # EP
        e.write(current_marks[33][:3] + ',')
        e.write(current_marks[34][:3] + ',')
        e.write(current_marks[35][:3] + ',')
        e.write(current_marks[36][:3] + ',')

        # BXE
        e.write(current_marks[5][:3] + ',')
        e.write(current_marks[6][:3] + ',')
        e.write(current_marks[7][:3] + ',')
        e.write(current_marks[8][:3] + ',')

        # EM2
        e.write(current_marks[37][:3] + ',')
        e.write(current_marks[38][:3] + ',')
        e.write(current_marks[39][:3] + ',')
        e.write(current_marks[40][:3] + ',')

        # EC
        e.write(current_marks[13][:3] + ',')
        e.write(current_marks[14][:3] + ',')
        e.write(current_marks[15][:3] + ',')
        e.write(current_marks[16][:3] + ',')

        # PPS
        e.write(current_marks[17][:3] + ',')
        e.write(current_marks[18][:3] + ',')
        e.write(current_marks[19][:3] + ',')
        e.write(current_marks[20][:3] + ',')

        # EG
        e.write(current_marks[26][:3] + ',')
        e.write(current_marks[27][:3] + ',')
        e.write(current_marks[28][:3] + ',')

        # WS
        e.write(current_marks[21][:3] + ',')

        # PBL
        e.write(current_marks[41][:3] + ',')
        e.write(current_marks[42][:3] + ',')
        pass
