
from scipy.optimize import linprog

c=[-5,-4]

A=[[2,1],
   [1,3]]

b=[100,150]

x_bounded =(0,None)
y_bounded =(0,None)

result=linprog(c , A_ub=A , b_ub=b , bounds=[x_bounded,y_bounded])

print("A= ",round(result.x[0],2))
print("B= ",round(result.x[1],2))
print("max profit =",round(-result.fun,2))