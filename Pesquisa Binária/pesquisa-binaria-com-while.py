# Pesquisa Binária, divide inicialmente um vetor ao meio a fim de buscar um valor chave nesse vetor
# comparando a chave com o valor do meio encontrado, se o valor do meio for igual ao valor da chave a busca termina, caso contrário,
# se a chave for menor que o meio então a busca é realizada na metade anterior do vetor (ou subvetor, 
# dependendo se o vetor já foi dividido antes e agora a referência é um subvetor, sub subvetor, etc...) e continua a dividir ao meio até que seja
# encontrada a chave, ou até que se chegue ao índice 0 do vetor inicial. O inverso vale para quando a chave é maior que o meio,
# ou seja, a busca começa na metade posterior ao meio do vetor de 6 a 9, até que seja encontrada a chave ou acabe sobrando apenas o índice final: 9.

import math

# Valor chave, é o valor a ser buscado no vetor ordenado
key = int(input("Informe o valor chave entre 0 e 9: "))

# Vetor onde será buscado o valor chave
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Valor do índice inicial do espaço de busca do vetor 
i = 0

# Valor do índice final do espaço de busca do vetor  
f = len(vetor) - 1

achou = False

while achou == False:
	# A função math.ceil arredonda para cima
	meio = math.ceil((i + f)/2)
	print("Meio: {0}".format(meio))

	# Se o valor do meio for igual a chave então foi encontrado e termina a execução do Looping
	if vetor[meio] == key:
		print("O valor chave foi encontrado!")
		achou = True
		break

	# Se o índice inicial for maior do que o final quer dizer que a busca não encontrou em todo o vetor o valor chave
	if i > f:
		print("O valor chave não foi encontrado no vetor!")
		break

	# Se o valor de meio for menor do que o valor de chave significa que a chave, provavelmente, está no lado posterior do meio
	if vetor[meio] < key:
		i = meio + 1
		print("Lista atualizada para o lado posterior do valor encontrado ao meio")

	# Se o meio for maior do que a chave, então, provavelmente a chave está no lado anterior ao meio
	if vetor[meio] > key:
		f = meio - 1
		print("Lista atualizada para o lado anterior ao valor encontrado ao meio")
		
