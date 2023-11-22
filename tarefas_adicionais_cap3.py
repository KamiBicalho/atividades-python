termo = int(input("Digite o primeiro termo da P.A.: "))
razao = int(input("Digite a razão da P.A.: "))
termo_quantidade = int(input("Digite quantos termos terá a P.A.: ")) 

contador = 0
soma_termos = 0

while contador < termo_quantidade:
    print(f"O {contador + 1}º termo da PA é = {termo}")
    termo = termo + razao
    soma_termos = soma_termos + (termo - razao)
    contador = contador + 1

print(f"A soma de todos os termos é = {soma_termos}")
