import random
import pyttsx3
from pyfiglet import figlet_format
import msvcrt
import time

class Bingo:
    def __init__(self):
        pass
    
    # Sorteia e retorne uma letra entre ('B','I','N','G','O')
    def sortear_letra(self):
        return random.choice(['B', 'I', 'N', 'G', 'O'])

    # Dado uma letra sortear e retornar um numero possivel
    # ou seja
    # Se for B: Um numero entre  1 e 15
    # Se for I: Um numero entre 16 e 30
    # Se for N: Um numero entre 31 e 45
    # Se for G: Um numero entre 46 e 60
    # Se for O: Um numero entre 61 e 75
    def sortear_numero(self, letra):
        if letra == 'B':
            return random.randint(1, 15)
        elif letra == 'I':
            return random.randint(16, 30)
        elif letra == 'N':
            return random.randint(31, 45)
        elif letra == 'G':
            return random.randint(46, 60)
        elif letra == 'O':
            return random.randint(61, 75)
        else:
            return None
    

    # Utilizando das funçoes de sortear letra e sortear numero
    # Realizar o sorteio da letra e numero e retornar
    # Exemplo B14
    def sorteio(self):
        letra = self.sortear_letra()
        numero = self.sortear_numero(letra)
        return f"{letra}{numero}"

    # Se necessario pode criar outras funções auxiliares

    def jogar(self):
        print(figlet_format("BINGO", font="standard"))
        while True:
            print("Sorteando em 3")
            time.sleep(1)
            print("Sorteando em 2")
            time.sleep(1)
            print("Sorteando em 1")
            time.sleep(1)
            sorteio = self.sorteio()
            self.falar(sorteio)
            time.sleep(3)
            print(sorteio)
            msvcrt.getch()

    # Nao mexer nessas abaixo
    def falar(self, texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()


bingo = Bingo()
bingo.jogar()