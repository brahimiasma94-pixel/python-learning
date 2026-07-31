
import sqlite3
import pandas as pd

# create Database ( or connect if exists)

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

print("Database connected !")

# create table

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
         id        INTEGER PRIMARY KEY,
         name      TEXT,
         math      INTEGER,
         science   INTEGER,
         english   INTEGER
    )
""")

conn.commit()
print("table created !")

# insert students

students = [
    (1,"asmaa",85,88,70),
    (2,"sara",90,75,85),
    (3,"yahia",78,95,80),
    (4,"ahmed",92,60,88)
]

cursor.executemany("""
    INSERT OR IGNORE INTO students
    VALUES(?,?,?,?,?)
""",students)

conn.commit()
print("Data inserted")

# read all students

cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()
print("\n ==== All students ====" )

for row in rows:
    print (row)

# select with where

print("\n=====student with math > 85 =====")

cursor.execute("SELECT name,math FROM students WHERE math > 85 ")
print(cursor.fetchall())

# order by

print("\n=====students ordered by math=====")
cursor.execute("SELECT name,math FROM students ORDER BY math DESC")
print(cursor.fetchall())

# load SQL data into DataFrame

df= pd.read_sql("SELECT * FROM students",conn)
print("\n========DataFrame FROM SQL====")
print(df)

# use pandas on sql data

df["average"] = df[["math","science","english"]].mean(axis=1).round(2)
df["status"] =  df["average"].apply(lambda x:"pass" if x>=80 else "fail")

print("\n====analysis====")
print(df)
print(f"\n class average  :  {df['average'].mean().round(2)}")
print(f"top student  :  {df.loc[df['average'].idxmax(),'name']} ")

#close connection
conn.close()
print("connection closed")