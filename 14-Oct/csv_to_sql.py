# Have 10 to 15 lines of data in csv file.
# Insert these records into employee table.
# employee_data.csv(eg:
# 101, Alice, 60000, 1
# 102, Bob, 75000, 2...)

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Assassincreed@3", database="practice")
cur = mydb.cursor()

with open("employees_data.csv",'r') as file:
    rows = file.readlines()
    for i in rows:
        lines = i.strip().split(",")

        query = "INSERT INTO employees VALUES (%s,%s,%s,%s,%s);"
        cur.execute(query,lines)

mydb.commit()
cur.close()

print("Rows inserted Successfully")
