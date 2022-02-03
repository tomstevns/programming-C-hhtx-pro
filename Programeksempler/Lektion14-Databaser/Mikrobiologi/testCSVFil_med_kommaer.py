from csv import reader
# skip first line i.e. read header first and then iterate over each row od csv as a list
with open('skylningsforsøg_med_kommaer.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row)
            #sqlcommand = "INSERT INTO bakterie_typer(" + row[0].encode('Windows-1252').decode('utf-8') +","\
            sqlcommand = "INSERT INTO bakterie_typer(" + row[0] +","\
            + row[1] +","\
            + row[2] +","\
            + row[3] +","\
            + row[4] +","\
            + row[5] +","\
            + row[6] +","\
            + row[7] +","\
            + row[8] +","\
            + row[9] +","\
            + row[10] +","\
            + row[11] +","\
            + row[12] +","\
            + row[13] +","\
            + row[14]+")"
            print("sqlcommand =" , sqlcommand)
