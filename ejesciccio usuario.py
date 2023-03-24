# Pedir al usuario que introduzca su información personal
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de teléfono: ")

# Crear un diccionario con la información personal del usuario
usuario = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

# Mostrar la información personal del usuario
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")