from random import randint
import matplotlib.pyplot as plt
import sys



arg = sys.argv[1]

if arg == "levyCurve":

    def f1(x, y): return (x-y)/2, (x+y)/2 

    def f2(x, y): return (x+y)/2 + 0.5, -(x-y)/2 + 0.5 


elif arg == "dragonCurve":
    def f1(x, y): return (x-y)/2, (x+y)/2 

    def f2(x, y): return -(x+y)/2 + 0.5, (x-y)/2 + 0.5 


elif arg == "custom":

    def f1(x, y): return (x-y)/2, (x+y)/2 

    def f2(x, y): return (x+y)/2 + 0.5, (x-y)/2 + 0.5 
else:
    print('Format error')
    sys.exit()

print("10e4 point minimum")
u=input("calculate how many points: ")


x,y = [0],[0]


for n in range(int(float(u))):
    rand = randint(1,2)

    if rand == 1:
        x[n], y[n] = f1(x[n], y[n])
    else:
        x[n], y[n] = f2(x[n], y[n])

    x.append(x[n])
    y.append(y[n])


    
plt.scatter(x, y, s=0.01)
plt.show()


