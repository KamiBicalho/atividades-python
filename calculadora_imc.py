def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade moderada"
    elif 35 <= imc < 39.9:
        return "Obesidade mórbida grave"
    else:
        return "Obesidade mórbida muito grave"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc_resultado = calcular_imc(peso, altura)
categoria_imc = classificar_imc(imc_resultado)

print(f"Seu IMC é {round(imc_resultado, 2)}, o que é classificado como '{categoria_imc}'.\n")


