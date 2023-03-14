menu = """
=========== Digite sua Opção ===========

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

========================================
=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input('Informe o valor do depósito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Indevida - Valor inválido")

    elif opcao == "2":
        valor = float(input('Informe o valor do saque: R$ '))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação - SALDO INSUFICIENTE")

        elif excedeu_limite:
            print("Falha na operação - VALOR ACIMA DO LIMITE")

        elif excedeu_saques:
            print("Falha na operação - SAQUES DIÁRIOS EXCEDIDOS")
        
        if valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques =+ 1

        else:
         print("Operação indevida - valor inválido ")

    elif opcao == "3":
        print("\n==================EXTRATO=================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('============================================')

    elif opcao == "4":
        break

    else:
        print("Operação Inválida, selecione novamente a operação desejada.")





