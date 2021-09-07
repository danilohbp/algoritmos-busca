# Busca Sequencial/Linear
elemento_procurado = int(input("Informe um número inteiro a ser procurado: "))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(lista)):
	if lista[i] == elemento_procurado:
		print("O elemento foi encontrado!")
		
	elif lista[i] == lista[len(lista) - 1]:
		print("O elemento não foi encontrado!") 