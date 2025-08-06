num=int(input("Digite um numero: "))

for cont in range(2,num):
    if num%cont==0:
     print("Não é primo")
     break
    else:
     print("É primo")