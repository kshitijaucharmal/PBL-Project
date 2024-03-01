# Import the required Module

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

# Creating a DataFrame with one row of zeros for each column
df1 = pd.DataFrame({
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

# for page 1
# identifying the course
course_1 = df.iloc[11,0].split(' ')[0]
course_2 = df.iloc[27,0].split(' ')[0]

# code for result 1
if(course_1 == "101011-1"):
    # index for separating the marks of subjects
    a = df.iloc[11,0].split(' ')
    b = df.iloc[9,0].split(' ')
    c = df.iloc[12,0].split(' ')
    d = df.iloc[13,0].split(' ')
    e = df.iloc[14,0].split(' ')
    f = df.iloc[15,0].split(' ')
    g = df.iloc[16,0].split(' ')
    h = df.iloc[17,0].split(' ')
    i = df.iloc[18,0].split(' ')
    j = df.iloc[19,0].split(' ')
    k = df.iloc[20,0].split(' ')
    l = df.iloc[23,0].split(' ')
        
    new = pd.DataFrame({
     "Rollno" : b[4],
    "EM_ISE" :a[2] , "EM_ESE" :a[4] , "EM_THEORY_TOT" :a[9] , "EM_TW" : c[4],
    "SME_ISE" :d[2] , "SME_ESE" :d[4] , "SME_THEORY_TOT" :d[9] , "SME_TW" :e[4] ,
    "BEE_ISE" :f[2], "BEE_ESE" :f[4], "BEE_THEORY_TOT" :f[9] , "BEE_TW" :g[4] ,
    "EM1_ISE" :h[2] , "EM1_ESE" :h[4] , "EM1_THEORY_TOT" :h[9] , "EM1_TW" : i[5],
    "EP_ISE" :j[2] , "EP_ESE" :j[4], "EP_THEORY_TOT" : j[9], "EP_TW" : k[4],
    "BXE_ISE" : [0], "BXE_ESE" :[0] , "BXE_THEORY_TOT" :[0] , "BXE_TW" : [0],
    "EC_ISE" : [0], "EC_ESE" :[0] , "EC_THEORY_TOT" : [0], "EC_TW" : [0],
    "PPS_ISE" :[0] , "PPS_ESE" : [0], "PPS_THEORY_TOT" : [0], "PPS_TW" : [0],
    "SGPA" : l[4] })
    df1 = pd.DataFrame(pd.concat([df1,new],ignore_index = False))

if(course_1 == "102003-1"):
    # index for separating the marks of subjects
    a = df.iloc[11,0].split(' ')
    b = df.iloc[9,0].split(' ')
    c = df.iloc[12,0].split(' ')
    d = df.iloc[13,0].split(' ')
    e = df.iloc[14,0].split(' ')
    f = df.iloc[15,0].split(' ')
    g = df.iloc[16,0].split(' ')
    h = df.iloc[17,0].split(' ')
    i = df.iloc[18,0].split(' ')
    j = df.iloc[19,0].split(' ')
    k = df.iloc[20,0].split(' ')
    l = df.iloc[23,0].split(' ')

    new = pd.DataFrame({
     "Rollno" : b[4],
    "EM_ISE" :[0] , "EM_ESE" :[0] , "EM_THEORY_TOT" :a[0] , "EM_TW" : [0],
    "SME_ISE" :a[2] , "SME_ESE" :a[4] , "SME_THEORY_TOT" :a[9] , "SME_TW" :c[4] ,
    "BEE_ISE" :[0], "BEE_ESE" :[0], "BEE_THEORY_TOT" :[0] , "BEE_TW" :[0] ,
    "EM1_ISE" :f[2] , "EM1_ESE" :f[4] , "EM1_THEORY_TOT" :f[9] , "EM1_TW" : g[5],
    "EP_ISE" :[0] , "EP_ESE" :[0], "EP_THEORY_TOT" : [0], "EP_TW" : [0],
    "BXE_ISE" : d[2], "BXE_ESE" :d[4] , "BXE_THEORY_TOT" :d[9] , "BXE_TW" : e[4],
    "EC_ISE" : h[2], "EC_ESE" :h[4] , "EC_THEORY_TOT" : h[9], "EC_TW" : i[4],
    "PPS_ISE" :j[2] , "PPS_ESE" : j[4], "PPS_THEORY_TOT" : j[9], "PPS_TW" : k[4],
    "SGPA" : l[4] })
    df1 = pd.DataFrame(pd.concat([df1,new], ignore_index =  False))

        
    
# code for result 2
if(course_2 == "101011-1"):
    # index for separating the marks of subjects
    a = df.iloc[27,0].split(' ')
    b = df.iloc[25,0].split(' ')
    c = df.iloc[28,0].split(' ')
    d = df.iloc[29,0].split(' ')
    e = df.iloc[30,0].split(' ')
    f = df.iloc[31,0].split(' ')
    g = df.iloc[32,0].split(' ')
    h = df.iloc[33,0].split(' ')
    i = df.iloc[34,0].split(' ')
    j = df.iloc[35,0].split(' ')
    k = df.iloc[36,0].split(' ')
    l = df.iloc[39,0].split(' ')

    new = pd.DataFrame({
     "Rollno" : b[4],
    "EM_ISE" :a[2] , "EM_ESE" :a[4] , "EM_THEORY_TOT" :a[9] , "EM_TW" : c[4],
    "SME_ISE" :d[2] , "SME_ESE" :d[4] , "SME_THEORY_TOT" :d[9] , "SME_TW" :e[4] ,
    "BEE_ISE" :f[2], "BEE_ESE" :f[4], "BEE_THEORY_TOT" :f[9] , "BEE_TW" :g[4] ,
    "EM1_ISE" :h[2] , "EM1_ESE" :h[4] , "EM1_THEORY_TOT" :h[9] , "EM1_TW" : i[5],
    "EP_ISE" :j[2] , "EP_ESE" :j[4], "EP_THEORY_TOT" : j[9], "EP_TW" : k[4],
    "BXE_ISE" : [0], "BXE_ESE" :[0] , "BXE_THEORY_TOT" :[0] , "BXE_TW" : [0],
    "EC_ISE" : [0], "EC_ESE" :[0] , "EC_THEORY_TOT" : [0], "EC_TW" : [0],
    "PPS_ISE" :[0] , "PPS_ESE" : [0], "PPS_THEORY_TOT" : [0], "PPS_TW" : [0],
    "SGPA" : l[4] })
    df1 = pd.DataFrame(pd.concat([df1,new],ignore_index = False))

    
if(course_2 == "102003-1"):
    # index for separating the marks of subjects
    a = df.iloc[27,0].split(' ')
    b = df.iloc[25,0].split(' ')
    c = df.iloc[28,0].split(' ')
    d = df.iloc[29,0].split(' ')
    e = df.iloc[30,0].split(' ')
    f = df.iloc[31,0].split(' ')
    g = df.iloc[32,0].split(' ')
    h = df.iloc[33,0].split(' ')
    i = df.iloc[34,0].split(' ')
    j = df.iloc[35,0].split(' ')
    k = df.iloc[36,0].split(' ')
    l = df.iloc[39,0].split(' ')

        
    new = pd.DataFrame({
     "Rollno" : b[4],
    "EM_ISE" :[0] , "EM_ESE" :[0] , "EM_THEORY_TOT" :[0] , "EM_TW" : [0],
    "SME_ISE" :a[2] , "SME_ESE" :a[4] , "SME_THEORY_TOT" :a[9] , "SME_TW" :c[4] ,
    "BEE_ISE" :[0], "BEE_ESE" :[0], "BEE_THEORY_TOT" :[0] , "BEE_TW" :[0] ,
    "EM1_ISE" :f[2] , "EM1_ESE" :f[4] , "EM1_THEORY_TOT" :f[9] , "EM1_TW" : g[5],
    "EP_ISE" :[0] , "EP_ESE" :[0], "EP_THEORY_TOT" : [0], "EP_TW" : [0],
    "BXE_ISE" : d[2], "BXE_ESE" :d[4] , "BXE_THEORY_TOT" :d[9] , "BXE_TW" : e[4],
    "EC_ISE" : h[2], "EC_ESE" :h[4] , "EC_THEORY_TOT" : h[9], "EC_TW" : i[4],
    "PPS_ISE" :j[2] , "PPS_ESE" : j[4], "PPS_THEORY_TOT" : j[9], "PPS_TW" : k[4],
    "SGPA" : l[4] })
    df1 = pd.DataFrame(pd.concat([df1,new],ignore_index = False))
    
else:
    print("Course not found")
    

df1.to_csv("Output.csv",index = False)