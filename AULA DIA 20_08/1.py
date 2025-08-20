def decimal_para_binarios():
    numero = int(input("Digite um número inteiro positivo: "))

    if numero < 0:
        print("Número negativo não é permitido.")
        return
    binario = ""
    if numero == 0:
        binario = "0"
    else:
        while numero > 0:
            binario = str(numero % 2) + binario
            numero //= 2
    print(f"Binário: {binario}")
decimal_para_binarios()