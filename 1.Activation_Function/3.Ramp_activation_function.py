from math import*
import numpy as np
from matplotlib import pyplot as plt

def ramp(x):
    y=[]
    i=0;
    while(i<len(x)):
        if x[i]<0:
            y.append(0)
        elif x[i]>1:
            y.append(1)
        else:
            y.append(x[i])
        i+=1
    return y

            
x=np.linspace(-10,10,100)# create 100 points in between -10 to 10
y=ramp(x) # function call 
plt.figure(1)
plt.plot(x,y)
plt.title("ramp activation function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

