print('••••••••••••••••••••••••••••••••••••••••••••••')
print('•Sistema de Recicladora:"TamboGrande Recicla"•')
print('••••••••••••••••••••••••••••••••••••••••••••••\n')

print('Opciones:\n')
print('1: Ingresar')
print('2: Registrarse')
print('3: Restablecer Contraseña\n')
op = int(input('Seleccione una opción: ')) 

if op == 1:
    cla = input('\nIngrese la contraseña: ')
    cla = cla.lower()  
    cla1 = 'hola'
    
    if cla == cla1:
        print('\n!Bienvenido al Sistema')
    else:
         print('!Error, Contraseña Incorrecta')
         
elif op == 2:
    cla = input('\nIngrese la contraseña: ')
    cla2 = input('Ingrese nuevamente la contraseña: ')
    cla = cla.lower()
    cla2 = cla2.lower()   
     
    if cla==cla2:
        print('\n!Registrado Correctamente')
    else:
        print('\n!Error, Las contraseñas no coinciden')    
        
elif op ==3:
    cla = input('\nIngrese su nueva contraseña: ')
    cla2 = input('Ingrese nuevamente la contraseña: ')
    cla = cla.lower()
    cla2 = cla2.lower()
    
    if cla==cla2:
        print('\n!Contraseña restablecida correctamente')
    else:
        print('\n!Error, Las contraseñas no coinciden')
        
else:
    print('\n!Error, Opción inválida')
print('Fin.')
