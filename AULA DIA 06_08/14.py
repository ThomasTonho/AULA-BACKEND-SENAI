a, b = 0, 1

n = int(input("Digite um numero: "))

print("Sequência de Fibonacci:")
for _ in range(n):
    print(a)
    a, b = b, a + b
