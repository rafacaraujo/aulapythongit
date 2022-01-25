# tuplas são criadas e não podem ser modificadas em tempo de execução

# tuplas
dimensoes = (200, 50, 30)

# exibe valor de uma posição especifica da tupla
print(dimensoes[0])
print(dimensoes[1])

# exibe todos os valores da tupla
print(dimensoes)

# percorrendo elementos da tupla

for dimensao in dimensoes:
    print(dimensao)