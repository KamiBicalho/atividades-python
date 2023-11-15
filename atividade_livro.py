#questão 1
x = 0.0
y = 18
print(type(x))
print(type(y))
z = x + y
print(z)
print(type(z))

#questão 2
a = 10
print(a)
#print(A) >>> quando usamos a maíuscula, ocorre o erro (NameError: name 'A' is not defined. Did you mean: 'a'?) então Python é caseSensitive

#questão 3
A = 'Questão 3'
B = 25
C = 3.9
print(type(A))
print(type(B))
print(type(C))

#questão 4
a = 14
b = 5
adicao = a + b
subtracao = a - b
multiplicacao = a * b 
divisao = a / b 
divisao_inteira = a // b 
resto = a % b 
oposto = -a
potenciacao = a ** b
print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(resto)
print(oposto)
print(potenciacao)

#questão 5 (serviu de base para a questão 6)
base_triangulo = 9
altura_triangulo = 6
area_triangulo = base_triangulo * altura_triangulo / 2
print(f"A área do triângulo é {area_triangulo}.")

# #questão 6
# base_triangulo = float(input("Digite a base do triângulo: "))
# altura_triangulo = float(input("Digite a altura do triângulo: "))
# area_triangulo = base_triangulo * altura_triangulo / 2
# print(f"A área do triângulo é {area_triangulo}.")

#questão 7
valor_hora = 14.25
horas_normais_trabalhadas = 163
horas_extras_trabalhadas = 20
pagamento_horas_normais = valor_hora * horas_normais_trabalhadas
pagamento_horas_extras = valor_hora * 2 * horas_extras_trabalhadas
pagamento_total = pagamento_horas_normais + pagamento_horas_extras
print(f"O salário bruto do funcionário será de R${pagamento_total}.")