# questão 15
primeiro_numero = int(input("Forneça um número para o início do intervalo: "))
segundo_numero = int(input("Forneça um número para o fim do intervalo: "))
min_intervalo = primeiro_numero
max_intervalo = segundo_numero

while primeiro_numero == segundo_numero:
    segundo_numero = int(input("Forneça outro número para o fim do intervalo: "))
    if primeiro_numero != segundo_numero:
        max_intervalo = segundo_numero
        break

if primeiro_numero > segundo_numero:
    print("O valor inicial é menor que o final. Será considerado o inverso.")
    min_intervalo = segundo_numero
    max_intervalo = primeiro_numero

while min_intervalo <= max_intervalo:
    if min_intervalo % 5 != 0:
        min_intervalo += 1
        continue
    print(min_intervalo)
    min_intervalo += 1


# questão 16
quantidade = int(input("Quantos números você vai digitar? "))
contador = 1

if quantidade <= 1: 
    print("Quantidade de números invalida para avaliação")
else:
    numero = float(input("Digite o 1º número: "))
    menor_numero = numero
    maior_numero = numero
    while contador < quantidade:
        proximo_numero = float(input(f"Digite o {contador + 1}º número: "))
        if proximo_numero < menor_numero:
            menor_numero = proximo_numero
        elif proximo_numero > maior_numero:
            maior_numero = proximo_numero
        contador += 1
    if maior_numero == menor_numero:
        print("Você digitou tudo igual. Não tem maior e menor")
    else:
        print(f"""Você digitou {contador} números. O menor deles é o 
              {menor_numero} e o maior deles é o {maior_numero}""")


# questão 17
quantidade = int(input("Quantos números você vai digitar? "))
contador = 1
contador_positivos = 0

if quantidade <= 1: 
    print("Quantidade de números invalida para avaliação")
else:
    numero = float(input("Digite o 1º número: "))
    if numero >= 0:
        menor_numero = numero
        maior_numero = numero
        contador_positivos +=1
        while contador < quantidade:
            proximo_numero = float(input(f"Digite o {contador + 1}º número: "))
            if proximo_numero >= 0:
                if proximo_numero < menor_numero:
                    menor_numero = proximo_numero
                elif proximo_numero > maior_numero:
                    maior_numero = proximo_numero
                contador_positivos += 1
            contador += 1
        if maior_numero == menor_numero:
            print("Você digitou tudo igual. Não tem maior e menor")
        else:
            print(f"Você digitou {contador} números positivos. O menor deles é o {menor_numero} e o maior deles é o {maior_numero}")
    else:
        while contador < quantidade:
            proximo_numero = float(input(f"Digite o {contador + 1}º número: "))
            menor_numero = proximo_numero
            maior_numero = proximo_numero
            if proximo_numero >= 0:
                if proximo_numero < menor_numero:
                    menor_numero = proximo_numero
                elif proximo_numero > maior_numero:
                    maior_numero = proximo_numero
                contador_positivos += 1
            contador += 1
        if maior_numero == menor_numero:
            print("Nao é possível encontrar o máximo ou mínimo.")
        else:
            print(f"Você digitou {contador_positivos} números positivos. O menor deles é o {menor_numero} e o maior deles é o {maior_numero}")

# questão 18 
print("Para sair use um inteiro menor ou igual a ZERO.")
numero_digitado = int(input("Digite o número:"))

if numero_digitado <= 0:
    print("Você saiu da operação!")
else: 
    numero_maximo = numero_digitado
    numero_minimo = numero_digitado
    soma_numeros = numero_digitado
    while numero_digitado > 0:
        numero_digitado = int(input("Digite o número: "))
        if numero_digitado > 0:
            if numero_digitado < numero_minimo:
                numero_minimo = numero_digitado
            elif numero_digitado > numero_maximo:
                numero_maximo = numero_digitado
            soma_numeros += numero_digitado
    print(f"A soma dos números é {soma_numeros}.")
    print(f"O menor número foi {numero_minimo}.")
    print(f"O maior número foi {numero_maximo}.")
