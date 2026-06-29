
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

def calculate_average (df):
    df["average"]=np.mean(df[["math","science","english"]],axis=1).round(2)
    return df


def add_status (df):
    df["status"]=df["average"].apply(lambda x:"pass" if x>=80 else "fail")
    return(df)


def show_summary(df):
    print("===top student===")
    print(df[df["average"]==df["average"].max()])

    print("\n===lowest student===")
    print(df[df["average"]==df["average"].min()])

    print("===general statistics===")
    print(df[["math","science","english","average"]].describe())


df=pd.DataFrame(student)
df=calculate_average(df)
df=add_status(df)
show_summary(df)
print(df)