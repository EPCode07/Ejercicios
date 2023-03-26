print('••••••••••••••••••••••••••••••')
print('•Sistema de Tributos Nacional•')
print('••••••••••••••••••••••••••••••\n')

print('Ingrese sus datos: \n')

n = input('Nombre: ')
e = int(input('Edad: '))
sl = int(input('Sueldo Mensual: '))

if e >16 and sl >= 1000:
    print('\n->',n,', ya tributas')
else:
    print('\n–>',n,', aun no tributas')