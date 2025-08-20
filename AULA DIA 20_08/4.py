def distancia_pontos(x1, y1, x2, y2):
    x2_menos_x1 = x2 - x1
    y2_menos_y1 = y2 - y1
    
    soma = x2_menos_x1 ** 2 + y2_menos_y1 ** 2
    distancia = soma ** 0.5
    return distancia

x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))
resultado = distancia_pontos(x1, y1, x2, y2)
print(resultado)