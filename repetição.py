# criando uma tupla

frutas = ("banana", "uva", "morango", "acerola")

print(frutas)

frutas[2] = "manga" # aqui teremos um erro, tuplas são imutaveis

print(frutas[2])

#exibir todos os frutos

for item in frutas:
    print(item)