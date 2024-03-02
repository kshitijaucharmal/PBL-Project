# Import the required Modules
import pandas as pd
import pdfplumber
from tqdm import tqdm

input_pdf = "big_input.pdf"
output_csv = 'output.csv'

final_df = pd.DataFrame({
    "Rollno" : [0],
    "EM_ISE" : [0], "EM_ESE" : [0], "EM_THEORY_TOT" : [0], "EM_TW" : [0],
    "SME_ISE" : [0], "SME_ESE" : [0], "SME_THEORY_TOT" : [0], "SME_TW" : [0],
    "BEE_ISE" : [0], "BEE_ESE" : [0], "BEE_THEORY_TOT" : [0], "BEE_TW" : [0],
    "EM1_ISE" : [0], "EM1_ESE" : [0], "EM1_THEORY_TOT" : [0], "EM1_TW" : [0],
    "EP_ISE" : [0], "EP_ESE" : [0], "EP_THEORY_TOT" : [0], "EP_TW" : [0],
    "BXE_ISE" : [0], "BXE_ESE" : [0], "BXE_THEORY_TOT" : [0], "BXE_TW" : [0],
    "EC_ISE" : [0], "EC_ESE" : [0], "EC_THEORY_TOT" : [0], "EC_TW" : [0],
    "PPS_ISE" : [0], "PPS_ESE" : [0], "PPS_THEORY_TOT" : [0], "PPS_TW" : [0],
    "SGPA" : [0]
})

def step(df):
    global final_df
# Creating a DataFrame with one row of zeros for each column
    # for page 1
    # identifying the course
    course_1 = df.iloc[11,0].split(' ')[0]
    course_2 = df.iloc[27,0].split(' ')[0]

    def splitter(loc_list):
        full_list = []
        for l in loc_list:
            full_list.append(df.iloc[l,0].split(' '))
        return full_list

