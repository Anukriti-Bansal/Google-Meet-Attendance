import sys
import pandas as pd
import numpy as np
import csv
import math
from glob import glob
import os

dfB1 = pd.read_csv('B1Attendance.csv')
dfB1['EMAILID'] = dfB1['EMAILID'].str.upper()
dfB1['EMAILID'] = dfB1['EMAILID'].str.strip()
B1emailID = np.unique(dfB1['EMAILID'])
column_names = ['Name','Email']
df = pd.DataFrame(columns=column_names)


root = './'
os.chdir(root+'Files/')
file_pattern = 'csv'
list_of_files = [file for file in glob('*.{}'.format(file_pattern))]




Date=''

for f in list_of_files:
    Date = f[0:10]
    print(Date)
    Date = (Date[-2:]+'-'+Date[5:7]+'-'+Date[0:4])
    print(Date)
    data = pd.read_csv(f)
    data['Email'] = data['Email'].str.upper()
    data['Email'] = data['Email'].str.strip()
    emailID = np.unique(data['Email'])
    print("\n\n")
#    print(emailID)
    Duration = []
    TimeJoined = []
    TimeExited = []
    for ID in emailID:
        if ID in B1emailID:
            #print("continue")
            continue
        if ID == 'ANUKRITI.BANSAL@LNMIIT.AC.IN':
            continue
        if ID not in df.values:
            print("If new student attend the class")
            studentData = data.loc[data['Email']==ID]
            df = df.append(studentData.iloc[:,:2], ignore_index=True)
list_of_files.sort()
for f in list_of_files: 
    Date = f[0:10]
    Date = (Date[-2:]+'-'+Date[5:7]+'-'+Date[0:4])
    data = pd.read_csv(f)
    data['Email'] = data['Email'].str.upper()
    data['Email'] = data['Email'].str.strip()

    emailID = np.unique(df['Email'])

    print("No of students from other batches", len(emailID))

    Duration = []
    TimeJoined = []
    TimeExited = []

    for ID in emailID:
        studentData = data.loc[data['Email']==ID]

        if not studentData.empty:
            Duration.append(studentData['Duration'].tolist()[0])
            TimeJoined.append(studentData['Time joined'].tolist()[0])
            TimeExited.append(studentData['Time exited'].tolist()[0])
        else:
            Duration.append('A')
            TimeJoined.append('A')
            TimeExited.append('A')
    df[Date+'(Duration)'] = Duration
#    df[Date+'(TimeJoined)'] = TimeJoined
#    df[Date+'(TimeExited)'] = TimeExited

os.chdir(root)
df.to_csv("AttendanceOthers.csv", index=False)

excelWriter = pd.ExcelWriter('AttendanceOthers.xlsx')
df.to_excel(excelWriter, index=False)
excelWriter.save()


