### PESQUISA BINÁRIA

A pesquisa binária consiste na procura de um valor chave, definido préviamente, para ser buscado em um vetor.
No ínicio da busca encontra-se o meio do vetor que é a soma entre o índice inicial: 0 com o índice final, exemplo: 9 e divide essa
soma por dois, se o resultado for um número decimal é arredondado para cima, logo, se obtém o índice do meio do vetor como um inteiro. Após esse processo
é comparado o valor que se encontra no índice do meio com o valor da chave, se a chave for maior o índice do meio é deslocado uma casa para
frente, exemplo:  meio = meio + 1, esse novo índice do meio é então comparado com a chave e o processo de busca se repete até que ambos os valores sejam iguais ou que se percorra
por completo o vetor até sua parte final. No caso de o valor chave for menor que o meio a busca é realizada sobre os índices anteriores ao índice do
meio, para isso o valor do índice meio será: meio = meio - 1, onde o meio é deslocado para os índices iniciais do vetor até que o valor encontrado no índice meio seja
igual a chave ou acabe o vetor, chegando ao índice 0 e nessa posição o valor seja diferente da chave.
