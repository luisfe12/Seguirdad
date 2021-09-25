import random
import re

#funciones para quitar tildes y volverlo mayúsculas
#-----------------------------------------------------------
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


#-----------------------------------------------------------

# empezamos con el cifrado de ALBERTI

#-----------------------------------------------------------

def Nuevo_Alfabeto(alfabeto):
    posicion_random = random.randint(0, 27)
    while posicion_random == 0:
        posicion_random = random.randint(0, 27)

    nuevo_alfabeto = alfabeto[posicion_random:] + alfabeto[:posicion_random]
    
    return nuevo_alfabeto

def Alberti(mensaje, alfabeto):
    nuevo_alfabeto = Nuevo_Alfabeto(alfabeto)
    mensaje_encriptado = ''
    for i in mensaje:
        if i == ' ' or i == '\n':
            continue
        elif ord(i) < 65  or  ord(i) > 90:
            if i != 'Ñ':
                continue
        #print(i)
        posci_a = nuevo_alfabeto.index(i)
        mensaje_encriptado += alfabeto[posci_a]
    return mensaje_encriptado
    
#-----------------------------------------------------------

# empezamos con el cifrado de VERNAM

#-----------------------------------------------------------
def quitar_signos(poema):
    out = re.sub(r'[^\w\s]','',poema)
    return out

def quitar_espacios(poema):
    texto_1 = re.sub(r"\s+", "", poema)
    texto_2 = quitar_signos(texto_1)
    return texto_2


def tam_sin_Eblanco(texto):
    contador = 0
    for i in texto:
        if i == ' ' or i == '\n': #necesario para evitar leer los saltos de linea
            continue
        contador+=1
    return contador

def Ampliar_clave(texto, clave):
    nueva_cl = ''
    tam_contador = tam_sin_Eblanco(texto)
    modulo = len(texto)%len(clave)
    division = len(texto)//len(clave)

    for i in range(division):
        nueva_cl+=clave
    if modulo == 0:
        return clave
    for i in range(modulo):
        nueva_cl+=clave[i]
    return nueva_cl

def minuscula_clave_ampliar(clave, mensaje):
    clave_minusculas = Ampliar_clave(mensaje, clave)
    clave_minusculas = clave_minusculas.lower()
    return clave_minusculas


def Vernam(mensaje, clave, alfabeto):
    mensaje_enciptado_Verm = ''
    mensaje = quitar_espacios(mensaje)
    mensaje = quitar_signos(mensaje)
    nueva_clave = minuscula_clave_ampliar(clave, mensaje)
    
    
    i = 0
    while i < len(mensaje):
        bin_resul = ord(mensaje[i]) ^ ord(nueva_clave[i])
        no_bin_resul = chr(bin_resul)
        mensaje_enciptado_Verm+=no_bin_resul
        i+=1
    
    #descifrar mensaje, si lo quiere descifrar solo descomente los los comentarios 
    #print('descifrado VERNAM \n')
    mensaje_descif = ''
    for j in range(len(mensaje)):
        bin_re_de = ord(mensaje_enciptado_Verm[j]) ^ ord(nueva_clave[j])
        des_bin_resul = chr(bin_re_de)
        mensaje_descif+=des_bin_resul
    #print(mensaje_descif)

    return mensaje_enciptado_Verm


    

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


f = open ('mensaje_sin_cifrar.txt','r')
mensaje = f.read()
f.close()

#Cifrado ALBERTI
mensaje = Mayusculas_tildes(mensaje)
print('Clave en cifrado Alberti')
print(Alberti(mensaje, alfabeto))


#Cifrado Vernam
clave = 'POSITIVO'
print('\n \n')
print('Clave en cifrado Vernam')
print(Vernam(mensaje, clave, alfabeto))

