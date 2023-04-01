class alupno:

  def init (self):
     self.nombre=input('ingrese el nombre: ')
     self.nota=float(input('Ingrese la nota: '))

  def imprimir(self):
     print('nombre: ', self.nombre)
     print('su nota es: ', self.nota)

  def resultado(self):
     if self.nota>=3.0:
        print('aprobado')
     else:
        print('reprobado')