def Cifrado_solo_letras(cifrado):
    contador=0
    for i in cifrado:
        if i == ' ' or i == '\n':
            continue
        contador+=1
    return contador


def modulo_descifrado(p_k, p_c):
    modulo = p_c - p_k
    modulo = modulo % 27

    return modulo



def Clave_completa(clave, modulo, divsion):
    clave_completa = ''

    for i in range(division):
        clave_completa+=clave
    
    if modulo == 0:
        return clave_completa
    
    for i in range(modulo):
        clave_completa+=clave[i]
    
    return clave_completa



def Descifrado_Vignere(clave_modificada, mensaje_cifrado, alfabeto):
    texto_claro = ''
    mensaje_i = 0
    clave_j = 0
    while True:
        if mensaje_i >= len(mensaje_cifrado):
            mensaje_i+=1
            break

        asci = ord(mensaje_cifrado[mensaje_i]) #valor en ascci
        if mensaje_i == ' ' or mensaje_i == '\n':
            mensaje_i+=1
            break
        elif asci < 65 or asci > 90:
            if mensaje_cifrado[mensaje_i] != 'Ñ':
                mensaje_i+=1
                continue
        
        pos_cif = alfabeto.index(mensaje_cifrado[mensaje_i])
        pos_cla = alfabeto.index(clave_modificada[clave_j])

        mod = modulo_descifrado(pos_cla, pos_cif)
        texto_claro+=alfabeto[mod]

        mensaje_i+=1
        clave_j+=1
    print(len(texto_claro))
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


f = open('texto_cifrado.txt', 'r')
menssaje_cifrado = f.read()
f.close()


clave = 'HIELO'
division = len(menssaje_cifrado)//len(clave) 
modulo = Cifrado_solo_letras(menssaje_cifrado) % len(clave)

Clave_modificada = Clave_completa(clave, modulo, division)
#print(len(Clave_modificada))
#print(len(menssaje_cifrado))
print(Descifrado_Vignere(Clave_modificada, menssaje_cifrado, alfabeto))


d = open ('DEScifrado_ejer_15.txt','w')
d.write(Descifrado_Vignere(Clave_modificada, menssaje_cifrado, alfabeto))
d.close()




