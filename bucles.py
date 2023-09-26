#Bucle While
'''
import math
numero=int(input("Escirba un numero positivo:"))
while numero<0:
    print("Ingresa un numero posi: ")
    numero=int(input("Escirba un numero positivo:"))
print(f"El resaultado de la raiz cuadrada es: {math.sqrt(numero):1.2f}")
'''
#Bucle For
'''
datos=[1,2,3,4,5,6,67,7,'asdasd']
for i in datos:
    print(i)'''

#Ejercicio bucle for
'''
total=0
for i in range(101):
   total=total+i
print(total)
'''  
#Conjuntos
a={1,2,3,4}
b={2,3,5,6}
c={3,4,6,7}

print(a^b)
