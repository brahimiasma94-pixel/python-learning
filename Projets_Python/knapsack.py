
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Data

items={
    "item":["laptop","phone","tablet","camera","book"],
    "weight":[3,1,4,2,1],
    "value":[10,5,8,7,3]
}

df=pd.DataFrame(items)
print(df)

# knapsack solution using dynamic programming

capacity = 10  # max weight
n=len(df)

weights = df["weight"].tolist()
values  = df["value"].tolist()

# Build Dp table

dp= np.zeros((n+1,capacity+1),dtype=int)

for i in range(1,n+1):
    for w in range (capacity+1):
        # Dont take item i
        dp[i][w]=dp[i-1][w]
        # take item i if it fits
        if weights[i-1] <= w :
            dp[i][w]= max(dp[i][w],dp[i-1][w-weights[i-1]]+values[i-1])

print(f"\n Max value :{dp[n][capacity]}")

# Find which items were selected

selected = []
w= capacity
for i in range(n,0,-1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(df["item"][i-1])
        w -= weights[i-1]

print(f"\n selected items : {selected}")
print(f" TOtal weight : {sum(df[df['item'].isin(selected)]['weight'])} ")        
print(f" TOtal value  :  {sum(df[df['item'].isin(selected)]['value'])} ")        

#visualization

fig,axes = plt.subplots(1,2,figsize=(12,5))

# 1) items camarison

ax1 = axes[0]
colors=["red" if item in selected else "steelblue" for item in df["item"]]
bars = ax1.bar(df["item"],df["value"],color=colors)

ax1.set_title("Item values(red = selected)")
ax1.set_xlabel("Item")
ax1.set_ylabel("value")

for bar,w in zip (bars,df["weight"]):
    ax1.text(bar.get_x()+bar.get_width()/2,
             bar.get_height()+0.2,
             f"w={w}",ha="center",fontsize=9)


# 2) DP table heatmap 
ax2 = axes[1]
im=ax2.imshow(dp,cmap="YlOrRd",aspect="auto")
ax2.set_title("Dp table")
ax2.set_xlabel("capacity")
ax2.set_ylabel("Items")
ax2.set_yticks( range(n+1) )
ax2.set_yticklabels(["0"]+df["item"].tolist())
plt.colorbar(im,ax=ax2)

plt.suptitle(f"knapsack problem_max value : {dp[n][capacity]},fontsize=13")
plt.tight_layout()
plt.show()