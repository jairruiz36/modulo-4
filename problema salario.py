#sb: salario base
#he: horas estra
#b: bonificacion

#se ingresan los datos
sb,he,b=input().split()
sb=float(sb)
he=int(he)
b=int(b)

#se hacen las operaciones
vh=sb/192 #valor de la hora normal
vhe=vh*1.25 #valor hora extra
bon=sb*0.05 #la bonificacion
st=(sb)+(vhe*he)+(bon*b) #salario total
salario=st-((st*0.035)+(st*0.04)+(st*0.01))

#se imprime el salario
print(round(salario,1))
