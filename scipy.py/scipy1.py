
from scipy import optimize
def equation(x):
    return x**2-4

s=optimize.brentq(equation, 0,3)
print("x= ",s)