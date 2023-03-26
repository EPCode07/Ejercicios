titulo = 'Método con While o For'
print('\n',titulo.center(50,'-'),'\n')

ing = input('Ingrese el texto a editar: ')
stop = input('¿Donde desea parar el texto?: ')

#opción 1
for i in range(0 , len(ing)):   
    ing2 = ing[i].lower()
    if stop.lower() == ing2:
        break
    elif ing2 == 'a' or ing2 =='e' or ing2== 'i' or ing2=='o' or ing2=='u':
        continue
    print(ing[i],end='')
print('\nFin..\n')

#opción 2
for i in ing:    
    if i.lower() == stop.lower():
        break
    elif i.lower()=='a' or i.lower()=='e' or i.lower=='i' or i.lower()=='o' or i.lower()=='u':
        continue
    print(i,end='')
print('\nFin..')