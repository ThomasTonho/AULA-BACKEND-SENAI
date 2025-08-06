lista_numeros = []

for i in range(5):
    numeros = int(input(f"Digite o {i + 1} numero: "))
    lista_numeros.append(numeros)
    
print(f"Numero maior {max(lista_numeros)}")
print(f"Numero menor {min(lista_numeros)}")