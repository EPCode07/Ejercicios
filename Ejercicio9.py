print('**Cabinas IntraNet**')

e = int(input('    Ingrese su edad: '))

if e < 4:
    m = ('      > Entrada: $/0')
elif e >=4 and  e <= 18:
    m = ('      > Entrada: $/5')
elif e > 18:
    m = ('      > Entrada: $10')
print(m)