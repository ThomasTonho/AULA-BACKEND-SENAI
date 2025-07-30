escolha = int(input("Digite um número: "))

for i in range(1, escolha + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Senai")
    elif i % 3 == 0:
        print("Super")
    elif i % 5 == 0:
        print("Lógica")
    else:
        print(i)
