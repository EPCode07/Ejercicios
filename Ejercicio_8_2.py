titulo = 'Tabla de Multiplicar'
print('\n',titulo.center(50,'-'),'\n')

numb = int(input('!Bienvenido, ¿Cual es la tabla que desea?: '))
print(f'\nLa tabla del {numb} es :')

for i in range(11):
    print(f'{numb} x {i} = {numb*i}')

print('\nFin de la tabla..')