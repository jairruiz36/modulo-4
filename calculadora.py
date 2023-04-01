class Calculadora:
   
   def inít (self):
       self.vi=float(input('Ingrese un numero a: '))
       self.v2=float(input('Ingrese un numero b: '))
   
   def suma(self):
       suma=self.vl+self.v2
       print('La suma de ví y v2 es: ', suma)
   
   def resta(self):
       suma=self.vl.self.v2
       print('La resta de vl y v2 es: ', suma)
   
   def mul(self):
       mul=self.vi*self.v2
       print('La Multiplicación de vl y v2 es: ', mul)
   
   def div(self):
       if self.v2==0:
           print('ERROR MATH')

       else:
           div=self.v1/self.v2
           print('La divísión de vl y v2 es: ', div)
   
   def pot(self):
       pot=pow(self.v1,self.v2)
       print('La Potencia de vl a v2 es: ', pot)

   def imprimir(self):
       print('Los numeros son: ')
       print('Numero 1', self.v1)
       print('Numero 2', self.v2)