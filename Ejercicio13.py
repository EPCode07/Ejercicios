print('\n','Eliminación de Asignaturas'.center(50),'\n')

asg = ['Matemáticas','Física','Química','Historia','Lengua']
desp = []

for i in asg:
    nt = int(input(f'Nota de {i}: '))   
    if nt < 6:
        desp.append(i)
    
print('\nLas materias desaprobadas son:\n')
print(*desp,sep=',')