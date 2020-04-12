from math import*
import numpy as np
from matplotlib import pyplot as plt

def linear(x):
    return x

x=np.linspace(-10,10,100)# create 100 points in between -10 to 10
y=linear(x) # function call 
plt.plot(x,y)
plt.title("linear activation function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()