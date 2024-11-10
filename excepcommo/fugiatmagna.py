except mysql.connector.Error as err:
    if err.errno == 1049:
        print("Database not found")
    elif err.errno == 1136:
        print("Table not found")
    else:
        print("Unknown error")
