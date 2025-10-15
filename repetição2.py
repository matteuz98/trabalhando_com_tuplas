numeros = [3, 5, 8, 10, 14]

#print(type(lista))

print(numeros)

numeros[2] = 15

# exibir todos os numeros

for item in numeros:
    print(item)

# inserindo valores no final na lista
numeros.append(23)

print(numeros)

#adicionando itens em qualquer lugar
numeros.insert(2,90) # iremos inserir o valor 90 no indice 2

print(numeros)

#Removendo item da lista
numeros.pop() #removendo item do final da lista
print(numeros)