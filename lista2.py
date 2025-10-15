valores = [] # Criando uma lista vazia

for item in range(10, 14):
    valores.append(item)

print(valores)

# Preenchendo uma lista com dados dinamicos
valores2 = []

while True:
    num= int(input("informe um valor numerico qualquer - zero para encerrar: "))

    if num == 0:
        break
    else:
        valores2.append(num)

print("\nprograma encerrado\n")
print(valores2)