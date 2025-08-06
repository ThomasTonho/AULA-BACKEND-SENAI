numero = int(input("Digite um número: "))

if numero == 0:
    binario = '0'
else:
    binario = ''
    n = numero
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2

print(f" {numero} é {binario} em binario")
