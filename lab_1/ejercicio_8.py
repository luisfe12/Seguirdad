

#cobertir unicode 8230

f = open ('los_heraldos_negros.txt','r')
mensaje = f.read()
#print(mensaje)
f.close()


print("texto original \n \n")

print(mensaje.encode('utf-32'))




f = open ('HERALDOSNEGROS_pre.txt','r')
mensaje = f.read()
f.close()


print('\n \n')

print("texto codificado \n \n")

print(mensaje.encode('utf-32'))


