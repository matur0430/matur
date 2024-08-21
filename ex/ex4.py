import random
from matplotlib import pyplot as plt
a=random.randint(1,5)
b=random.randint(1,10)
c=random.randint(1,10)
d=random.randint(1,10)
f=random.randint(1,10)
g=random.randint(1,10)

y = [a, b, c, d, f, g]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.plot(x,y,color="red")
plt.show()