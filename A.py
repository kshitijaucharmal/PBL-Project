import PyPDF2
import re
import pprint
a=PyPDF2.PdfReader('students.pdf')
b=len(a.pages)
sno=0
s=''
length=[]
k=[]
with open('stext.txt','w') as f:
 with open ('c.csv','w') as e:
  e.write('Rollno,EM_ISE,EM_ESE,EM_THEORY_TOT,EM_TW,SME_ISE,SME_ESE,SME_THEORY_TOT,SME_TW,BEE_ISE,BEE_ESE,BEE_THEORY_TOT,BEE_TW,EM1_ISE,EM1_ESE,EM1_THEORY_TOT,EM1_TW,EP_ISE,EP_ESE,EP_THEORY_TOT,EP_TW,BXE_ISE,BXE_ESE,BXE_THEORY_TOT,BXE_TW,EC_ISE,EC_ESE,EC_THEORY_TOT,EC_TW,PPS_ISE,PPS_ESE,PPS_THEORY_TOT,PPS_TW\n')  
  for i in range(0,b,1):
    s += a.pages[i].extract_text()
    # with open('stext.txt','w') as f:
    #     f.write(s)
    sem2 = re.findall(r'SEM\.:2', s)
    k.append(len(sem2))
    if k[i-1]==k[i]:
         continue
    sno=re.findall(r'F1900\S*', s)
    # print(sem2)
    subject=re.findall(r'101011 ENGINEERING MECHANICS', s,)
    length.append(len(subject))
    m=re.findall(r'[0-9]*/[0-9]*', s)
    #with open ('c.csv','w') as e:
  for i in range(len(sno)):
      if length[i-1]==length[i]:
                e.write(sno[i]+',')
                #First subject SME
                e.write(','*4)
                e.write(m[1+22*i][:3] +',')
                e.write(m[2+22*i][:3] +',')
                e.write(m[3+22*i][:3] +',')
                e.write(m[4+22*i][:3]+',')
                #e.write(t[0][7:10]+',')
                #e.write(g[7][-1:]+',')
                #e.write(g[9][-1:]+',')
                #Third subject em1
                e.write(','*4)
                e.write(m[9+22*i][:3]+',')
                e.write(m[10+22*i][:3]+',')
                e.write(m[11+22*i][:3]+',')
                e.write(m[12+22*i][:3]+',')
                #e.write(t[10][7:10]+',')
                #e.write(g[15][-1:]+',')
                #e.write(g[17][-1:]+',')
                #Second subject BXE
                e.write(','*4)
                e.write(m[5+22*i][:3]+',')
                e.write(m[6+22*i][:3]+',')
                e.write(m[7+22*i][:3]+',')
                e.write(m[8+22*i][:3]+',')
                #e.write(t[5][7:10]+',')
                #e.write(g[11][-1:]+',')
                #e.write(g[13][-1:]+',')
                #Fourth object ec
                e.write(m[13+22*i][:3]+',')
                e.write(m[14+22*i][:3]+',')
                e.write(m[15+22*i][:3]+',')
                e.write(m[16+22*i][:3]+',')
                #e.write(t[15][7:10]+',')
                #e.write(g[19][-1:]+',')
                #e.write(g[21][-1:]+',')
                #Fifth subject pps
                e.write(m[17+22*i][:3]+',')
                e.write(m[18+22*i][:3]+',')
                e.write(m[19+22*i][:3]+',')
                e.write(m[20+22*i][:3]+',\n')
                #e.write(t[20][7:10]+',')
                #e.write(g[19][-1:]+',')
                #e.write(g[21][-1:]+',')
      else :
                e.write(sno[i]+',')
                e.write(m[1+22*i][:3] +',')
                e.write(m[2+22*i][:3] +',')
                e.write(m[3+22*i][:3] +',')
                e.write(m[4+22*i][:3]+',')
                #e.write(t[0]7:10]+',')
                #e.write(g[7][-1:]+',')
                #e.write(g[9][-1:]+',')
                #Second subject sme
                e.write(m[5+22*i][:3]+',')
                e.write(m[6+22*i][:3]+',')
                e.write(m[7+22*i][:3]+',')
                e.write(m[8+22*i][:3]+',')
                #e.write(t[5][7:10]+',')
                #e.write(g[11][-1:]+',')
                #e.write(g[13][-1:]+',')
                #Third subject BEE
                e.write(m[9+22*i][:3]+',')
                e.write(m[10+22*i][:3]+',')
                e.write(m[11+22*i][:3]+',')
                e.write(m[12+22*i][:3]+',')
                #e.write(t[10][7:10]+',')
                #e.write(g[15][-1:]+',')
                #e.write(g[17][-1:]+',')
                #Fourth object em1
                e.write(m[13+22*i][:3]+',')
                e.write(m[14+22*i][:3]+',')
                e.write(m[15+22*i][:3]+',')
                e.write(m[16+22*i][:3]+',')
                #e.write(t[15][7:10]+',')
                #e.write(g[19][-1:]+',')
                #e.write(g[21][-1:]+',')
                #Fifth subject ep
                e.write(m[17+22*i][:3]+',')
                e.write(m[18+22*i][:3]+',')
                e.write(m[19+22*i][:3]+',')
                e.write(m[20+22*i][:3]+',\n')
                #e.write(t[20][7:10]+',')
                #e.write(g[19][-1:]+',')
                #e.write(g[21][-1:]+',') 
                 
      #else:
                #e.write(sno[i]+',')
                #First subject SME
                #e.write(','*3)
                #e.write(m[1][:3] +',')
                #e.write(m[2][:3] +',')
                #e.write(m[3][:3] +',')
                #e.write(m[4][:3]+',')
                #e.write(t[0][7:10]+',')
                #e.write(g[7][-1:]+',')
                #e.write(g[9][-1:]+',')
                #Third subject em1
                #e.write(','*3)
                #e.write(m[9][:3]+',')
                #e.write(m[10][:3]+',')
                #e.write(m[11][:3]+',')
                #e.write(m[12][:3]+',')
                #e.write(t[10][7:10]+',')
                #e.write(g[15][-1:]+',')
                #e.write(g[17][-1:]+',')
                #Second subject BXE
                #e.write(','*3)
                #e.write(m[5][:3]+',')
                #e.write(m[6][:3]+',')
                #e.write(m[7][:3]+',')
                #e.write(m[8][:3]+',')
                #e.write(t[5][7:10]+',')
                #e.write(g[11][-1:]+',')
                #e.write(g[13][-1:]+',')
                #Fourth object ec
                #e.write(m[13][:3]+',')
                #e.write(m[14][:3]+',')
                #e.write(m[15][:3]+',')
                #e.write(m[16][:3]+',')
                #e.write(t[15][7:10]+',')
                #e.write(g[19][-1:]+',')
                #e.write(g[21][-1:]+',')
                #Fifth subject pps
                #e.write(m[17][:3]+',')
                #e.write(m[18][:3]+',')
                #e.write(m[19][:3]+',')
                #e.write(m[20][:3]+',\n')
                #e.write(t[20][7:10]+',')
                #e.write(g[19][-1:]+',')
                #e.write(g[21][-1:]+',')
# e.close()
# f.close()
          

                    
                    