
# Inclusão de valores em lista usando while até atingir uma determinada quantidade

nomes=[]
i = 0

while i<=4:
    nomes.append(input('Digite o nome: '))
    i = i+1

print(nomes)


print('-----------------')

nomes2 = []
resposta = "s"
while resposta =='s':
    nomes2.append(input("Digite o nome: "))
    resposta = input('Deseja continuar?')

print(nomes2)