

def convertir_exadecimal(mensaje):
    nuevo_mensaje = ''
    for i in range(len(mensaje)):
        letra = hex(ord(mensaje[i]))
        nuevo_mensaje = nuevo_mensaje + letra

    return nuevo_mensaje


#este cóiigo solo vuelve lo caracteres raros a utf-8 hexadecimal
f = open ('los_heraldos_negros.txt','r')
mensaje = f.read()
#print(mensaje)
f.close()


print('conversion archivo original \n \n')
print(convertir_exadecimal(mensaje))





print('\n \n')

f = open('HERALDOSNEGROS_pre.txt','r')
mensaje_codificado = f.read()
f.close()

print('conversion archivo ya codificado  \n \n')
print(convertir_exadecimal(mensaje_codificado))
