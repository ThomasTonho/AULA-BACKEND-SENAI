contas = {}

def depositar_dinheiro():
    print("DEPÓSITO")
    
    try:
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor para depositar: RS "))
        
        if valor <= 0:
            print("O valor deve ser positivo!")
            return

        if numero_conta not in contas:
            contas[numero_conta] = 0
            print(f"Nova conta {numero_conta} criada!")

        contas[numero_conta] += valor
        
        print(f"Depósito realizado com sucesso!")
        print(f"Valor depositado: RS {valor:.2f}")
        print(f"Saldo atual: RS {contas[numero_conta]:.2f}")
        
    except ValueError:
        print("Digite valores válidoS!")

def sacar_dinheiro():
    print("SAQUE")
    
    try:
        numero_conta = int(input("Digite o número da conta: "))
        
        if numero_conta not in contas:
            print("Conta não encontrada!")
            return
        
        valor = float(input("Digite o valor para sacar: RS "))

        if valor <= 0:
            print("O valor deve ser positivo!")
            return
        
        if valor > contas[numero_conta]:
            print("Saldo insuficiente!")
            print(f"Saldo disponível: Rs {contas[numero_conta]:.2f}")
            return
        
        contas[numero_conta] -= valor
        
        print(f"Saque realizado com sucesso!")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo restante: R$ {contas[numero_conta]:.2f}")
        
    except ValueError:
        print("Digite valores válidos!")

def exibir_saldo():
    print("CONSULTAR SALDO")
    
    try:
        numero_conta = int(input("Digite o número da conta: "))
 
        if numero_conta not in contas:
            print("❌ Conta não encontrada!")
            return
        
        print(f"Saldo da conta {numero_conta}: R$ {contas[numero_conta]:.2f}")
        
    except ValueError:
        print("Digite um número válido!")

def sair_sistema():
    print("Saindo do sistema")
    print("Obrigado por usar nosso banco!")
    return True  # Retorna True para indicar que deve sair

def menu():
    print("="*30)
    print("1 - Depositar dinheiro")
    print("2 - Sacar dinheiro") 
    print("3 - Exibir saldo")
    print("4 - Sair do sistema")
    print("="*30)

def simulador_banco():
    
    while True:
        menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                depositar_dinheiro()
            
            elif opcao == 2:
                sacar_dinheiro()
            
            elif opcao == 3:
                exibir_saldo()
            
            elif opcao == 4:
                if sair_sistema():
                    break
            
            else:
                print("❌ Opção inválida! Escolha de 1 a 4.")
                
        except ValueError:
            print("❌ Digite apenas números!")
        
simulador_banco() 