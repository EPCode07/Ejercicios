print('•División de Grupos: A y B•\n')

print('¿Cuál es tu nombre?: ')
n=input(' →')
n = n.title()    

print('Elije tu sexo:')
print('  1: Masculino')
print('  2: Femenino')
sx=int(input(' →'))
# < sirve para ver si es anterior a una letra
# > sirve para ver si es posterior a una letra

if sx==2 and n[0]<'M' or sx==1 and n[0]>'N':
    print('Perteneces al Grupo A ')
else:
    print('Perteneces al Grupo B')
