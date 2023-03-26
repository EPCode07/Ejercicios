print('\n','Palíndromo'.center(50),'\n')
palabra = input('Ingrese un palabra: ')
pa = [] ; parv = []
for i in palabra:
    pa.append(i) ; parv.append(i)    
parv.reverse()
if pa == parv:
    print('Es un Palíndromo')
else:
    print('No es un Palíndromo')