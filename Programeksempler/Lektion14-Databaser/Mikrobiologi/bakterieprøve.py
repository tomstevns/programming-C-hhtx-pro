
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
    connection = sqlite3.connect('bakterie.db')
    print('connection succesfull')
except:
    print('connection error')



def createTable_bakterie_typer():
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE bakterie_typer ( 
    prøve_nummer INTEGER PRIMARY KEY, 
    type1 VARCHAR(1),
    type2 VARCHAR(1),
    type3 VARCHAR(1),
    type4 VARCHAR(1),
    type5 VARCHAR(1),
    type6 VARCHAR(1),
    type7 VARCHAR(1),
    type8 VARCHAR(1),
    type9 VARCHAR(1),
    type10 VARCHAR(1),
    type11 VARCHAR(1),
    type12 VARCHAR(1),
    type13 VARCHAR(1),
    type14 VARCHAR(1));"""
    return sql_command


def createTable_prøver():
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE prøver ( To be implemented);"""
    return sql_command




def insertIntoTable():
    # SQL command to insert the data in the table
    sql_command = """INSERT INTO bakterie_typer VALUES (5, "","","","","","x","x","x","x","x","x","x","x","x");
    """
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
    crsr.execute("SELECT * FROM bakterie_typer")

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

#cursor
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")


# execute the statement

try:
    crsr.execute(createTable_bakterie_typer())
except:
    print("Maybe table is already created")

try:
    insertIntoTable()
except:
    print("Maybe something is already inserted")


fetchAll()


# close the connection
connection.close()
