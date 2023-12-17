#CRIANDO SISTEMA BANCÁRIO COM PYTHON

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))


        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}∖n"

        else:
            print("Operação falhou! O valor informado é inválido.")

        
    elif opcao  == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= limite_saques


        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            