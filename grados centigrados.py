#Conversión de temparaturas.
repetir='S'
while repetir=='S' or repetir=='s':
    print('Ingrese la temperatura en Grados Celcius')
    c=float(input('Temperatura: '))
    print('Presione 1 si desea Grados Fahrenheit')
    print('Presione 2 si desea Grados Rankine')
    print('Presione 3 si desea Grados Kelvin')
    num=int (input('Ingrese la opción : '))
    
    if num==1:
      f=((9/5)*c) + 32
    print(c, 'es equivalente a', f, 'Grados Fahrenheit')
    
    if num==2:
      r=((c*1.8)+491.67)
    print(c, 'es eáuivalente a', r, 'Grados Rankine')
    
    if num==3:
       k=c+273.15
    print(c, 'es equivalente a', k, 'Grados Kelvin')
