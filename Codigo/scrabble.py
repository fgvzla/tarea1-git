#!/usr/bin/python

import sys

file_name = sys.argv[1]
fp = open(file_name)
arch = fp.readline()
lanterior = ''
no_repetidas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
				"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for line in fp:
	for letra in line:
		if letra == lanterior:
			if no_repetidas.count(letra) > 0:
				no_repetidas.remove(letra)
		lanterior = letra
if len(no_repetidas) > 0:
	print "Las letras que no se repiten de forma consecutiva en ninguna palabra son:"
	print no_repetidas
else:
	print "No hay ninguna letra que no se repita de forma consecutiva"