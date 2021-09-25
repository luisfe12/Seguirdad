from matplotlib import pyplot as plt

def resturar_abecedario(abecedario_):
    i = 0
    j = len(abecedario_) - 1

    while i <= j:
        abecedario_[i][1] = 0
        abecedario_[j][1] = 0
        i+=1
        j-=1
    
    return abecedario_


def dibujar(abecedario_ordenado):
    plt.bar(*zip(*abecedario_ordenado))
    plt.show()



def frecuencia_valores(mensaje_codificado, abecedario):
    for i in range(len(mensaje_codificado)):
        for j in range(len(abecedario)):
            if mensaje_codificado[i] == abecedario[j][0]:
            # print('entro')
                abecedario[j][1] = abecedario[j][1] + 1
    
    abecedario_ordenado = sorted(abecedario, key=lambda abc : abc[1])

    dibujar(abecedario_ordenado)

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


abecedario_POSITIVO = abecedario


abecedario_HIELO = abecedario

abecedario_MAR = abecedario



#histograma de frecuencia en POSITIVO

P = open('Cifrado_con_POSITIVO.txt','r')
mensaje_codificado = P.read()
P.close()


frecuencia_valores(mensaje_codificado, abecedario_POSITIVO)

print(abecedario_POSITIVO)


abecedario = resturar_abecedario(abecedario)
#histograma de frecuencia en HIELO

H = open('Cifrado_con_HIELO.txt','r')
mensaje_codificado = H.read()
H.close()


frecuencia_valores(mensaje_codificado, abecedario_HIELO)

print(abecedario_HIELO)

abecedario = resturar_abecedario(abecedario)

#histograma de frecuencia en MAR

M = open('Cifrado_con_MAR.txt','r')
mensaje_codificado = M.read()
M.close()


frecuencia_valores(mensaje_codificado, abecedario_MAR)

print(abecedario_MAR)