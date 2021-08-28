import math

chave = int(input("Digite o valor chave: "))
v = [0,1,2,3,4,5,6,7,8,9]

i = 0 # índice inicial
f = len(v) - 1 # índice final: onde o tamanho do vetor é n - 1 

def pesquisa_binaria(chave, vetor, inicio, fim):
	meio = math.ceil((inicio + fim)/2) # Arredonda para cima
	print("O índice do meio é: {0}".format(meio))
	if chave == vetor[meio]:
		print("A chave {0} foi encontrada no índice {1}!".format(vetor[meio], meio))
		return
	if inicio == fim:
		print("Acabou a busca, não foi encontrado o valor chave.")
		return
	if chave > vetor[meio]:
		inicio = meio + 1
		pesquisa_binaria(chave, vetor, inicio, fim)
	if chave < vetor[meio]:
		fim = meio - 1
		pesquisa_binaria(chave, vetor, inicio, fim)


pesquisa_binaria(chave, v, i, f)







