
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# connect to database

conn = sqlite3.connect("E:/pythonn/Projets_Python/inventory.db")
cursor=conn.cursor()

# create table

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS products(
    id    INTEGER PRIMARY KEY,
    name  TEXT,
    stock INTEGER,
    price REAL,
    min_stock INTEGER
    )
""")
conn.commit()
print("DataBase readi!")

# add product with input

print("\n add new product")
name= input("product name : ")
stock= int(input("current stock : "))
price= float(input("price : "))
min_stock=int(input("minimum stock : "))

cursor.execute("""
    INSERT OR IGNORE INTO products (name, stock, price, min_stock)
    VALUES (?, ?, ?, ?)
""", (name, stock, price, min_stock))

conn.commit()
print(f"{name} added!")

# add sample prodects

sample_products=[
    ("phone",30,800,5 ),
    ("tablet",15,500,8),
    ("camera",25,300,10),
    ("watch",8,150,5)
]

cursor.executemany("""
    INSERT OR IGNORE INTO products (name, stock, price, min_stock)
    VALUES(?,?,?,?)
""",sample_products)

conn.commit()
print("sample products add!")

# show all products

df=pd.read_sql("SELECT * FROM products",conn )
print("\n inventory")
print(df)

# Analysis

print("\n Analysis")

# products below minimum stock

low_stock = df[df["stock"]<df["min_stock"]]
print("\n low stock products : ")
print(low_stock[["name","stock","min_stock"]]  if len(low_stock)>0 else "All stock OK:! ")

# Total inventory value
df["total_value"]= df["stock"]*df["price"]
print(f"\n Total inventory value : {df['total_value'].sum()}")

# Most valuable product
print(f"most valuable : {df.loc[df['total_value'].idxmax(),'name']}")

# visualization

fig,axes =plt.subplots(1,2,figsize = (12,5))

# 1) stock levels
ax1=axes[0]
colors=["red" if s < m else "steelblue"
        for s,m in zip(df["stock"],df["min_stock"])]

bars = ax1.bar(df["name"],df["stock"],color=colors)
ax1.plot(df["name"],df["min_stock"],"r--",label="min stock")
ax1.set_title("stock levels")
ax1.set_ylabel("Quantity")
ax1.legend()

for bar in bars:
    ax1.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() +0.5,
             str(bar.get_height()),
             ha="center",fontsize=9)


# 2) inventory value

ax2=axes[1]
ax2.bar(df["name"],df["total_value"],color="mediumseagreen")
ax2.set_title("Total value by product")
ax2.set_ylabel("value")

for bar , val in zip(ax2.patches , df["total_value"]):
    ax2.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 100,
             str(int(val)),
             ha="center",fontsize=9)


plt.suptitle("Invontory system dashboard",fontsize=13)
plt.show()

# optimization with scipy

print("order optimization")
print("how many units to order to minimize cost?")

order_cost=[50,30,40,20,60]  # shipping cost per unit

#we need to order at least (min_stock) for low stock items
#minimize value gained per cost

c = [-v/ o for v,o in zip(df["price"],order_cost)]  # minimize negative = maximize

#budget constraint

budget = float(input("\nenter available budget: "))

A=[order_cost]
b=[budget]
bounds= [(0, 20) for _ in range(len(df))]  #max 20 units per product

result =linprog(c,A_ub=A, b_ub=b, bounds=bounds)
print("\n optimal order")

for i , name in enumerate(df["name"]):
    units = round(result.x[i],1)
    if units>0:
        print (f"{name} : order {units} units")


print(f"\n max value gained:{round(-result.fun,2)}")
conn.close()
print("\n done!")

