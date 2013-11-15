#!/usr/bin/python

import sys

# Abrimos el archivo pasado como parametro
file_name = sys.argv[1]
fp = open(file_name)
arch = fp.readline()

# Definimos lista de todas las letras del abecedario
no_repetidas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
				"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Para cada palabra del archivo se verifica si la letra es igual a la anterior.
# Si son iguales, dicha letra se elimina de la lista en caso de quq no se haya
# borrado ya.
for line in fp:
	lanterior = ''
	for letra in line:
		if letra == lanterior:
			if no_repetidas.count(letra) > 0:
				no_repetidas.remove(letra)
		lanterior = letra

# Si hay letras que no son repetidas de forma consecutiva, se imprimen por pantalla.
# Caso contrario se muestra mensaje de que no se consiguio ninguna letra.
if len(no_repetidas) > 0:
	print "Las letras que no se repiten de forma consecutiva en ninguna palabra son:"
	print no_repetidas
else:
	print "No hay ninguna letra que no se repita de forma consecutiva"