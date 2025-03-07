import sqlite3

conn = sqlite3.connect("python.db")

print("Database connected")

cursor = conn.cursor()

query = "CREATE TABLE STUDENT(ID INT PRIMARY KEY, NAME TEXT, AGE INT)"
cursor.execute(query)
print("Table created successfully")

query1 = "INSERT INTO STUDENT(ID,NAME,AGE) VALUES(1,'Kaustav Das',20)"
cursor.execute(query1)
conn.commit()
print("1st Record inserted successfully")

query1_1 = "INSERT INTO STUDENT(ID,NAME,AGE) VALUES(2,'Jeet Das',22)"
cursor.execute(query1_1)
conn.commit()
print("2nd Record inserted successfully")

query2 = "SELECT * FROM STUDENT"
cursor.execute(query2)
data = cursor.fetchall()
for row in data:
    print(row)

query3 = "UPDATE STUDENT SET AGE = 21 WHERE ID = 1"
conn.execute(query3)
conn.commit()
print("Record updated successfully")

query4 = "DELETE FROM STUDENT WHERE ID = 2"
conn.execute(query4)
conn.commit()
print("Record deleted successfully")



conn.close()
cursor.close()