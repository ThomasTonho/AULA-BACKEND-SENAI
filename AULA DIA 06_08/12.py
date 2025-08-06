import random

numero_secreto = random.randint(1, 100)
tentativa = 0

while True:
    chute = int(input("Adivinhe o número (1 a 100): "))
    tentativa += 1

    if chute < numero_secreto:
        print("Maior!")
    elif chute > numero_secreto:
        print("Menor!")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas.")
        break
