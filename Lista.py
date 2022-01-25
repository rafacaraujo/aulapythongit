# Declaração de lista (array/vetor)

nomes = ['juan','kauanny','jorge','diogo','rafael','eduardo']
idades = [46,18,38,30,43,38]

print(nomes)

# Listar um unico elemento da lista

print(nomes[2].title())
print(nomes[-2].title())

# Concatenar valores de listas

mensagem = ("O aluno da posição 3 é o "+nomes[3].title()+" e a sua idade é: ",idades[3])

print(mensagem)

motos = ['honda','yamaha','kawasaki',]
print(motos)

motos[0] = 'ducatti'
print(motos)

# Acrescentar valores a lista

motos.append('honda')
print(motos)
print(motos[3])

# Inserir novos elementos na lista em posição determinada

frutas = ['banana','maça','laranja']
frutas.insert(1,'pera')
print(frutas)

# Apagar um elemento da lista

del frutas[1]
print(frutas)

# Ordenação - sort() - sort altera a ordem dentro da lista

print(nomes)
nomes.sort()
print(nomes)

# Ordenar a lista, sem alterar a listagem original - sorted

print('lista original')
print(nomes)

print('Lista alterada temporariamente')
print(sorted(nomes))

# Ordem reversa

print('Ordem inversa de apresentação')
nomes.reverse()
print(nomes)

# Exibe tamanho da lista

print('Tamanho da lista: ',len(nomes))

# Criando listas numéricas
# range()


