import random

tentativas = 6
letras_certas = []
letras_erradas = []

filmes = [
    "Demon Slayer Trem Infinito",
    "Doutor Estranho no Multiverso da Loucura",
    "Guardioes da Galaxia",
    "Harry Potter e a Pedra Filosofal",
    "Homem Aranha Através do Aranhaverso",
    "Homem Aranha Sem Volta para Casa",
    "Luca",
    "Monstros SA",
    "O Batman",
    "Pantera Negra",
    "Soul",
    "Velozes e Furiosos",
    "Venom",
    "Vingadores Ultimato",
    "Viuva Negra"
]

filme_escolhido = random.choice(filmes).upper()

while True:
    palavra = ""
    for letra in filme_escolhido:
        if letra in letras_certas:
            palavra += letra
        else:
            palavra += "_"

    print("Filme:", palavra)
    print("Erradas:", letras_erradas)
    print("Tentativas restantes:", tentativas)

    if "_" not in palavra:
        print("Parabéns! Você acertou o filme!")
        break
    if tentativas == 0:
        print("Você perdeu! O filme era:", filme_escolhido)
        break

    chute = input("Digite uma letra: ").upper()
    if len(chute) != 1 or not chute or chute in letras_certas or chute in letras_erradas:
        continue

    if chute in filme_escolhido:
        letras_certas.append(chute)
    else:
        letras_erradas.append(chute)
        tentativas -= 1
        