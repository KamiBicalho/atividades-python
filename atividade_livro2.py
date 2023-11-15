#questão 8
A = 4
B = 5
C = 1
x1 = 1
y1 = 1
x2 = 4
y2 = 5

R = (A + B) / 2
X = (-B + ((B ** 2 - 4 * A * C) ** (1 / 2))) / (2 * A)
S = (3 * A + 2 * B) / (A + B)
Z = 7.6 * A - B ** 1.7
d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) #serviu de base para a questão 9

print(R)
print(X)
print(S)
print(Z)
print(d)

# #questão 9 
# x1 = float(input("Digite o valor de x1:"))
# y1 = float(input("Digite o valor de y1:"))
# x2 = float(input("Digite o valor de x2:"))
# y2 = float(input("Digite o valor de y2:"))
# distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
# print(round(distancia, 3))

#questão 10
primeiro_produto = input("Digite o nome do primeiro brinquedo: ")
vendas_primeiro_produto = int(input("Quantidade vendida: "))
valor_primeiro_produto = float(input("Valor do primeiro produto: "))
segundo_produto = input("Digite o nome do segundo brinquedo: ")
vendas_segundo_produto = int(input("Quantidade vendida: "))
valor_segundo_produto = float(input("Valor do segundo produto: "))
terceiro_produto = input("Digite o nome do terceiro brinquedo: ")
vendas_terceiro_produto = int(input("Quantidade vendida: "))
valor_terceiro_produto = float(input("Valor do terceiro produto: "))

faturamento_primeiro = vendas_primeiro_produto * valor_primeiro_produto
faturamento_segundo = vendas_segundo_produto * valor_segundo_produto
faturamento_terceiro = vendas_terceiro_produto * valor_terceiro_produto
faturamento_total = faturamento_primeiro + faturamento_segundo + faturamento_terceiro

print(f"Você faturou um total de R${faturamento_total}. Sendo:")
print(f"R${faturamento_primeiro} do {primeiro_produto}; R${faturamento_segundo} do {segundo_produto} e R${faturamento_terceiro} do {terceiro_produto}.")
