
numero = int(input("Digite um número: "))

if numero < 0:
    print("Nenhum número positivo foi digitado.")
else:
    maior = numero
    while True:
        numero = int(input("Digite um número: "))
        if numero < 0:
            break
        if numero > maior:
            maior = numero
    print(f"O maior número digitado foi: {maior}")
