import sqlite3 as s

db = s.connect('student.db')
print("Database connected successfully")

cursor = db.cursor()

table_name = input("Enter table name: ")
query = f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT, roll_no INTEGER, cgpa FLOAT)"
cursor.execute(query)
print("Table created successfully")

def add_student():
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    roll_no = int(input("Enter roll no: "))
    cgpa = float(input("Enter cgpa: "))
    query = f"INSERT INTO {table_name} (id, name, roll_no, cgpa) VALUES ('{id}','{name}', {roll_no}, {cgpa})"
    cursor.execute(query)
    db.commit()
    print("Record added successfully")

def update_student():
    id = int(input("Enter id: "))
    choice = input("What do you want to update? (name/roll_no/cgpa): ")
    if choice == "name":
        up_name = input("Enter new name: ")
        query = f"UPDATE {table_name} SET name = '{up_name}' WHERE id = {id}"
        cursor.execute(query)
        db.commit()
        print("Record updated successfully")
    elif choice == "roll_no":
        up_roll_no = int(input("Enter new roll no: "))
        query = f"UPDATE {table_name} SET roll_no = {up_roll_no} WHERE id = {id}"
        cursor.execute(query)
    elif choice == "cgpa":
        up_cgpa = float(input("Enter new cgpa: "))
        query = f"UPDATE {table_name} SET cgpa = {up_cgpa} WHERE id = {id}"
        cursor.execute(query)
        db.commit()
        print("Record updated successfully")
    else:
        print("Invalid choice")
def delete_student():
    id = int(input("Enter id: "))
    query = f"DELETE FROM {table_name} WHERE id = {id}"
    cursor.execute(query)
    db.commit()
    print("Record deleted successfully")

def display_student():
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)

def search_student():
    choice = input("What do you want to search? (id/name/roll_no/cgpa): ")
    if choice == "id":
        id = int(input("Enter id: "))
        query = f"SELECT * FROM {table_name} WHERE id = {id}"
        cursor.execute(query)
    elif choice == "name":
        name = input("Enter name: ")
        query = f"SELECT * FROM {table_name} WHERE name LIKE '%{name}%'"
    elif choice == "roll_no":
        roll_no = int(input("Enter roll no: "))
        query = f"SELECT * FROM {table_name} WHERE roll_no = {roll_no}"
    elif choice == "cgpa":
        cgpa = float(input("Enter cgpa: "))
        query = f"SELECT * FROM {table_name} WHERE cgpa = {cgpa}"

    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)

def main():
    while True:
        choice = input("What do you want to do? (add/update/delete/display/search/exit): ")
        if choice == "add":
            add_student()
        elif choice == "update":
            update_student()
        elif choice == "delete":
            delete_student()
        elif choice == "display":
            display_student()
        elif choice == "search":
            search_student()
        elif choice == "exit":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()