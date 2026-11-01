
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

student={
    "name":   ["asmaa","sara","yahia","ahmed"],
    "age":    [24,22,25,23],
    "math":   [85,90,78,92],
    "science":[88,75,95,60],
    "english":[70,85,80,88]
}

class studentManager:
    def __init__(self,data):
        self.df=pd.DataFrame(data)

    def calculate_average (self):
        self.df["average"]=np.mean(self.df[["math","science","english"]],axis=1).round(2)

    def add_status (self):
         self.df["status"]=self.df["average"].apply(lambda x:"pass" if x>=80 else "fail")

    def show_summary(self):
         print("===top student===")
         print(self.df[self.df["average"]==self.df["average"].max()])

         print("\n===lowest student===")
         print(self.df[self.df["average"]==self.df["average"].min()])

         print("===general statistics===")
         print(self.df[["math","science","english","average"]].describe())

    def plot (self):
        colors=["steelblue","salmon","mediumseagreen","orange"]
        bars=plt.bar(self.df["name"],self.df["average"],color=colors)

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

manager=studentManager(student)
manager.calculate_average()
manager.show_summary()
print(manager.df)
manager.plot()

     
         