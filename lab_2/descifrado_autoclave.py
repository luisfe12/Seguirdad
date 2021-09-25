def Cifrado_solo_letras(cifrado):
    contador=0
    for i in cifrado:
        if i == ' ' or i == '\n':
            continue
        contador+=1
    return contador

def juantar_partes(parte_clave, clave_encontrada):
    nuevo_clave = parte_clave+clave_encontrada

    return nuevo_clave


def descifrar_partes(clave_nueva_porsion, parte_encriptado, largo, alfabeto, inicial):
    nuevo_texto = ''
    i = inicial
    j = inicial
   
    while j < largo:
        
        if(parte_encriptado[i] == ' ' or parte_encriptado[i] == '\n'):
            i+=1
            continue
        pos_c = alfabeto.index(parte_encriptado[i]) 
        pos_k = alfabeto.index(clave_nueva_porsion[j])
        resta = pos_c - pos_k
        mod = resta % 27
        nuevo_texto+=alfabeto[mod]
        i+=1
        j+=1
        
    return nuevo_texto

    

def descifrado_AUTOCLAVE(mensaje_encriptado, parte_clave, alfabeto):
    tam_inicial = len(parte_clave)
    texto_claro =''
    nuevo_tam = Cifrado_solo_letras(mensaje_encriptado)
    while len(texto_claro) < nuevo_tam:
        #parte_largo = len(mensaje_cifrado)
        marcador = 0
        nuevo_texto = descifrar_partes(parte_clave, mensaje_encriptado, tam_inicial, alfabeto, marcador)
        parte_clave+=nuevo_texto
        texto_claro+=nuevo_texto

        
        marcador+=tam_inicial
    #print(parte_clave)
    #print(len(texto_claro), " ", len(mensaje_encriptado))
    #print(texto_claro[:61])
    return texto_claro


alfabeto =  ['A', 
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L', 
            'M',
            'N',
            'Ñ',
            'O',
            'P', 
            'Q',
            'R',
            'S',
            'T',
            'U', 
            'V',
            'W',
            'X',
            'Y',
            'Z']


f = open('Autoclave_cifrado.txt', 'r')
menssaje_cifrado = f.read()
f.close()

clave_inicial = 'UNODELOSMASGRANDESCRIPTOGRAFOS'

print(descifrado_AUTOCLAVE(menssaje_cifrado, clave_inicial, alfabeto))
#print(Cifrado_solo_letras(menssaje_cifrado))