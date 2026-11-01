
from scipy import linalg
import numpy as np

A=np.array([[2,1],
            [1,3]])

b=np.array([8,9])

solution=linalg.solve(A,b)

print("x= ",round(solution[0],2))
print("y= ",round(solution[1],2))