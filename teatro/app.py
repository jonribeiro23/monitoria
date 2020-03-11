import teatro
''' subprocess é uma biblioteca para utilizar comandos Linux.
 Se você estiver utilizando Windows, apague as linhas que
 contêm subprocess '''
import subprocess

teatro = teatro.Teatro(5, 5)
opc = 0

while opc != 9:
	print()
	print('=== MENU ===')
	print()
	print('1 - Ver teatro')
	print('2 - Comprar ingresso')
	print('3 - Trocar ingresso')
	print('4 - Devolver ingresso')
	print('9 - Sair')
	print('============')
	opc = int(input('Digite uma opção: '))
	
	# subprocess.call(['clear'])

	if opc == 1:
		teatro.exibe_teatro()
	
	elif opc == 2:
		fila = int(input('Número da fila: '))
		cadeira = int(input('Número da cadeira: '))
		teatro.vende_ingresso(fila, cadeira)

	elif opc == 3:
		fila_antiga = int(input('Fila: '))
		cadeira_antiga = int(input('Cadeira antiga: '))

		nova_fila = int(input('Nova fila: '))
		nova_cadeira = int(input('Nova cadeira: '))
		teatro.trocar_ingresso(fila_antiga, cadeira_antiga, nova_fila, nova_cadeira)

	elif opc == 4:
		fila = int(input('Fila: '))
		cadeira = int(input('Cadeira: '))
		teatro.devolve_ingresso(fila, cadeira)

	elif opc == 9:
		print('Até mais! Volte sempre')

	else:
		print('Opção inválida. Tente outra.')
