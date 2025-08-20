def imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser positivos.")
        return
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
imc() 