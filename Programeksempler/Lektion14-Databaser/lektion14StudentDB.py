"""
Dear ZBC-HTX-Programming teams(B/C),

I've recently started a python assignment which uses the chinook database.
The assignment that I'm stuck on is figuring out which album is listened to most.
Then, I need to write print the top 10 results with the name of the album and the artist,
and the number of times a track is played on the album.
Also, i need to fit all this into one query.
My attempt includes using PyCharm-EDU as IDE:
"""

#connection
"""The sqlite3 package below has to be installed by yourself, 
teherefore please 
- click on the Python Packages tab below 
- search for sqlite3 and install the package"""

import sqlite3
"""
run the code so far to ensure taht the package sqlite 3 is 
installed and enterpreted(understood) successfully"""

"""
You have to ensure that the code runs en a robust manner, 
this is done by encapsulating the connection commands into
try/exeption blocks implemented below 
"""




try:
    connection = sqlite3.connect('lektion14.db')
    print('connection succesfull')
except:
    print('connection error')



def createTable():
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE emp ( 
    staff_number INTEGER PRIMARY KEY, 
    fname VARCHAR(20), 
    lname VARCHAR(30), 
    gender CHAR(1), 
    joining DATE);"""
    return sql_command

def insertIntoTable():
    # SQL command to insert the data in the table
    sql_command = """INSERT INTO emp VALUES (23, "Rishabh",\
    "Bansal", "M", "2014-03-28");"""
    crsr.execute(sql_command)

    # another SQL command to insert the data in the table
    sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates",\
    "M", "1980-10-28");"""
    crsr.execute(sql_command)

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    connection.commit()

def insertingDataInputByTheUser():
    # primary key
    pk = [2, 3, 4, 5, 6]

    # Enter 5 students first names
    f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']

    # Enter 5 students last names
    l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal']

    # Enter their gender respectively
    gender = ['M', 'F', 'M', 'M', 'F']

    # Enter their jpining data respectively
    date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14']

    for i in range(5):

        # This is the q-mark style:
        crsr.execute(f'INSERT INTO emp VALUES ({pk[i]}, "{f_name[i]}", "{l_name[i]}", "{gender[i]}", "{date[i]}")')

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    connection.commit()

def fetchAll():
    print("into fetchAll()")
    # execute the command to fetch all the data from the table emp
    crsr.execute("SELECT * FROM emp")

    # store all the fetched data in the ans variable
    ans = crsr.fetchall()

    # Since we have already selected all the data entries
    # using the "SELECT *" SQL command and stored them in
    # the ans variable, all we need to do now is to print
    # out the ans variable
    for i in ans:
        print(i)

#Point to the database
#Now You are ready to create a SQL command, as a python string
# that soon will be fired against the chinook database

# cursor
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")


# execute the statement

try:
    crsr.execute(createTable())
except:
    print("Maybe table is already created")

try:
    insertIntoTable()
except:
    print("Maybe something is already inserted")
try:
    insertingDataInputByTheUser()
except:
    print("Maybe something is already inserted")








fetchAll()


# close the connection
connection.close()
