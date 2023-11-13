salario_base1 = 2112.00
salario_base2 = 2826.65
salario_base3 = 3751.05
salario_base4 = 4664.68

salario_funcionario = input("Digite o seu salário: ")
salario_liquido = float(salario_funcionario)*0.89 #desconto base do INSS em 11%

if salario_liquido < salario_base1:
  print("Não tem desconto do IR.")
elif salario_liquido < salario_base2:
  calculo_imposto = salario_liquido * 0.075 - 158.40
  calculo_arredondado = round(calculo_imposto, 2)
  print(f"O desconto do IR vai ser de R${calculo_arredondado}")
elif salario_liquido < salario_base3:
  calculo_imposto = salario_liquido * 0.15 - 370.4
  calculo_arredondado = round(calculo_imposto, 2)
  print(f"O desconto do IR vai ser de R${calculo_arredondado}")
elif salario_liquido < salario_base4:
  calculo_imposto = salario_liquido * 0.225 - 651.73
  calculo_arredondado = round(calculo_imposto, 2)
  print(f"O desconto do IR vai ser de R${calculo_arredondado}")
else:
  calculo_imposto = salario_liquido * 0.275 - 884.96
  calculo_arredondado = round(calculo_imposto, 2)
  print(f"O desconto do IR vai ser de R${calculo_arredondado}")
