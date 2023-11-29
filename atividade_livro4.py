# #questão 1
# contador = 1
# lista = []
# for x in range(10):
#     numero = int(input(f"Digite o {contador}º número: "))
#     lista.append(numero)
#     contador += 1

# lista.reverse()

# print(f"Os valores foram {lista}")

# #questão 2 
# lista1 = []
# lista2 = []
# contador1 = 0
# contador2 = 0

# for x in range(10):
#     numero = int(input(f"Digite o {contador1}º número da lista 1: "))
#     lista1.append(numero)
#     contador1 += 1

# print(lista1)

# for x in range(10):
#     numero = int(input(f"Digite o {contador2}º número da lista 1: "))
#     lista2.append(numero)
#     contador1 += 1

# print(lista2)

# listas_juntas = lista1 + lista2
# print(f"/n Juntas ficam: {listas_juntas}")

#questão 3
# lista1 = []
# lista2 = []
# contador1 = 0
# contador2 = 0

# for x in range(5):
#     numero = int(input(f"Digite o {contador1}º número da lista 1: "))
#     lista1.append(numero)
#     contador1 += 1

# print(lista1)

# for x in range(7):
#     numero = int(input(f"Digite o {contador2}º número da lista 1: "))
#     lista2.append(numero)
#     contador1 += 1

# print(lista2)

# listas_juntas = lista1 + lista2
# print(f"/n Juntas ficam: {listas_juntas}")

# #questão 4
# tamanho_lista = int(input("Digite o tamanho da lista: "))
# lista = []

# for x in range(tamanho_lista):
#     numero = int(input(f"Digite o {x + 1}º número da lista: "))
#     while lista.count(numero) != 0:
#         print("Este número já foi digitado.")
#         numero = int(input("Digite outro: "))
#     lista.append(numero)

# print(lista)

# #questão 5
# quantidade_lista1 = int(input("Digite o tamanho da 1ª lista: "))
# lista1 = []
# lista2 = []
# lista_juntas = lista1

# for x in range(quantidade_lista1):
#     numero = int(input(f"Digite o {x + 1}º número da lista 1: "))
#     while lista1.count(numero) != 0:
#         print("Este número já foi digitado.")
#         numero = int(input("Digite outro: "))
#     lista1.append(numero)
# print(lista1)

# quantidade_lista2 = int(input("Digite o tamanho da 2ª lista: "))
# for x in range(quantidade_lista2):
#     numero = int(input(f"Digite o {x + 1}º número da lista 2: "))
#     while lista2.count(numero) != 0:
#         print("Este número já foi digitado.")
#         numero = int(input("Digite outro: "))
#     lista2.append(numero)
#     if lista1.count(numero) == 0:
#         lista_juntas.append(numero)
# print(lista2)

# print(lista_juntas)

# #questão 6
# primeiro_termo = int(input("Digite o primeiro termo: "))
# razao = int(input("Digite a razão: "))
# numero_termos = int(input("Digite a quantidade de termos: "))
# termo_geral = primeiro_termo + razao * (numero_termos - 1)

# termos_pa = list(range(primeiro_termo, (termo_geral + 1), razao))

# print(termos_pa)

# #questão 7
# tamanho_lista = int(input("Digite um número entre 0 e 50: "))
# contador_positivo = 0
# contador_negativo = 0
# lista_positiva = []
# lista_negativa = []

# while tamanho_lista < 0 or tamanho_lista >50:
#     print("Número inválido.")
#     tamanho_lista = int(input("Digite um número entre 0 e 50: "))

# for x in range(tamanho_lista):
#     dado_numero = float(input(f"Digite o número:"))
#     if dado_numero < 0:
#         lista_negativa.append(dado_numero)
#         contador_negativo += 1
#     else:
#         lista_positiva.append(dado_numero)
#         contador_positivo += 1

# print(f'Você digitou {contador_positivo} números positivos:')
# print(lista_positiva)
# print(f'Você digitou {contador_negativo} números negativos:')
# print(lista_negativa)

