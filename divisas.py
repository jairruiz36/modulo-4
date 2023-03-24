divisas={'Buro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa=input('Ingrese la divisa: ')
if divisa in divisas:
    simbolo = divisas[divisa]
    print(simbolo)
else:
    print("La divisa no está en el diccionario")
