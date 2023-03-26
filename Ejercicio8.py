print('Sistema de Puntuación\n')
p=float(input('Ingrese su puntuación: '))
tl = 2400
if p == 0.0:
    m = (f'    Nivel de rendimiento: Inaceptable\n    Pago: $/{tl * p}')
elif p == 0.4:
    m = (f'    Nivel de rendimiento: Aceptable\n    Pago: $/{tl * p} ')
elif p >= 0.6:
    m = (f'    Nivel de rendimiento: Memorable\n    Pago: $/{tl * p}')
else:
    m = (f'    !Error, puntuación incorrecta')
print(m)