def raio_circulo():
    raio = float(input("Digite o raio do círculo: "))
    if raio < 0:
        print("Raio não pode ser negativo.")
        return
    area = 3.14159 * (raio ** 2)
    print(f"A área do círculo é: {area}")

raio_circulo()