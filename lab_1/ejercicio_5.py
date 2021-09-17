from matplotlib import pyplot as plt

#valore del abecedario con sus contadores
abecedario = [['A',0], 
              ['B',0],
              ['C',0],
              ['D',0],
              ['E',0],
              ['F',0],
              ['G',0],
              ['H',0],
              ['I',0],
              ['J',0],
              ['K',0],
              ['L',0], 
              ['M',0],
              ['N',0],
              ['Ñ',0],
              ['O',0],
              ['P',0], 
              ['Q',0],
              ['R',0],
              ['S',0],
              ['T',0],
              ['U',0], 
              ['V',0],
              ['W',0],
              ['X',0],
              ['Y',0],
              ['Z',0]]



f = open('HERALDOSNEGROS_pre.txt','r')
mensaje_codificado = f.read()
f.close()

print(mensaje_codificado)

for i in range(len(mensaje_codificado)):
    for j in range(len(abecedario)):
        if mensaje_codificado[i] == abecedario[j][0]:
           # print('entro')
            abecedario[j][1] = abecedario[j][1] + 1

print('Diccionario de las letras y repeticiones \n')
print(abecedario)



#ordenamos para sacar los 5 más repetidos

abecedario_ordenado = sorted(abecedario, key=lambda abc : abc[1])

print('\n \n')
print('Las 5 letras más repetidas \n')
print(abecedario_ordenado[len(abecedario)-5:])


plt.bar(*zip(*abecedario_ordenado))
plt.show()
