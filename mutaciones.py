#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import random

def mutacion_uniforme(poblacion,porcentajeMutacion):
	pm = float(porcentajeMutacion)/100
	nuevaPoblacion = []
	for individuo in poblacion:
		ind = list(individuo)
		for i in range(len(ind)):
			r = random.random()
			if r > pm:
				print "mutacion"
				if ind[i] == "0":
					ind[i] = "1" 
				elif ind[i] == "1":
					ind[i] = "0"
		ind = "".join(ind)
		nuevaPoblacion.append(ind)
	print nuevaPoblacion
	"""
	for i in poblacion:
		ind = list(i)
		for j in range(len(ind)):
			p = np.random.random_sample()
			if p > 0.001 and p < 0.010:
				print "mutacion"
				if ind[j] == "0":
					ind[j] = "1" 
				elif ind[j] == "1":
					ind[j] = "0"
		ind = "".join(ind)
		nuevaPoblacion.append(ind)
	return nuevaPoblacion
	"""
	"""
	for i in poblacion:
		porcentaje = np.random.random_sample()	
		if porcentaje > (float(porcentajeMutacion)/100):
				print porcentaje	
	"""

def main():
	poblacion = ["10101010","01010101","10000000","01010101","01010101"]
	porcentajeMutacion = 90
	print poblacion
	mutacion_uniforme(poblacion,porcentajeMutacion)


main()
