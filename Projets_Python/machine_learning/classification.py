import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix

print("Libraries imported ! ")

# data_study hours , sleep hours , result
data={
    "study_hours": [2, 8, 5, 1, 7, 3, 9, 4, 6, 2, 8, 1, 7, 5, 3],
     "sleep_hours":[5, 7, 6, 4, 8, 5, 7, 5, 6, 4, 8, 3, 7, 6, 4],
      "result":    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
}
# 0 = fail, 1 = pass
df = pd.DataFrame(data)
print(df)
print(f"\n pass : {df['result'].sum()}")
print(f"\n Fail : {len(df)-df['result'].sum()}")

# prepare data

X = df[["study_hours","sleep_hours"]]
y =df["result"]

# split data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=7)

# train model_KNN
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
print("model trained !")

# Evaluate model

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred , labels=[0,1])

print(f"\n Accuracy : {round(accuracy*100,2)}%")
print(f"\ confusion matrix : ")
print(cm)

print("\n predicted")

print(f"fail   pass")

print(f"fail  {cm[0][0]}     {cm[0][1]}")
print(f"pass  {cm[1][0]}     {cm[1][1]}")

# predict new student
print("\n predict new student : ")

study = float(input("study hours : "))
sleep = float(input("sleep hours : "))

new_student = pd.DataFrame([[study,sleep]],
                           columns=["study_hours","sleep_hours"])
prediction = model.predict(new_student)
result = "pass" if prediction[0] == 1 else "Fail"
print(f"Result : {result}")

# visualization
plt.figure(figsize=(8,6))
# plot training data
colors = ["red" if r==0 else "green" for r in y_train]
plt.scatter(X_train["study_hours"],X_train["sleep_hours"],c=colors,marker="o",s=100,label="train data")

# plot test data
colors_test= ["red" if r==0 else "green" for r in y_test]
plt.scatter(X_test["study_hours"],X_test["sleep_hours"],c=colors_test,marker="^",s=150,label="test data")

# plot new student
plt.scatter(study,sleep,c="blue",marker="*",s=300,label=f"New student({study}h,{sleep}h)")

plt.xlabel("study Hours")
plt.ylabel("sleep Hours")
plt.title("KNN classification _ pass/Fail")
plt.legend()
plt.grid(True)
plt.show()