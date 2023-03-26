print('*****************************************************')
print('"Compañía Multinacional Rappi": Sistema de vacaciones')
print('*****************************************************')

print('\n  ·Ingrese los datos del empleado·\n')
n=input('   1: Nombre: ')
c=int(input('   2: Clave de departamento: '))
a=float(input('   3: Años de antigüedad: '))
if c==1:
    if a >= 1 and a < 2:
        print('\n   >%s, merece 6 días de vacaciones'%n)
    elif a >= 2 and a <= 6:
        print('\n   >%s, merece 14 días de vacaciones'%n)
    elif a >= 7:
        print('%s, merece 20 días de vacaciones'%n)
    else:
        print('\n   >!Aún no accede a vacaciones')
elif c==2:
    if a >= 1 and a < 2:
        print('\n   >%s, merece 7 días de vacaciones'%n)
    elif a >= 2 and a <= 6:
        print('\n   >%s, merece 15 días de vacaciones'%n)
    elif a >= 7:
        print('\n   >%s, merece 22 días de vacaciones'%n)
    else:
        print('\n   >!Aún no accede a vacaciones')
elif c==3:
    if a >= 1 and a < 2 :
        print('\n   >%s, merece 10 días de vacaciones'%n)
    elif a >= 2 and a <= 6:
        print('\n   >%s, merece 20 días de vacaciones'%n)
    elif a >= 7:
        print('\n   >%s, merece 30 días de vacaciones'%n)
    else:
        print('\n   >!Aún no accede a vacaciones')
else:
    print('\n   >!Error, clave departamental incorrecta')
print('Fin.')