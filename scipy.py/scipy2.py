
from scipy.optimize import linprog

c= [-5,-4]
 
#القيود

A=[[2,1]]
b=[100]

#الحدود
x_bounded=(10,None)
y_bounded=(0,None)

result=linprog(c , A_ub=A , b_ub=b , bounds=[x_bounded,y_bounded])

print("A= ",result.x[0])
print("B= ",result.x[1])
print("max profit = ",-result.fun)
