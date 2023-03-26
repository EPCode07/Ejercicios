#Fórmula del IMC: peso (kg) / [estatura (m)]2

print('Ejercicio N° 19 : Calculadora básica del índice de masa corporal\n')
weight = int(input('Ingrese su peso en "Kg": '))
height = float(input('Ingrese su estatura en "m": '))
imc = weight/((height)**2)
print(f'  => Tu índice de masa corporal es: {round(imc,2)}')
print('Fin.')