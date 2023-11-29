# O cliente que fabrica peças automotivas requisitou uma nova funcionalidade para o sistema: 
# calcular o total de vendas. Como seus negócios estão expandindo, o cliente solicitou que o sistema seja capaz de receber valores em reais, dolár ou euro, 
# e que seja feita a conversão para o valor em reais.

# o valor do produto (obrigatório).
# a quantidade do produto (obrigatório).
# a moeda em que deve ser feito o cálculo (obrigatório, sendo padrão o real).
# a porcentagem do desconto que será concedida na compra (opcional).
# a porcentagem de acréscimo, que depende da forma de pagamento (opcional).
   
valor_produto = float(input("Digite o valor do produto: "))
quantidade_produto = int(input("Quantos produtos foram vendidos? "))
moeda = input("Digite se o valor está em real, euro ou dolar: ")
lista_moedas = ["euro", "real", "dolar"]

while lista_moedas.count(moeda) == 0:
    moeda = input("Não reconhecido. Digite novamente o valor está em real, euro ou dolar: ")

desconto = float(input("Digite a % do desconto: "))
aumento = float(input("Digite a % do aumento: "))

def valor_total(valor_produto, quantidade_produto, moeda, desconto_aumento):
    if moeda == "euro":
        valor_produto = valor_produto * 5.7
    elif moeda == "dolar":
        valor_produto = valor_produto * 5
    
    if desconto_aumento > 0:
        return valor_produto * quantidade_produto * desconto_aumento
    else:
        print("Não é possível calcular total da venda.")


def desconto_aumento(desconto = 0, aumento = 0):
    if desconto >= 0 and aumento == 0:
        return 1 - (desconto / 100)
    elif aumento > 0 and desconto == 0:
        return 1 + (aumento / 100)
    else:
        print("Não é possível aplicar desconto e aumento simultaneamente.")

print(valor_total(valor_produto, quantidade_produto, moeda, desconto_aumento(desconto, aumento)))
    


# SUGESTÃO DO AUTOR:

# def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
#     v_bruto = valor_prod * qtde
    
#     if desconto:
#         v_liquido = v_bruto - (v_bruto * (desconto / 100))
#     elif acrescimo:
#         v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
#     else:
#         v_liquido = v_bruto
    
#     if moeda == 'real':
#         return v_liquido
#     elif moeda == 'dolar':
#         return v_liquido * 5
#     elif moeda == 'euro':
#         return v_liquido * 5.7
#     else:
#         print("Moeda não cadastrada!")
#         return 0
    
# valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
# print(f"O valor final da conta é {valor_a_pagar}")