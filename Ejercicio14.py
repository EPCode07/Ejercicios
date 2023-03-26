print('\n','Números Múltiplos de 3'.center(50),'\n')

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abcm = []
for i in abc:

    if (abc.index(i)+1) % 3 != 0:
        abcm.append(i)
print(abcm)