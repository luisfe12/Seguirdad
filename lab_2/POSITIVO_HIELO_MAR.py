#todo es es para el de 27 de modulo
def tam_sin_Eblanco(texto):
    contador = 0
    for i in texto:
        if i == ' ' or i == '\n': #necesario para evitar leer los saltos de linea
            continue
         
        contador+=1
    return contador

def quitar_tildes(texto):
    sin_tilde = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in sin_tilde:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto 


def Mayusculas_tildes(texto):
    Sin_minusculas = texto.upper()
    Sin_tildes = quitar_tildes(Sin_minusculas)
    return Sin_tildes

#se obtiene la clave extensa para el cifrado
def Clave_completa(clave, modulo, division):
    clave_extensa = ''
    for i in range(division):
        clave_extensa+=clave
    if modulo == 0:
        return clave_extensa
    
    for i in range(modulo):
        clave_extensa+=clave[i]

    return clave_extensa


def Cifrado_VIGNRE(texto, clave_extensa, alfabeto):
    texto_cifrado = ''
    i = 0 #para el texto
    j = 0 #para la clave
    while True:
        if i  >= len(texto):
            break
        
        asc = ord(texto[i])
        if texto[i] == ' ':
            
            texto_cifrado+=' '
            
            i+=1
            continue
        elif texto[i] == '\n':
            texto_cifrado+='\n'
            
            i+=1
            continue
        elif texto[i] == 'Ñ':
            
            posicion_t = alfabeto.index(texto[i])
            posicion_c = alfabeto.index(clave_extensa[j])

            suma_posiciones = posicion_c + posicion_t
            modulo = suma_posiciones % 27

            texto_cifrado+=alfabeto[modulo]
            
            i+=1
            j+=1
            continue

        elif asc < 65 or asc > 90:
            texto_cifrado+=chr(asc)
            
            i+=1
            continue
        
        posicion_t = alfabeto.index(texto[i])
        posicion_c = alfabeto.index(clave_extensa[j])

        suma_posiciones = posicion_c + posicion_t
        modulo = suma_posiciones % 27

        texto_cifrado+=alfabeto[modulo]
        i+=1
        j+=1
    return texto_cifrado




#--------------------------
#--------------------------

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

    




#---------------------------
###leemos el archivo con el texto sin cifrar

f = open ('mensaje_sin_cifrar.txt','r')
mensaje = f.read()
f.close()

#-----------------------------------------------------

#escribimos en un archivo el cifrado con la clave POSITIVO

#----------------------------------------------------------

clave = 'POSITIVO'

nuevo_mensaje = Mayusculas_tildes(mensaje)
modulo = tam_sin_Eblanco(mensaje) % len(clave)
division = tam_sin_Eblanco(mensaje)//len(clave) #para pbtener el menor entero
clave_extensa = Clave_completa(clave, modulo, division)

p = open ('Cifrado_con_POSITIVO.txt','w')
p.write(Cifrado_VIGNRE(nuevo_mensaje, clave_extensa, alfabeto))
p.close()

#-----------------------------------------------------

#escribimos en un archivo el cifrado con la clave HIELO

#----------------------------------------------------------
clave_2 = 'HIELO'

nuevo_mensaje_2 = Mayusculas_tildes(mensaje)
modulo_2 = tam_sin_Eblanco(mensaje) % len(clave_2)
division_2 = tam_sin_Eblanco(mensaje)//len(clave_2) #para pbtener el menor entero

clave_extensa_2 = Clave_completa(clave_2, modulo_2, division_2)

h = open ('Cifrado_con_HIELO.txt','w')
h.write(Cifrado_VIGNRE(nuevo_mensaje_2, clave_extensa_2, alfabeto))
h.close()


#-----------------------------------------------------

#escribimos en un archivo el cifrado con la clave MAR

#----------------------------------------------------------

clave_3 = 'MAR'

nuevo_mensaje_3 = Mayusculas_tildes(mensaje)
modulo_3 = tam_sin_Eblanco(mensaje) % len(clave_3)
division_3 = tam_sin_Eblanco(mensaje)//len(clave_3) #para pbtener el menor entero

clave_extensa_3 = Clave_completa(clave_3, modulo_3, division_3)

h = open ('Cifrado_con_MAR.txt','w')
h.write(Cifrado_VIGNRE(nuevo_mensaje_3, clave_extensa_3, alfabeto))
h.close()



#-------------------------veamos si cifro como descifra el vignere ejercicio 15


dv = open ('DEScifrado_ejer_15.txt','r')
mensaje_DV = dv.read()
dv.close()


clave_DV = 'HIELO'

nuevo_mensaje_DV = Mayusculas_tildes(mensaje_DV)
modulo_DV = tam_sin_Eblanco(mensaje_DV) % len(clave_DV)
division_DV = tam_sin_Eblanco(mensaje_DV)//len(clave_DV) #para pbtener el menor entero

clave_extensa_DV = Clave_completa(clave_DV, modulo_DV, division_DV)

print(Cifrado_VIGNRE(nuevo_mensaje_DV, clave_extensa_DV, alfabeto))

s_dv = open ('CIFRADO_EJER_15.txt','w')
s_dv.write(Cifrado_VIGNRE(nuevo_mensaje_DV, clave_extensa_DV, alfabeto))
s_dv.close()