# code for result 1
    if(course_1 == "101011-1"):
        # index for separating the marks of subjects
        full_list = splitter([11, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23])
            
        new = pd.DataFrame({
        "Rollno" : full_list[1][4],

        "EM_ISE" :full_list[0][2], "EM_ESE" :full_list[0][4], "EM_THEORY_TOT" :full_list[0][9],
        "EM_TW" : full_list[2][4],
        "SME_ISE" :full_list[3][2], "SME_ESE" :full_list[3][4], "SME_THEORY_TOT" :full_list[3][9],
        "SME_TW" :full_list[4][4],
        "BEE_ISE" :full_list[5][2], "BEE_ESE" :full_list[5][4], "BEE_THEORY_TOT" :full_list[5][9],
        "BEE_TW" :full_list[6][4],
        "EM1_ISE" :full_list[7][2], "EM1_ESE" :full_list[7][4], "EM1_THEORY_TOT" :full_list[7][9],
        "EM1_TW" : full_list[8][5],
        "EP_ISE" :full_list[9][2], "EP_ESE" :full_list[9][4], "EP_THEORY_TOT" : full_list[9][9],
        "EP_TW" : full_list[10][4],

        # Zeros
        "BXE_ISE" : [0], "BXE_ESE" :[0], "BXE_THEORY_TOT" :[0], "BXE_TW" : [0],
        "EC_ISE" : [0], "EC_ESE" :[0], "EC_THEORY_TOT" : [0], "EC_TW" : [0],
        "PPS_ISE" :[0], "PPS_ESE" : [0], "PPS_THEORY_TOT" : [0], "PPS_TW" : [0],

        "SGPA" : full_list[11][4] })
        final_df = pd.DataFrame(pd.concat([final_df,new],ignore_index = False))

    if(course_1 == "102003-1"):
        # index for separating the marks of subjects 
        full_list = splitter([11, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23])
        new = pd.DataFrame({
        "Rollno" : full_list[1][4],

        "EM_ISE" :[0], "EM_ESE" :[0], "EM_THEORY_TOT" :full_list[0][0],
        "EM_TW" : [0],
        "SME_ISE" :full_list[0][2], "SME_ESE" :full_list[0][4], "SME_THEORY_TOT" :full_list[0][9],
        "SME_TW" :full_list[2][4],
        "BEE_ISE" :[0], "BEE_ESE" :[0], "BEE_THEORY_TOT" :[0], "BEE_TW" :[0],
        "EM1_ISE" :full_list[5][2], "EM1_ESE" :full_list[5][4], "EM1_THEORY_TOT" :full_list[5][9],
        "EM1_TW" : full_list[6][5],
        "EP_ISE" :[0], "EP_ESE" :[0], "EP_THEORY_TOT" : [0], "EP_TW" : [0],
        "BXE_ISE" : full_list[3][2], "BXE_ESE" :full_list[3][4], "BXE_THEORY_TOT" :full_list[3][9],
        "BXE_TW" : full_list[4][4],
        "EC_ISE" : full_list[7][2], "EC_ESE" :full_list[7][4], "EC_THEORY_TOT" : full_list[7][9],
        "EC_TW" : full_list[8][4],
        "PPS_ISE" :full_list[9][2], "PPS_ESE" : full_list[9][4], "PPS_THEORY_TOT" : full_list[9][9],
        "PPS_TW" : full_list[10][4],
        "SGPA" : full_list[11][4] })
        final_df = pd.DataFrame(pd.concat([final_df,new], ignore_index =  False))
        
    # code for result 2
    if(course_2 == "101011-1"):
        # index for separating the marks of subjects
        full_list = splitter([27, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39])

        new = pd.DataFrame({
         "Rollno" : full_list[1][4],
        "EM_ISE" :full_list[0][2], "EM_ESE" :full_list[0][4], "EM_THEORY_TOT" :full_list[0][9],
        "EM_TW" : full_list[2][4],
        "SME_ISE" :full_list[3][2], "SME_ESE" :full_list[3][4], "SME_THEORY_TOT" :full_list[3][9],
        "SME_TW" :full_list[4][4],
        "BEE_ISE" :full_list[5][2], "BEE_ESE" :full_list[5][4], "BEE_THEORY_TOT" :full_list[5][9],
        "BEE_TW" :full_list[6][4],
        "EM1_ISE" :full_list[7][2], "EM1_ESE" :full_list[7][4], "EM1_THEORY_TOT" :full_list[7][9],
        "EM1_TW" : full_list[8][5],
        "EP_ISE" :full_list[9][2], "EP_ESE" :full_list[9][4], "EP_THEORY_TOT" : full_list[9][9],
        "EP_TW" : full_list[10][4],

        # Zeros
        "BXE_ISE" : [0], "BXE_ESE" :[0], "BXE_THEORY_TOT" :[0], "BXE_TW" : [0],
        "EC_ISE" : [0], "EC_ESE" :[0], "EC_THEORY_TOT" : [0], "EC_TW" : [0],
        "PPS_ISE" :[0], "PPS_ESE" : [0], "PPS_THEORY_TOT" : [0], "PPS_TW" : [0],

        "SGPA" : full_list[11][4] })
        final_df = pd.DataFrame(pd.concat([final_df,new],ignore_index = False))

        
    if(course_2 == "102003-1"):
        # index for separating the marks of subjects
        full_list = splitter([27, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39])
            
        new = pd.DataFrame({
        "Rollno" : full_list[1][4],
        "EM_ISE" :[0], "EM_ESE" :[0], "EM_THEORY_TOT" :[0], "EM_TW" : [0],
        "SME_ISE" :full_list[0][2], "SME_ESE" :full_list[0][4], "SME_THEORY_TOT" :full_list[0][9],
        "SME_TW" :full_list[2][4],
        "BEE_ISE" :[0], "BEE_ESE" :[0], "BEE_THEORY_TOT" :[0], "BEE_TW" :[0],
        "EM1_ISE" :full_list[5][2], "EM1_ESE" :full_list[5][4], "EM1_THEORY_TOT" :full_list[5][9],
        "EM1_TW" : full_list[6][5],
        "EP_ISE" :[0], "EP_ESE" :[0], "EP_THEORY_TOT" : [0], "EP_TW" : [0],
        "BXE_ISE" : full_list[3][2], "BXE_ESE" :full_list[3][4], "BXE_THEORY_TOT" :full_list[3][9],
        "BXE_TW" : full_list[4][4],
        "EC_ISE" : full_list[7][2], "EC_ESE" :full_list[7][4], "EC_THEORY_TOT" : full_list[7][9],
        "EC_TW" : full_list[8][4],
        "PPS_ISE" :full_list[9][2], "PPS_ESE" : full_list[9][4], "PPS_THEORY_TOT" : full_list[9][9],
        "PPS_TW" : full_list[10][4],
        "SGPA" : full_list[11][4] })
        final_df = pd.DataFrame(pd.concat([final_df,new],ignore_index = False))
        
    else:
        print("Course not found")

# converting pdf to csv
def pdf_to_csv(input_pdf):
    with pdfplumber.open(input_pdf) as pdf:
        for page in tqdm(pdf.pages):
            file = []
            lines = page.extract_text().split('\n')
            for line in lines[1:]:
                file.append(line)
            df = pd.DataFrame(file)
            step(df)
    # Write final file
    final_df.to_csv(output_csv, index = False)
pdf_to_csv(input_pdf)
