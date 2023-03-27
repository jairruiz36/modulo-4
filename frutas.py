# Definir el diccionario de precios
precios = {'manzanas': 0.5, 'peras': 0.6, 'melocotones': 0.8, 'plátanos': 0.4}

# Pedir al usuario que introduzca la fruta y la cantidad deseada
fruta = input("Introduce una fruta: ")
kilos = float(input("Introduce el número de kilos que deseas: "))

# Buscar la fruta en el diccionario de precios
if fruta in precios:
    precio_total = precios[fruta] * kilos
    print(f"{kilos} kilos de {fruta} cuestan {precio_total} euros.")
else:
    print("Lo siento, esa fruta no está en nuestro inventario.")
