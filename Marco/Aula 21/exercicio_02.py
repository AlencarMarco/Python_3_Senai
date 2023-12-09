import matplotlib.pyplot as plt
import pandas as pd

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y=[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500]

plt.title("Distância percorrida x Energia")
plt.xlabel('Energia')
plt.ylabel('Distancia')
plt.barh(x,y)
plt.show()