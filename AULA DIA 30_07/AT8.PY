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

filme_escolhido = random.choice(filmes)
escolha = input("Digite um filme para jogar o jogo da FORCA")
print(filme_escolhido)