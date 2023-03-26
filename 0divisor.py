print('•Sistema de división•\n')
print('Ingrese los valores')
d  = int(input('  Primer valor(dividendo): '))
di = int(input('  Segundo valor(divisor): '))

if di > 0:
    r = d / di 
    print('El resultado es:', round(r, 2))
else:
    print('\n!Error, ingrese dividendo mayor que 0')
print('Fin.')
    

E