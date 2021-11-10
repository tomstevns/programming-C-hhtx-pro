import csv
fName = "aFile.csv"

try:
    with open(fName, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            pass #do stuff here

except IOError:
    print "Could not read file:", fName
