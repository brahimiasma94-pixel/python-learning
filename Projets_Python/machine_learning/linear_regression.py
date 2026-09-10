
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
print("\nlibraries imported!")
print("\n")
# Data - advertising budget vs sales
data = {
    "advertising": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "sales":       [15, 25, 32, 42, 55, 58, 72, 80, 88, 102]
}

df = pd.DataFrame(data)
print(df)

# prepare data

X = df[["advertising"]]  #input
Y=  df["sales"]          # output

#split data : 80% train ,20% test

X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)

#train model

model= LinearRegression()
model.fit(X_train,Y_train)

print(f"\nmodel trained! ")
print(f"\n coefficient: {round(model.coef_[0],2)}")
print(f"\n Intercept: {round(model.intercept_ ,2)}")

# Evaluate model
 
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test,Y_pred)
r2=r2_score(Y_test,Y_pred)

print(f"MSE : {round(mse, 2)}")
print(f"R2  : {round(r2,2)}")

# predict new value

budget= float(input("\n Enter advertising budget : "))
prediction=model.predict([[budget]])
print(f"Expected sales:{round(prediction[0],2)}")

#plot
plt.figure(figsize=(8,5))
plt.scatter(X,Y,color="steelblue",label="Real data")
plt.plot(X,model.predict(X),color="red",label="Regression line")
plt.xlabel("Advertising")
plt.ylabel("sales")
plt.title(f"linear Regression(R²={round(r2,2)})")
plt.legend()
plt.grid(True)
plt.show()