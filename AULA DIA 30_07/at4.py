nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceiro nota: "))
nota4 = int(input("Digite a quarta nota: "))
nota5 = int(input("Digite a quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if media >= 5:
    print("APROVADO")
elif media > 2.5 and media < 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
