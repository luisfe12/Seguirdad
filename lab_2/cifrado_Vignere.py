

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




#-----------------------------------------------------------------------------------

#CIFRAMOS CON 191 caracteres


#-----------------------------------------------------------




def QUITAR_EPACIOS_MOD191(texto):
    contador = 0
    for i in texto:
        if i == '\n' or i == ' ': #necesario para evitar leer los saltos de linea
            continue
        
        contador+=1
    
    return contador


def CIFRADO_VIGENERE_MOD_191(texto, clave_extensa_mod191, alfabeto_191):
    texto_cifrado_191 = ''
    i=0
    j=0
    n_me = ''
    #print()
    while True:
        if(j >= len(clave_extensa_191)):
            break
        
        if texto[i] == '\n' or texto[i] == ' ':
            texto_cifrado_191+=texto[i]
            i+=1
            continue
    
        pos_mens = alfabeto_191.index(texto[i])
        pos_clave = alfabeto_191.index(clave_extensa_191[j])
        #print(texto[i], " ", clave_extensa_191[j], " ", j)
        
        suma_191 = pos_mens + pos_clave
        mod_191 = suma_191 % 191

        texto_cifrado_191+=alfabeto_191[mod_191]

        i+=1
        j+=1
        
    
    return texto_cifrado_191


#----------------------------------------------------------------------
#alfabeto de 27 caracteres
#-------------------------------------------------------------------------
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

CIFRA = '!"#$%&'
CIFRA_2 = "'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~‘’¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'"
ALFABETO_191 = CIFRA+CIFRA_2




#creamos el VIGNERE este paso fue inecesario, pero representa como se crearia
#la tabla de vignere de 27 caracteres

alfabeto_vignere = []
alfabeto_vignere.append(alfabeto)
tam_alfabeto_original = len(alfabeto)
for i in range(len(alfabeto)):
    temporal = []
    temporal = alfabeto[i:] + alfabeto[:i]
    
    alfabeto_vignere.append(temporal)
    

#leemos el archivo
f = open ('mensaje_sin_cifrar.txt','r')
mensaje = f.read()
f.close()
clave = 'POSITIVO'

# TODA ESTA PARTE HASTA EL FINAL DEL WHILE TRUE ES LA REALIZACION DEL EJERCICIO 
print("Ingres el número 27 si quiere mod de 27 o 191 si dese modulo 191 \n")
print("Ingrese 0 si desea salir\n")
while True:
    modo_alfabeto = int(input("ingrese el digito: "))

    if modo_alfabeto == 0:
        break
    
    elif modo_alfabeto == 27:
        nuevo_mensaje = Mayusculas_tildes(mensaje)
        modulo = tam_sin_Eblanco(mensaje) % len(clave)
        division = tam_sin_Eblanco(mensaje)//len(clave) #para pbtener el menor entero
        clave_extensa = Clave_completa(clave, modulo, division)
        #print usado en el ejerccio 10
        print(Cifrado_VIGNRE(nuevo_mensaje, clave_extensa, alfabeto))

    elif modo_alfabeto == 191:

        modulo_191 = QUITAR_EPACIOS_MOD191(mensaje) % len(clave)
        division_191 = QUITAR_EPACIOS_MOD191(mensaje)//len(clave) #para pbtener el menor entero
        clave_extensa_191 = Clave_completa(clave, modulo_191, division_191)
        print(CIFRADO_VIGENERE_MOD_191(mensaje, clave_extensa_191, ALFABETO_191))

    else:
        print("vuelva a intentar su dígito este fue erroneo \n")

#------------------------------------------------------




#escribimos en un  archivo el cifrado con la clave POSITIVO
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

