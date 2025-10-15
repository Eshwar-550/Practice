import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Assassincreed@3", database="practice")
cur = mydb.cursor()

with open("department_data.csv",'r') as file:
    rows = file.readlines()
    for i in rows:
        lines = i.strip().split(",")

        query = "INSERT INTO departments VALUES (%s,%s,%s,%s);"
        cur.execute(query,lines)

mydb.commit()
cur.close()

print("Rows inserted Successfully")
