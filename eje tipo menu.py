#Ejercicio tipo menu
import math
repetir='s'
while repetir=='S' or repetir=='s':
    a=float(input('Ingrese el coeficiente a: '))
    b=float(input('Ingrese el coeficiente b: '))
    c=float (input('Ingrese el coeficiente c: '))
    #Calculo del discriminante
    disc=b**2-4*a*c
    if disc>0:
       rl=(-b+math.sqrt(disc))/2*a
       r2=(-b-math.sqrt(disc))/2*a
       print(('La raiz 1 es: ',rl,'La raiz 2 es: ',r2))
    else:
       print('Raiz 1: ', -b/2*a,'+', math.sqrt(-disc)/2*a, 'i')
       print('Raiz 2: ', -b/2%a,'-', math.sqrt(-disc)/2*a, 'i')
       repetir=input('iDesea continuar S/N?')