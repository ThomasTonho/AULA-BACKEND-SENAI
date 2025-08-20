def volume_cilindro():
    raio = float(input("Digite o raio da base do cilindro: "))
    altura = float(input("Digite a altura do cilindro: "))
    if raio < 0 or altura < 0:
        print("Raio e altura devem ser positivos.")
        return
    volume = 3.14 * (raio ** 2) * altura
    print(f"O volume do cilindro é: {volume}")
volume_cilindro()