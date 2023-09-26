#Ejercicio 1
'''
n1=float(input("Valor para n1: "))
n2=float(input("Valor para n2: "))

if (n1%2==0) and (n2%2==0):
    print("Los dos números son pares")
elif (n1%2==0) and (n2%2!=0):
    print("n1 es par, n2 no es par")
elif (n1%2!=0) and (n2%2==0):
    print("n2 es par, n1 no es par")
else:
    print("Los dos no son pares")
'''
#Ejercicio 2
'''
print("Asignarle valores a las siguientes variables: ")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

if a>b and a>c:
    print(f"El mayor de los 3 es: {a}")
elif b>a and b>c:
    print(f"El mayor de los 3 es: {b}")
elif c>a and c>b:
    print(f"El mayor de lo 3 es: {c}")
else:
    print("Los tres son iguales")
'''
#Ejercicio 3
'''
nombre1=input("nombre1: ")
nombre2=input("nombre2: ")
if nombre1[0]==nombre2[0] or nombre1[-1]==nombre2[-1]:
    print("La primera letra o última letra de los nombres son iguales")
else:
    print("No hay coincidencias")
'''
#Ejercicio 4
print("Cajero Autmático El Samu")
print("Menu")
saldo=2000
print("1. Ingreso de dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")
op=int(input("Elija el numero de la operacion:"))
if op==1:
    d=float(input("Ingrese la cantidad de dinero a ingresar:"))
    print(f"Se ingreso exitosamente el dinero")
    saldo+=d
    print(f"Su nuevo saldo es {saldo}")
elif op==2:
    r=float(input("Ingrese la cantidad que desea retirar: "))
    if r<saldo:
        print("Se retiro exitosamente el dinero")
        saldo-=r
        print(f"Su nuevo saldo es {saldo}")
    else:
        print("Saldo insuficiente")
elif op==3:
    print(f"Su saldo es {saldo}")
elif op==4:
    exit()
else: 
    print("No existe esa opcion")