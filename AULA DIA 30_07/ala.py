import random

filmes = [
    "Demon Slayer: Trem Infinito",
    "Doutor Estranho no Multiverso da Loucura",
    "Guardiões da Galáxia",
    "Harry Potter e a Pedra Filosofal",
    "Homem-Aranha: Através do Aranhaverso",
    "Homem-Aranha: Sem Volta para Casa",
    "Luca",
    "Monstros S.A.",
    "O Batman",
    "Pantera Negra",
    "Soul",
    "Velozes e Furiosos 9",
    "Venom",
    "Vingadores: Ultimato",
    "Viúva Negra"
]

filme = random.choice(filmes).lower()
letras_adivinhadas = set()
tentativas = 7

print("Bem-vindo ao Jogo da Forca - Filmes!")
print(f"Você tem {tentativas} tentativas para adivinhar o filme.")

while tentativas > 0:
    # Mostrar o filme com letras descobertas e "_" para as não descobertas
    exibicao = ""
    for c in filme:
        if c.isalpha():
            if c in letras_adivinhadas:
                exibicao += c
            else:
                exibicao += "_"
        else:
            exibicao += c  # mostra espaços, pontuação e números
    print("\n" + exibicao)

    # Verificar se o jogador já ganhou
    if "_" not in exibicao:
        print("\nParabéns! Você adivinhou o filme:", filme)
        break

    palpite = input("Digite uma letra: ").lower()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue

    if palpite in letras_adivinhadas:
        print("Você já tentou essa letra:", palpite)
        continue

    letras_adivinhadas.add(palpite)

    if palpite in filme:
        print("Boa! A letra está no filme.")
    else:
        tentativas -= 1
        print(f"Letra errada! Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("\nSuas tentativas acabaram! O filme era:", filme)
