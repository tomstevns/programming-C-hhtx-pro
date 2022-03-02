import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def stddev(myarray):
    #compute standard deviation
    output = np.std(A)
    #print(output)
    return output


def getIdFromRecords(myfile):
    try:
        df = pd.read_csv(myfile,sep=';',usecols=["id"])
        print(df.get("id"))
        return df
    except:
        print("Oops!", sys.exc_info()[0].__class__, "occurred.")
        return sys.exc_info()[0]

def getHeightFromRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["height"])
    print(df.get("height"))
    return df

def getHeightWithIdFromRecords(myfile,id):
    df = pd.read_csv(myfile,sep=';',usecols=["height"])
    heights = df.get("height")
    print("height with id=", id, "is ",heights[id])
    return df
def getCompleteDataFrameFromRecords(myfile):
    completedf = pd.read_csv(myfile,sep=';',usecols=["id","height","text"])
    print(completedf.get("id"))
    print(completedf.get("height"))
    print(completedf.get("text"))
    return completedf


def getTextFromRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["text"])
    print(df.get("text"))
    return df

def getColumnFromRecords(myfile,columnName):
    """This function has two inputs both the filename and the column to inpect"""
    df = pd.read_csv(myfile,sep=';',usecols=[columnName])
    print(df.get(columnName))
    return df

def getStdDevFromHeightInRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["height"])
    result = df.std()
    print("Standard Deviation is: ",result)
    return result

def getMeanFromHeightInRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["height"])
    result = df.mean()
    print("MEAN value of heights is: ",result)
    return result

def heightInsideStandardDevitation(standarddevitation,meanvalue,height):
    minvalue = meanvalue - standarddevitation
    maxvalue = meanvalue + standarddevitation
    print("minvalue ", minvalue)
    print("maxvalue ", maxvalue)
    print("height ", height)


    if (((minvalue.item()  < height) and (height < maxvalue.item() )) == True):
    #if minvalue.item() < height:
        print("height=", height," is inside Standard deviation")
        return True
    else:
        print("height=", height," is outside Standard deviation")
        return False

def saveAllRecordsWithHeightsInsideStdDevToCSV(dataframe,stddevfile,stddev, mean):
    data_frame_to_csv_file = []
    heights = dataframe.get("height")
    print("height with id=", 0, "is ",heights[0])

    file = open(stddevfile, "a")
    nfile = open(nostdDevFile, "a")
    for i in range(len(heights)):
        if heightInsideStandardDevitation(stddev,mean,heights[i]):
            file.write(str(dataframe.iloc[i]) + "\n\n")
            print("YES")
        else:
            nfile.write(str(dataframe.iloc[i]) + "\n\n")
            print("NO")
    file.close()
    nfile.close()

def plotHistoGram(dataframe):
    plt.hist(dataframe)
    plt.show()

def gangTalMed7(inputTal):
    #printer input
    print("input tal er: ", inputTal)
    #ganger input med 7
    resultat = inputTal*7
    #printer resultat
    print("resultat er: ", resultat)
    #funktionen gangTalMed7() returnerer resultat
    return resultat


##############################
#  Functional TESTING BELOW  #
##############################
#initialize array
A = np.array([170,175,175,180,180,180,180,185,185,190])
aFile = "100records.csv"
stdDevFile = "stdDevFile.txt"
nostdDevFile = "no_stdDevFile.txt"


print("Standardafvigelsen er: ",stddev(A))
getIdFromRecords(aFile)
getHeightFromRecords(aFile)
getTextFromRecords(aFile)
getColumnFromRecords(aFile,"height")

stdDevValue = getStdDevFromHeightInRecords(aFile)
meanValue = getMeanFromHeightInRecords(aFile)

heightInsideStandardDevitation(stdDevValue,meanValue,180)

getHeightWithIdFromRecords(aFile,0)
getHeightWithIdFromRecords(aFile,1)
getHeightWithIdFromRecords(aFile,2)
getHeightWithIdFromRecords(aFile,3)

completeDF = getCompleteDataFrameFromRecords(aFile)
saveAllRecordsWithHeightsInsideStdDevToCSV(completeDF,stdDevFile,stdDevValue,meanValue)

df_heights = getHeightFromRecords(aFile)

plotHistoGram(df_heights)
