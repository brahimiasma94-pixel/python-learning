
from scipy import stats
import numpy as np

grades=[85,90,78,92,88,75,95,60]

print("mean: ",np.mean(grades))
print("median: ",np.median(grades))
print("std : ",np.std(grades))
print("variance: ",np.var(grades))

stat , p=stats.normaltest(grades)

print("p_value:  ",round(p,2))

if p> 0.05:
    print("normal distribution")
else:
    print("not normal distribution")    