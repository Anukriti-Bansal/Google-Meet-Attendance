import sys
import pandas as pd
import numpy as np
import csv
import math

attendanceFile = sys.argv[1]

df_attend = pd.read_csv(attendanceFile)
df_attend.columns = ['Name', 'Email', 'Duration', 'TimeJoined', 'TimeExited']
df_attend['Email'] = df_attend['Email'].str.upper()
df_attend['Email'] = df_attend['Email'].str.strip()

print(df_attend)

print(attendanceFile)

Date = attendanceFile[0:10]
print(Date)
Date = (Date[-2:]+'-'+Date[5:7]+'-'+Date[0:4])
print(Date)

dfB1 = pd.read_csv('B1Attendance.csv')
dfB1['EMAILID'] = dfB1['EMAILID'].str.upper()
dfB1['EMAILID'] = dfB1['EMAILID'].str.strip()
emailID = np.unique(dfB1['EMAILID'])

print("Number of students in B1",len(emailID))
print(dfB1)

df = dfB1


print(df)

Duration = []
TimeJoined = []
TimeExited = []

for ID in emailID:
    studentData = df_attend.loc[df_attend['Email']==ID]
    if not studentData.empty:
        Duration.append( studentData['Duration'].tolist()[0])
        TimeJoined.append(studentData['TimeJoined'].tolist()[0])
        TimeExited.append(studentData['TimeExited'].tolist()[0])
    else:
        Duration.append('A')
        TimeJoined.append('A')
        TimeExited.append('A')

df[Date+'(Duration)'] = Duration
df[Date+'(TimeJoined)'] = TimeJoined
df[Date+'(TimeExited)'] = TimeExited

df.to_csv('B1Attendance.csv',index=False)


excelWriter = pd.ExcelWriter('B1Attendance.xlsx')
df.to_excel(excelWriter, index=False)
excelWriter.save()


print(df)
