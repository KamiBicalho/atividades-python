# Cálculo base para desconto do INSS 2023 no regime de CLT 

salario_inicial1 = 1320
salario_inicial2 = 2571.29
salario_inicial3 = 3856.94
salario_inicial4 = 7507.49

aliquota_inss1 = 7.5 / 100
aliquota_inss2 = 9 / 100
aliquota_inss3 = 12 / 100
aliquota_inss4 = 14 / 100

taxa_aliquota_inss1 = salario_inicial1 * aliquota_inss1
taxa_aliquota_inss2 = (salario_inicial2 - salario_inicial1) * aliquota_inss2
taxa_aliquota_inss3 = (salario_inicial3 - salario_inicial2) * aliquota_inss3
taxa_aliquota_inss4 = (salario_inicial4 - salario_inicial3) * aliquota_inss4
taxa_teto_inss = taxa_aliquota_inss1 + taxa_aliquota_inss2 + taxa_aliquota_inss3 + taxa_aliquota_inss4

salario_funcionario = float(input("Digite o seu salário: "))
salario_descontado_inss = 0
desconto_salario_inss = 0

if salario_funcionario <= salario_inicial1:
  desconto_salario_inss = salario_funcionario * aliquota_inss1
  salario_descontado_inss = salario_funcionario - desconto_salario_inss
elif salario_funcionario <= salario_inicial2:
  desconto_salario_inss = taxa_aliquota_inss1 + (salario_funcionario - salario_inicial1) * aliquota_inss2
  salario_descontado_inss = salario_funcionario - desconto_salario_inss
elif salario_funcionario <= salario_inicial3:
  desconto_salario_inss = taxa_aliquota_inss1 + taxa_aliquota_inss2 + (salario_funcionario - salario_inicial2) * aliquota_inss3
  salario_descontado_inss = salario_funcionario - desconto_salario_inss
elif salario_funcionario < salario_inicial4:
  desconto_salario_inss = taxa_aliquota_inss1 + taxa_aliquota_inss2 + taxa_aliquota_inss3 + (salario_funcionario - salario_inicial3) * aliquota_inss4
  salario_descontado_inss = salario_funcionario - desconto_salario_inss
else:
  desconto_salario_inss = taxa_teto_inss
  salario_descontado_inss = salario_funcionario - desconto_salario_inss

salario_descontado_inss = round(salario_descontado_inss, 2)

print(f"O desconto do seu INSS foi de R${round(desconto_salario_inss, 2)}")


# Cálculo base para desconto do Importo de Renda 2023 no regime de CLT 

salario_base_descontado1 = 2112.00
salario_base_descontado2 = 2826.65
salario_base_descontado3 = 3751.05
salario_base_descontado4 = 4664.68

calculo_imposto = 0

if salario_descontado_inss < salario_base_descontado1:
  print("Você está isento do Imposto de Renda")
elif salario_descontado_inss < salario_base_descontado2:
  calculo_imposto = salario_descontado_inss * 0.075 - 158.40
elif salario_descontado_inss < salario_base_descontado3:
  calculo_imposto = salario_descontado_inss * 0.15 - 370.4
elif salario_descontado_inss < salario_base_descontado4:
  calculo_imposto = salario_descontado_inss * 0.225 - 651.73
else:
  calculo_imposto = salario_descontado_inss * 0.275 - 884.96

print(f"O desconto do IR vai ser de R${round(calculo_imposto, 2)}")

salario_liquido = salario_funcionario - desconto_salario_inss - calculo_imposto

print(f"Seu salário líquido será de R${round(salario_liquido, 2)}")