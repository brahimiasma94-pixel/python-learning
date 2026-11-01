
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

student={
    "name":["asmaa","sara","yahia","ahmed"],
    "age":  [24,22,25,23],
    "math": [85,90,78,92],
    "science":[88,75,95,60],
    "english":[70,85,80,88]
}

df=pd.DataFrame(student)
print(df)


df["average"]=np.mean(df[["math","science","english"]],axis=1).round(2)
print(df)



df["status"]=df["average"].apply(lambda x :"pass" if x>=80 else "fail")
print(df)



print("===top student===")
print(df[df["average"]==df["average"].max()])

print("\n===lowest student===")
print(df[df["average"]==df["average"].min()])

print("===general statistics===")
print(df[["math","science","english","average"]].describe())

plt.bar(df["name"],df["average"],color="steelblue")
plt.title("student average")
plt.xlabel("name")
plt.ylabel("average")
plt.ylim(0,100)
plt.show()

colors=["steelblue","salmon","mediumseagreen","orange"]
bars=plt.bar(df["name"],df["average"],color=colors)

#show value on top of each bar

for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2,
    bar.get_height()+0.5,
    str(bar.get_height()),
    ha="center")

plt.title("student average")
plt.xlabel("name")
plt.ylabel("average")
plt.ylim(78,86)
plt.show()



