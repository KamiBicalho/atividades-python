# questão 4
numero = int(input("Digite um número inteiro:"))

if numero < 0:
    print("Este número é negativo.")
elif numero == 0:
    print("Você digitou o Zero.")
else:
    print("Este número é positivo.")


#questão 5
resto_divisao = numero % 2

if resto_divisao == 0:
    print("Você digitou um número par.")
else:
    print("Você digitou um número ímpar.")


# questão 6
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
elif numero1 < numero2:
    print(f"O número {numero2} é maior que o número {numero1}")
else: 
    print("Os números são iguais.")


# questão 7
lado1 = float(input("Insira o primeiro lado:"))
lado2 = float(input("Insira o segundo lado:"))
lado3 = float(input("Insira o terceiro lado:"))

verificacao1 = (lado1 + lado2) > lado3
verificacao2 = (lado2 + lado3) > lado1
verificacao3 = (lado1 + lado3) > lado2

if verificacao1 and verificacao2 and verificacao3:
    print(f"É possível construir um triângulo com os lados {lado1}, {lado2} e {lado3}")

    if lado1 == lado2 and lado1 == lado3:
        print("O triângulo é equilátero")
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 != lado2 and lado1 == lado3) or (lado3 == lado2 and lado1 != lado3):
        print("O triângulo é isóceles")
    else:
        print("O triângulo é escaleno")

else:
    print(f"Não é possível construir um triângulo com os lados {lado1}, {lado2} e {lado3}")


# questão 8
nome_lutador = input("Nome do lutador:")
peso_lutador = float(input("Peso do lutador:"))
categoria = ""

if peso_lutador < 65:
    categoria = "Pena"
elif peso_lutador < 72:
    categoria = "Leve"
elif peso_lutador < 79:
    categoria = "Ligeiro"
elif peso_lutador < 86:
    categoria = "Meio-médio"
elif peso_lutador < 93:
    categoria = "Médio"
elif peso_lutador < 100:
    categoria = "Meio-pesado"
else:
    categoria = "Pesado"

print(f"O lutador {nome_lutador} pesa {peso_lutador}kg e se enquadra na categoria {categoria}.")


# questão 9 (questão 7 do capítulo anterior)


# questão 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1


# questão 11
numero_dado = int(input("Escreva um número inteiro positivo:"))
contador = 1

while contador <= 10:
    resultado = numero_dado * contador
    print(f"{numero_dado} x {contador} = {resultado}")
    contador += 1


# questão 12
quantos_somar = int(input("Quantos números você quer somar? "))

contador = 0
soma_positiva = 0

while contador < quantos_somar:
    numero_dado = int(input(f"{contador + 1}º numero: "))
    if numero_dado < 0:
        contador += 1
        continue
    soma_positiva = soma_positiva + numero_dado
    contador += 1

print(f"A soma dos positivos deu {soma_positiva}.")


#questão 13
print("Lembre-se: o ZERO faz a calculadora parar.")
numero_digitado = int(input("Digite um número inteiro:"))
soma_positiva = 0
soma_negativa = 0
contador = 0

while numero_digitado != 0:
    if numero_digitado > 0:
        soma_positiva += numero_digitado
        numero_digitado = int(input("Digite um número inteiro:"))
    else:
        soma_negativa += numero_digitado
        numero_digitado = int(input("Digite um número inteiro:"))
    contador += 1

print(f"Você somou {contador} números, os positivos deram {soma_positiva} e os negativos deram {soma_negativa}.")


# questão 14 
primeiro_termo = int(input("Primeiro termo da PG: "))
razao = int(input("Razão da PG: "))
termo = int(input("Número de termos: "))
soma_termos = 0

contador = 0

while contador < termo:
    proximo_termo = primeiro_termo * razao ** contador
    print(f"O {contador + 1}º termo é {proximo_termo}.")
    soma_termos += proximo_termo
    contador += 1

print(f"A soma dos {termo} primeiros termos da PG é {soma_termos}.")


