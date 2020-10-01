import pilha

pilha = pilha.Pilha()

opcao = 0

while opcao != 9:
	print('=== MENU ===')
	print('Escolha uma opção: ')
	print('1 - Empilhar novo elemento')
	print('2 - Desempilhar')
	print('3 - Exibir elemento do topo')
	print('4 - Mostra pilha')
	print('9 - Sair')

	opcao = int(input('Digite uma opção: '))

	if opcao == 1:
		novo_elemento = input('Digite um novo elemento: ')
		pilha.empilha(novo_elemento)

	if opcao == 2:
		elemento_desempilhado = pilha.desempilha()
		print('O elemento desempilhado foi: ', elemento_desempilhado)

	if opcao == 3:
		elemento_do_topo = pilha.elemento_do_topo()
		print('O elemento do topo é: ', elemento_do_topo)

	if opcao == 4:
		print(pilha.mostra_pilha())


print('Encerrando programa...')
print('Obrigado, volte sempre!')

