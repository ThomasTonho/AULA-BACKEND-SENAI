def hipotenusa(cateto1, cateto2):
    quadrado1 = cateto1 ** 2
    quadrado2 = cateto2 ** 2
    soma = quadrado1 + quadrado2
    raiz = soma ** 0.5
    return raiz

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))
resultado = hipotenusa(cateto1, cateto2)
print(f"A hipotenusa é: {resultado:.2f}")
