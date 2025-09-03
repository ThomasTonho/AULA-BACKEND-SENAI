class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10
    

class Gerente(Funcionario):
     def calcular_bonus(self):
        return self.salario * 0.20
     

nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

funcionario1 = Funcionario(nome, salario)
print(f"Bônus do {funcionario1} é o igual o valor de R$ {funcionario1.calcular_bonus():.2f}")
