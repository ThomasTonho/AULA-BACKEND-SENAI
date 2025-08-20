import random

def gerar_numeros_aleatorios():
    N = int(input("Digite um numero: "))
    M = int(input("Digite um numero: "))

    if N > M:
        N, M = M, N
 
    numero = random.randint(N, M)
    print("Número aleatório gerado entre", N, "e", M, "é", numero)
    return numero
gerar_numeros_aleatorios()