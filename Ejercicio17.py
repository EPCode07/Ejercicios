print('Ejercicio N° 17 : Suma de Enteros Positivos Hasta "n" números\n')
numero_n = int(input('Número positivo hasta el que desea sumar: '))

try:
    if numero_n > 0:
except:
    numero_n = int(input('Número positivo hasta el que desea sumar: '))
    for i in range(numero_n):
            total_suma = (numero_n*(numero_n + 1 ))/2
    print(total_suma)

def suma(x):
    for i in range(x):
        total_suma = (x*(x+1))/2
    print()
    
try:    
    if numero_n > 0:
     suma(numero_n)
except:
    numero_n = int(input('Número positivo hasta el que desea sumar: '))
    suma(numero_n)


