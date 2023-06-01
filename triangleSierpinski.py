from random import randint
import matplotlib.pyplot as plt

print("10e3 point minimum")
u=input("calculate how many points: ")


x,y = [0], [0]

for n in range(int(float(u))):
    trans = randint(1,3)

    if trans == 3:
        x[n] = (x[n] - 3) / 2
        y[n] = (y[n]) / 2
    elif trans == 2:
        x[n] = ( x[n] + 3 ) / 2
        y[n] = (y[n]) / 2
    else:
        x[n] = (x[n]) / 2
        y[n] = (y[n] + 3 ) / 2 

    x.append(x[n])
    y.append(y[n])
    
    

plt.title('Sierpinski Triangle')
plt.scatter(x, y, s=0.5, edgecolor='blue')
plt.scatter(x, y, s=0.001, edgecolors='Red') 

plt.show()