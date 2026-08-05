
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("E:/pythonn/Projets_Python/sales.db")
cursor =conn.cursor()
print("\nDatabase conected!")

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS sales(
        id               INTEGER PRIMARY KEY,
        product          TEXT,
        month            TEXT,
        quantity         INTEGER,
        price            INTEGER
    ) 
""")
conn.commit()
print("\ntable created !")

sales = [
    (1,  "laptop",  "January",  10, 1200),
    (2,  "phone",   "January",  25,  800),
    (3,  "laptop",  "February", 15, 1200),
    (4,  "phone",   "February", 30,  800),
    (5,  "tablet",  "January",  20,  500),
    (6,  "tablet",  "February", 18,  500)
]

cursor.executemany(""" 
    INSERT OR IGNORE INTO sales
    VALUES(?,?,?,?,?) 
""",sales)
conn.commit()
print("\n data inserted")

cursor.execute("SELECT * FROM sales")
rows=cursor.fetchall()
print("\n all sales : ")
for row in rows:
    print(row)

df=pd.read_sql("SELECT * FROM sales ",conn)
print("\n  datafram SQL : ")
print(df)

df["revenue"]=df["quantity"] * df["price"]

print("\n new datafram : ")

print(df)

# group by product and sum revenue
 
df_product = df.groupby("product")["revenue"].sum()
print("\n Revenue by product : ")
print(df_product)

# plot

plt.figure(figsize=(8,5))
plt.bar(df_product.index,df_product.values,color = ["steelblue","salmon","mediumseagreen"])
plt.title("Total revenue by prodect")
plt.xlabel("product")
plt.ylabel("revenue")

for i,val in enumerate(df_product.values):
    plt.text(i,val+200,str(val),ha="center")

plt.show()    

conn.close()



