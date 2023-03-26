print('\n','Ordenar Números'.center(50),'\n')

n = int(input('¿Cuantos números de la lotería serán?: '))
nlt = [] ; i = 1

while i <= n:
    numeros_ingresados = int(input('Ingrese un número: '))
    nlt.append(numeros_ingresados)
    nlt.sort()
    i+=1
print(f'Los números de la lotería son: {nlt}')