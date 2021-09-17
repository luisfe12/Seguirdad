
def insertar_Aqui(texto):
    nuevo_texto=''
    for i in range(len(texto)):
        if (i%20 == 0):
            nuevo_texto = nuevo_texto + 'AQUI'
            continue
        nuevo_texto = nuevo_texto + texto[i]
    return nuevo_texto


    
def modulo_len(mensaje):

    mensaje_AQUI = insertar_Aqui(mensaje)

    if len(mensaje_AQUI) % 4 == 0:
        print(mensaje_AQUI)
    
    else:
        #print('eco__1212')
        modulo = len(mensaje_AQUI)%4
        resta = len(mensaje_AQUI) - modulo
        n_valor = resta + 4
        nueva_resta = n_valor - len(mensaje_AQUI)

        for i in range(nueva_resta):
            mensaje_AQUI = mensaje_AQUI + 'X'
        print(len(mensaje_AQUI))
        print(insertar_Aqui(mensaje_AQUI))

    

#resultado archivo preocesado
f = open ('HERALDOSNEGROS_pre.txt','r')
mensaje = f.read()
f.close()

modulo_len(mensaje)


#esultado archivo original
f = open ('los_heraldos_negros.txt','r')
mensaje_ = f.read()
f.close()

modulo_len(mensaje_)



    
