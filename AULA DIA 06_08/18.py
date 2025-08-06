escolha = int(input("Digite o valor: "))

nota_100 = escolha // 100
resto = escolha % 100
nota_50 = resto // 50
resto = resto % 50
nota_20 = resto // 20
nota_10 = resto // 10
resto = resto % 10
nota_5 = resto // 5
resto = resto % 5
nota_2 = resto // 2
resto = resto % 2


print(f"Cédulas de R$100: {nota_100}")
print(f"Cédulas de R$50: {nota_50}")
print(f"Cédulas de R$20: {nota_20}")
print(f"Cédulas de R$10: {nota_10}")
print(f"Cédulas de R$5: {nota_5}")
print(f"Cédulas de R$2: {nota_2}")
print(f"Cédulas de R$1: {resto}")
