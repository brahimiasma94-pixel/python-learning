
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix


# cities: A=0,B=1,C=2,D=3,E=4

cities = ["A","B","C","D","E"]

# distance matrix (0 = no direct road )

graph = np.array ([
    [0,10,3,0,0], # A
    [0,0,1,2,0],  # B
    [0,4,0,8,2],  # C
    [0,0,0,0,5],  # D
    [0,0,0,1,0]   # E
])

df = pd.DataFrame(graph,index= cities,columns= cities)
print(" Distance matrix : ")
print(df)

# solve shortest path

matrix= csr_matrix (graph)

dist_matrix , predecessors = shortest_path(matrix , directed = True, return_predecessors = True)

print ("\n shortest distances from all cities : " )
df_dist = pd.DataFrame(dist_matrix,index=cities,columns=cities)
print(df_dist)

# find actual path from A to D 
start,end = 0,3
path = [end]
while path[-1]!= start:
    path.append(predecessors[start,path[-1]])

path.reverse()
path_cities = [cities[i] for i in path]

print(f"\n shortest path from A to D : ")
print("->".join(path_cities)  )
print(f" Total distance {dist_matrix[start,end]}")

# visualization

fig,axes = plt.subplots(1, 2, figsize = (14,5))

# 1) distance matrix heatmap

ax1=axes[0]
dist_display = dist_matrix.copy()

dist_display[dist_display == np.inf] = 0

im = ax1.imshow(dist_display,cmap="YlOrRd")

ax1.set_xticks(range(5))
ax1.set_yticks(range(5))
ax1.set_xticklabels(cities)
ax1.set_yticklabels(cities)
ax1.set_title("shortest distances matrix")

for i in range(5):
    for j in range(5):
        val = dist_matrix[i,j]
        text = "inf" if val == np.inf else str(val)
        ax1.text(j, i, text, ha="center", va="center", fontsize=10)


plt.colorbar(im,ax=ax1)

# 2) shortest path 

ax2= axes[1]

ax2.set_xlim(0,5)
ax2.set_ylim(0,5)
ax2.axis("off")
ax2.set_title(f"Shortest path A -> D (distance = {dist_matrix[0,3]})")

positions = {"A":(1,4) , "B":(3,4) , "C" : (1,2) , "D":(4,2),"E":(2.5,1)}

# Draw all edges 

for i,c1 in enumerate(cities):
    for j,c2 in enumerate(cities):
        if graph[i,j]>0:
            x=[positions[c1][0],positions[c2][0]]
            y=[positions[c1][1],positions[c2][1]]
            ax2.plot(x,y,"gray",linewidth=1,alpha=0.5)


# Draw shortest path in red

for k in range(len(path_cities)-1):
    c1,c2 = path_cities[k],path_cities[k+1]
    x=[positions[c1][0],positions[c2][0]]
    y=[positions[c1][1],positions[c2][1]]
    ax2.plot(x,y,"red",linewidth=3)

# Draw cities

for city,(x,y) in positions.items():
    color="red" if city in path_cities else "steelblue"
    ax2.plot(x,y,"o",markersize = 30,color=color,alpha=0.7)
    ax2.text(x,y,city,ha="center",va="center",fontsize=13,fontweight="bold",color="white")

plt.suptitle("shortest path problem",fontsize=13)
plt.tight_layout()
plt.show()
        