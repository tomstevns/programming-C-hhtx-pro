import numpy as np
import pandas as pd
import csv

#initialize array
A = np.array([170,175,175,180,180,180,180,185,185,190])



def stddev(myarray):
    #compute standard deviation
    output = np.std(A)
    #print(output)
    return output


def getIdFromRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["id"])
    print(df.get("id"))

def getHeightFromRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["height"])
    print(df.get("height"))

def getHeightWithIdFromRecords(myfile,id):
    df = pd.read_csv(myfile,sep=';',usecols=["height"])
    heights = df.get("height")
    print("height with id=", id, "is ",heights[id])


def getTextFromRecords(myfile):
    df = pd.read_csv(myfile,sep=';',usecols=["text"])
    print(df.get("text"))

def getColumnFromRecords(myfile,columnName):
    """This function has two inputs both the filename and the column to inpect"""
    df = pd.read_csv(myfile,sep=';',usecols=[columnName])
    print(df.get(columnName))

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

    if (((minvalue.item()  < height) or (height < maxvalue.item() )) == True):
    #if minvalue.item() < height:
        print("height=", height," is inside Standard deviation")
        return True
    else:
        print("height=", height," is outside Standard deviation")
        return False

###################
#  TESTING BELOW  #
###################

aFile = "100records.csv"

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

