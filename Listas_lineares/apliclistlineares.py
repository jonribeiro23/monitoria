# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:31:41 2020

@author: lab53
"""

import listlineares

tamanho=int(input("Digite o tamanho da lista:"))

lista=listlineares.Lista(tamanho)
opc=1

while(opc != 9):
	print()
	print('===== MENU =====')
	print()
	print('1 - Inserir número')
	print('2 - Remover número')
	print('3 - Lista cheia')
	print('4 - Lista vazia')
	print('9 - Sair')
	opc = int(input('Opção: '))
	print()

	if opc == 1:
		print('-- Inserir número --')
		numero = int(input('Digite um número: '))
		lista.insere(numero)
		lista.mostralista()

	elif opc == 2:
		print('-- Remover número --')
		print(lista.remove())
		lista.mostralista()

	elif opc == 3:
		print('A lista está cheia?')
		print(lista.listacheia())

	elif opc == 4:
		print('A lista está vazia?')
		print(lista.listavazia())

	elif opc == 9:
		print('Saindo...')
		print('Obrigado. Volte sempre!')








