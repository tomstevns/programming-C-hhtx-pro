import pandas


def readCSVIntoDataFrame():
    #Let’s see how to read it into a DataFrame using Pandas read_csv() function
    emp_df = pandas.read_csv('employees.csv')
    print(emp_df)



readCSVIntoDataFrame()

