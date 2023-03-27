print('Ejercicio N° 17 : Suma de enteros positivos hasta "n" números\n')

def suma(x):
    for i in range(x):
        total_suma = (x*(x+1))/2
    print(total_suma)

while True:
    try:
        numero_n = int(input('Número positivo hasta el que desea sumar: '))     
    except ValueError:
        print("Debes escribir un número.")
        continue
    if numero_n < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break
suma(numero_n)


