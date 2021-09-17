import re



#las tilde de cada vocal despareceran
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


#remplaza las letras j x i, h x i, ñ x n, k x l, u x v, w x v, y x z
def remplazo_letras(texto):
    r_letras = (
        ("j", "i"),
        ("h", "i"),
        ("ñ", "n"),
        ("k", "l"),
        ("u", "v"),
        ("w", "v"),
        ("y", "z"),
    )
    for a, b in r_letras:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto


#convierte solo las mayusculas en minusculas
def convertir_mayusculas(poema):
    mayusculas_todo = ''
    for i in range(len(poema)):
        
        valor = ord(poema[i])

        if valor >= 65 and valor <= 90:
            p_ = chr(valor)
            mayusculas_todo=mayusculas_todo+p_
            continue
        
        elif valor < 97 or valor > 122:
            continue
        valor = valor - 32
        p = chr(valor)
        mayusculas_todo =mayusculas_todo + p
    return mayusculas_todo



#se usa en la funcion quitar_espacios
def quitar_signos(poema):
    out = re.sub(r'[^\w\s]','',poema)
    return out

#quita espacios en blaco y saltos de linea
def quitar_espacios(poema):
    texto_1 = re.sub(r"\s+", "", poema)
    texto_2 = quitar_signos(texto_1)
    return texto_2



#funcion donde corre todo el código

f = open ('los_heraldos_negros.txt','r')
mensaje = f.read()
#print(mensaje)
f.close()

#m1=re.sub(r"\s+", "", mensaje)

m1 = quitar_espacios(mensaje)

print(m1)
m2 = quitar_tildes(m1)

print(m2)
m3 = remplazo_letras(m2)

print(m3)

texto_final = convertir_mayusculas(m3)


print(texto_final)

#escribimos en el archivo

f = open ('HERALDOSNEGROS_pre.txt','w')
f.write(texto_final)
f.close()


#print(quitar_tildes(m1))
#print(remplazo_letras(m1))
#print(convertir_mayusculas(m1))
#print(quitar_signos(m1))