
import numpy as np

A=np.array([[2,1],
           [1,3]])

print("diterminant: ",np.linalg.det(A))

print("inverse: ",np.linalg.inv(A))

eigenvalues,eigenvectors=np.linalg.eig(A)

print("eigenvalues :",eigenvalues)