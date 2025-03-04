import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Uncomment each part to test the code
#First Part
#I
df = pd.read_csv('AdmissionPredict.csv')
'''
print(df.head())

print(df.describe())

print(df.info())
'''

#II
#print(df.isna().sum())

#III
df['GRE Score'] = df['GRE Score'].fillna(df['GRE Score'].mean())
df['TOEFL Score'] = df['TOEFL Score'].fillna(df['TOEFL Score'].mean())
df['University Rating'] = df['University Rating'].fillna(df['University Rating'].mean())
df['SOP'] = df['SOP'].fillna(df['SOP'].mean())
df['LOR '] = df['LOR '].fillna(df['LOR '].mean())
df['CGPA'] = df['CGPA'].fillna(df['CGPA'].mean())
df['Research'] = df['Research'].fillna(df['Research'].mean())
#print(df.isna().sum())

#Second Part
#I
'''
plt.scatter('Serial No.', 'Chance of Admit', c='#b5347e', data=df)
plt.xlabel('Serial No.')
plt.ylabel('Chance of Admit')
plt.show()

plt.scatter('GRE Score', 'Chance of Admit', c='#9a34b5', data=df)
plt.xlabel('GRE Score')
plt.ylabel('Chance of Admit')
plt.show()

plt.scatter('TOEFL Score', 'Chance of Admit', c='#1cc32f', data=df)
plt.xlabel('TOEFL Score')
plt.ylabel('Chance of Admit')
plt.show()

plt.scatter('University Rating', 'Chance of Admit', c='#1691a7', data=df)
plt.xlabel('University Rating')
plt.ylabel('Chance of Admit')
plt.show()

plt.scatter('SOP', 'Chance of Admit', c='#de6722', data=df)
plt.xlabel('SOP')
plt.ylabel('Chance of Admit')
plt.show()

plt.scatter('LOR ', 'Chance of Admit', c='#e5d700', data=df)
plt.xlabel('LOR ')
plt.ylabel('Chance of Admit')
plt.show()

plt.figure()
plt.scatter('CGPA', 'Chance of Admit', c='#e500a9', data=df)
plt.xlabel('CGPA')
plt.ylabel('Chance of Admit')
plt.show()

plt.scatter('Research', 'Chance of Admit', c='#eb8def', data=df)
plt.xlabel('Research')
plt.ylabel('Chance of Admit')
plt.show()
'''

#II
#Reported Property = CGPA

#Third Part
#I
CGPA_filtered = df[df['CGPA'] >= 9]
TOEFL_filtered = CGPA_filtered[CGPA_filtered['TOEFL Score'] >= 110]
array = np.array(TOEFL_filtered['Serial No.'])
print("Number of Students with CGPA >= 9 and TOEFL Score >= 110 :")
#print(array.size)

#II
'''
rank1 = df[df['University Rating'] == 1]
print("Average of GRE Scores of Students from Universities with rank 1 :")
print(rank1['GRE Score'].mean())

rank2 = df[df['University Rating'] == 2]
print("Average of GRE Scores of Students from Universities with rank 2 :")
print(rank2['GRE Score'].mean())

rank3 = df[df['University Rating'] == 3]
print("Average of GRE Scores of Students from Universities with rank 3 :")
print(rank3['GRE Score'].mean())

rank4 = df[df['University Rating'] == 4]
print("Average of GRE Scores of Students from Universities with rank 4 :")
print(rank4['GRE Score'].mean())

rank5 = df[df['University Rating'] == 5]
print("Average of GRE Scores of Students from Universities with rank 5 :")
print(rank5['GRE Score'].mean())
'''

#Fourth Part
#I
new_df = df.loc[:, ['CGPA', 'Chance of Admit']]
x = df['CGPA']
y = df['Chance of Admit']
xm = df['CGPA'].mean()
ym = df['Chance of Admit'].mean()
n = x.size

#II
SSxy = x * y - n * xm * ym
SSxy = SSxy.mean() * n

SSxx = x * x - n * xm * xm
SSxx = SSxx.mean() * n

theta1 = SSxy / SSxx
theta0 = ym - theta1 * xm

h = theta0 + theta1 * x

j = (h - y)**2
j = j.mean() / 2 

'''
print("Mean Square Error :")
print(j)

plt.scatter('CGPA', 'Chance of Admit', c='#e500a9', data=df)
plt.scatter(x, h, c='g')
plt.xlabel('CGPA')
plt.ylabel('Chance of Admit')
plt.show()

#III
NaN_filtered = df[pd.isna(df['Chance of Admit'])]
print("Students with Missing Chance of Admits :")
print(NaN_filtered)

NaN_filtered['Chance of Admit'] = theta0 + theta1 * NaN_filtered['CGPA']
print("Output of my Model to Fill Missing Chance of Admits :")
print(NaN_filtered)
'''