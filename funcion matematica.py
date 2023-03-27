#Funcio de la recta
from matplotlib import pyplot as plt
def linea(x):
  return x

def cuadrado(x):
  return x**2
l=[]
m=[]
for i in range(-3,4):
  l.append(linea(i))
  m.append(cuadrado(i))

print(m)
plt.plot(1,1)
plt.plot(1,m)
plt.grid()
plt.show()
