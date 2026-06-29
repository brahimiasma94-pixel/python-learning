# ----------------------}-----------------------------------------
# strings indexing & Slicing
# [1] All data in python is object
# [2] object contain Elements
# [3] Every Element has its Index
# [4] python use zero based Indexing ( index start from zero )
# [5] use square brackets [] to Access Element
# [6] Enable Accessing parts of strings , tuples or lists
#----------------------------------------------------------------
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,15,30,25]

plt.plot(x , y)
plt.title("my first chart ")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.bar(x,y)
plt.title("bar chart")
plt.show()

plt.pie(y,labels=["a","b","c","d","e"])
plt.show()

plt.scatter(x,y)
plt.show()

print("git is working")