print('•••••••••••••••••••••••••••••••••')
print('• Verificación del número mayor •')
print('•••••••••••••••••••••••••••••••••\n')

print('   Ingrese 3 números a verificar\n')

n1=int(input('    >  '))
n2=int(input('    >  '))
n3=int(input('    >  '))
print('    •••••••••••••••••••••••••••••')
if n1 >= n2 and n1 >= n3:
    r = n1
    print('    > El número %s, es el mayor'%n1)
elif n2 >= n1 and n2 >= n3:
    r = n2
    print('    > El número %s, es el mayor'%n2)
else:
    r = n3
    print('    > El número %s, es el mayor'%n3)
print('Fin.')