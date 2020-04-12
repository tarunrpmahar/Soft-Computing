from math import*
import numpy as np
from matplotlib import pyplot as plt

def logsig(x):
    y=[]
    i=0
    while(i<len(x)):
        y.append(1/(1+exp(-x[i])))
        i+=1
    return y

            
x=np.linspace(-10,10,100)# create 100 points in between -10 to 10
y=logsig(x) # function call 
plt.figure(1)
plt.plot(x,y)
plt.title("logsigmoid activation function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

