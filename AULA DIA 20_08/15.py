import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 10
    min_intervalo = 1
    max_intervalo = 100
    
    print("Tente adivinhar o número entre 1 e 100.")
    
    for tentativa in range(1, tentativas + 1):
        print(f"\nTentativa {tentativa} de {tentativas}.")
        print(f"Dica: O número está entre {min_intervalo} e {max_intervalo}.")
        palpite = int(input("Digite seu palpite: "))
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativa} tentativas.")
            return
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
            if palpite >= min_intervalo:
                min_intervalo = palpite + 1
        else:
            print("O número secreto é menor.")
            if palpite <= max_intervalo:
                max_intervalo = palpite - 1
    
    print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")
jogar_adivinhacao()