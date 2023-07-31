LIMITE_DE_SAQUES_DIARIOS = 3
VALOR_LIMITE_DE_SAQUE = 500
saldo = 0
extrato = ''

menu = """
===============SISTEMA BANCÁRIO DIO================
Escolha uma opção:
1 - Saque
2 - Depósito
3 - Extrato
0 - Sair
:"""
while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Insira o valor que deseja sacar: "))
        if valor <= saldo:
            saldo -= valor
            extrato += f"R$ {valor}. Saldo {saldo}\n"
            print("A operação foi realizada com sucesso")
        else:
            print("Saldo insuficiente!")