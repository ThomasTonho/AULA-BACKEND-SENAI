def area_quadrado():
    lado = float(input("Digite o lado do quadrado: "))
    if lado < 0:
        print("Lado não pode ser negativo.")
        return
    area = lado ** 2
    print(f"A área do quadrado é: {area}")
area_quadrado()