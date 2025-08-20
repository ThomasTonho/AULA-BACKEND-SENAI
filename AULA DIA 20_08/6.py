def numero_digitos():
    numero = input("Digite um número inteiro: ")
    if not numero.isdigit():
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")
        return
    print(f"O número {numero} tem {len(numero)} dígitos.")
numero_digitos()