
import sqlite3
import pandas as pd

# 1) connect to database 

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

print("\nDatabase connected !")

# 2) create table

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name        TEXT,
        departement TEXT,
        salary       REAL,
        age          REAL
    )
""")

conn.commit()

print("\nTable created!")

# 3) insert employees

employees = [
    (1,"karim","IT",75000,30),
    (2,"lina","finance",82000,28),
    (3,"omar","IT",68000,35),
    (4,"nadia","HR",71000,32)
]

cursor.executemany("""
    INSERT OR IGNORE INTO employees
    VALUES(?,?,?,?,?)
""",employees)

conn.commit()
print("\ndata inserted!")

# 4)read all students

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("\n all students : ")
for row in rows:
    print(row)

#   5) select with where
print("\n employees in 'IT' : ")

cursor.execute("SELECT id,name,age FROM employees WHERE departement = 'IT' ")
print(cursor.fetchall())

cursor.execute("SELECT name,salary FROM employees ORDER BY salary DESC ")
print(cursor.fetchall())

# 6)load SQL into dataFram

df = pd.read_sql("SELECT * FROM employees",conn)
print("\n datafram sQL : ")
print(df)
df["bonus"]=df["salary"]*0.10
print("\n")
print(df)

#  7) UPDATE_raise karim's salary by 5000

cursor.execute("UPDATE employees SET salary = salary + 5000 WHERE name = 'karim' ")
conn.commit()
print("\n after UPDATE : ")
print(pd.read_sql("SELECT name,salary FROM employees",conn) )

# 8) DELATE omar

cursor.execute(" DELETE FROM employees  WHERE name = 'omar' ")
conn.commit()

print("\n after delete omar : ")
print(pd.read_sql("SELECT * FROM employees",conn))

conn.close()
print("\nconnection is closed!")