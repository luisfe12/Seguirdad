from collections import Counter


def buscar_trigrama(arr1, arr2):
    for i in range(len(arr2)):
        if arr1 == arr2[i]:
            return True

    return False

def comparar_substring(sub_cadena):
    if sub_cadena[0] == sub_cadena[1] and sub_cadena[0] == sub_cadena[2]:
        return True
    return False

def comparar_arreglos(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            continue
        else:
            return False
    return True


#leer archivo 
f = open('HERALDOSNEGROS_pre.txt','r')
mensaje_codificado = f.read()
f.close()

#mensaje_codificado = 'fsdvdfvdfbvnnnefsedfsdfegrthrtgrhaaaacrferbcvbcgxxxcerterrr'

arreglo_de_substring = []
arreglo_de_posiciones = []
arreglo_alamacenamientorepe = []


for i in range(len(mensaje_codificado)):
    if i+2 > len(mensaje_codificado)-1:
        #print('salto')
        break
    sub_arreglo = mensaje_codificado[i:i+3]
    arreglo_de_substring.append(sub_arreglo)
    #print(sub_arreglo)
    j = i+1
    posiciones = []
    while j <= len(mensaje_codificado):
        #print(j)
        
        #print(len(mensaje_codificado[j:j+3]))
        if j+2 > len(mensaje_codificado)-1:
            break
        if(comparar_arreglos(sub_arreglo, mensaje_codificado[j:j+3])):
            #print("igulaes de los 3")
            #print(sub_arreglo)
            #print(mensaje_codificado[j:j+3])
            valor_dis = j-i+2
            texto_val =str(valor_dis)
            if buscar_trigrama(sub_arreglo, arreglo_alamacenamientorepe) == False:
                arreglo_alamacenamientorepe.append(sub_arreglo)
                posiciones.append(valor_dis)
                #arreglo_alamacenamientorepe[len(arreglo_alamacenamientorepe)-1] + " " + texto_val
                posiciones.append(valor_dis)
                continue
            #arreglo_alamacenamientorepe[len(arreglo_alamacenamientorepe)-1] + " " + texto_val
             
            posiciones.append(valor_dis)
        j+=1
    arreglo_de_posiciones.append(posiciones)


    #booleano = comparar_substring(sub_arreglo)
    #if booleano == True:
    #    print('entro')
    #   arreglo_de_substring.append(sub_arreglo)
    #    arreglo_posicion = [i,i+2]
    #    arreglo_de_posiciones.append(arreglo_posicion)

#encontramos trigramas repetidos




#print(arreglo_de_substring)
#print(arreglo_de_posiciones)

#print(len(arreglo_de_posiciones))

print("valores repetidos \n")
print(arreglo_alamacenamientorepe)
print("\n \n distancias \n")
print(arreglo_de_posiciones)
#unigrams = word_tokenize("The quick brown fox jumps over the lazy dog")
#bigrams = bigrams(unigrams)



