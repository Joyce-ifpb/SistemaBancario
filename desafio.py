menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if(opcao == "d"):
        valor = float(input("Informe o valor do depósito: "))

        if(valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro. O valor informado é inválido.")
    
    elif(opcao == "s"):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUE

        if(excedeu_saldo):
            print("Erro. Você não possui saldo suficiente")
        elif(excedeu_limite):
            print("Erro. O valor do saque excedeu o limite")
        elif(excedeu_saque):
            print("Erro. Número máximo de saques excedido")
        elif(valor > 0):
            saldo -= valor
            extrato += f"Saque: R% {valor:.2f}\n"
        else:
            print("Erro. O valor informado é inválido.")

    elif(opcao == "e"):
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=============================================")

    elif(opcao == "q"):
        break

    else:
        print("Opção inválida, selecione a operação desejada corretamente.")
