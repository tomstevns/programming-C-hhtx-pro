import openpyxl
import pandas as pd

def getPasswordFromRecords(myfile):
    df = pd.read_csv(myfile, usecols=[0,0], names=['colA'], header=None)
    print(df)
    return df

def getPasswordFromExcel(myfile):
    df = pd.read_excel(myfile,sheet_name='Navne', usecols="A")


    fourLettersDF = pd.DataFrame(columns=['names'])
    fiveLettersDF = pd.DataFrame(columns=['names'])

    counter4 = 0
    counter5 = 0


    for i in range(len(df)):
        navn = df.iloc[i]['Navn']
        #print(navn)
        if len(navn) == 4:
            fourLettersDF.loc[counter4] = navn
            counter4 = counter4 + 1
        if len(navn) == 5:
            fiveLettersDF.loc[counter5] = navn
            counter5 = counter5 + 1


    #for a in range(len(fourLettersDF)):
    #    print(fourLettersDF.iloc[a]['names'])

    for b in range(len(fiveLettersDF)):
        print(fiveLettersDF.iloc[b]['names'])


    return df

def getPasswordWithLengthFromExcel(myfile,pwlength):
    df = pd.read_excel(myfile,sheet_name='Navne', usecols="A")
    lettersDF = pd.DataFrame(columns=['names'])
    counter = 0

    for i in range(len(df)):
        navn = df.iloc[i]['Navn']
        #print(navn)
        if len(navn) == pwlength:
            lettersDF.loc[counter] = navn
            counter = counter + 1

    #for a in range(len(lettersDF)):
    #    print(lettersDF.iloc[a]['names'])
    return lettersDF


myDF = getPasswordFromRecords("passwords")
#allMyNamesDF = getPasswordFromExcel("navne.xlsx")
#print(myDF)
#print(allMyNamesDF)


nextDF = getPasswordWithLengthFromExcel("navne.xlsx", 4)

for a in range(len(nextDF)):
    for h in range(100):
        print(str(h)+nextDF.iloc[a]['names'])
    for k in range(100):
        print(nextDF.iloc[a]['names']+str(k))

nextDF = getPasswordWithLengthFromExcel("navne.xlsx", 5)

for a in range(len(nextDF)):
    for h in range(10):
        print(str(h)+nextDF.iloc[a]['names'])
    for k in range(10):
        print(nextDF.iloc[a]['names']+str(k))

