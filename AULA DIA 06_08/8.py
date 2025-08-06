notas = []

while True:
    nota = float(input("Digite uma nota: "))
    if nota == -1:
        break
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(media)