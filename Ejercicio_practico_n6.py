titulo = 'Eliminar Substring de una cadena'
print(titulo.center(50,' '))

txtingreso = input('> Ingrese el texto: ')
txtcortar = input('> Ingrese la palabra o letra a cortar: ')

union = ""
# buscar indice
indice = txtingreso.find(txtcortar)
# concatenar las palabras
union = txtingreso[0 :indice]+txtingreso[indice+len(txtcortar)+1:]
#             Inicio         +    Fin[ indice + longitud a cortar + 1]
print(f'\nLa palabra edita es: \n> {union}')