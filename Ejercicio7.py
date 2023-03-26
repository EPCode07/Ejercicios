#Tramos impositivos

print('\n         Sistema de Impuestos')
print('         --------------------\n')

n=input('Ingrese su nombre: ')
print(f'!Bienvenido {n}\n')

r=int(input('¿Cuál es el monto de su renta anual?: '))

if r<=10000:
    rs=5
elif r>10000 and r<=20000:
    rs=15
elif r>20000 and r<=35000:
   rs=20
elif r>35000 and r<=60000:
    rs=30
else:
    rs=45
print(f'{n}, tu total a pagar es: {(r*rs)/100} ')