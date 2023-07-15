menu = '''
****Bem vindo ao Caixa Eletrônico do Banco Dio!****
**********Selecione a operação desejada:***********
[1] - Depósitos
[2] - Saques
[3] - Extratos
[0] - Sair
***************************************************
IMPORTANTE: Os valores decimais devem ser indicados
com ponto, e não vírgula.
***************************************************
Nunca peça ajudas de estranhos, caso tenha dúvidas,
contate um de nossos ajudantes, devidamente identi-
ficados ou nossas centrais telefonicas.
***************************************************
Limite de Saque desse terminal R$ 500,00 por opera-
ção.
*********Este caixa trabalha com notas de**********
--- R$ 2 --- R$ 5 --- R$ 10 --- R$ 20 --- R$ 50 ---  
***************************************************
'''
saldo = 0
limite_saque_especie= 500
extrato = [] #aqui o professor sugere que seja 1uma string, mas coloquei uma lista, me parece mais funcional
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

#pro futuro, apresentr tudo isso numa tela em interfale com ascii, como eram os antigos ATM, usando "curses" ou "windows-curses"
 
while True:
    opcao = input(menu)
    
    if opcao == "1":
        #funcão deposito
        print("Função Depósito")
        valor_depositado = float(input("Favor digitar o valor a ser depositado:")) #aqui forçamos a entrada a ser float, pra representar os centavos
        if valor_depositado > 0: #consi=cional para impedir deposito negativo
            saldo += valor_depositado
            extrato.append({'tipo': 'depósito', 'valor': f'R1${valor_depositado:.2f}'}) #regista operação na varioiavel extrato para consulta posterior
            print("***************************************************")
            print(f'Depósito de R$ {valor_depositado:.2f} efetuado com sucesso!')
            print(f'O saldo atual é de R$ {saldo:.2f}')
            print("***************************************************")
        else:    
            print("***************************************************")
            print("Por favor, digite um valor de deposito válido")
            print("***************************************************") 
    elif opcao == "2":
        #funcão saque
        print("Função Saque.")
        valor_sacado = float(input("Favor digitar o valor a ser sacado:"))
        if valor_sacado <= 500 and valor_sacado > 0.1 and valor_sacado <= saldo and numero_saques <= LIMITE_NUMERO_SAQUES:
            saldo -= valor_sacado
            numero_saques += 1
            extrato.append({'tipo': 'saque', 'valor': f'R${valor_sacado:.2f}'}) #regista operação de saque, analogo a função anterior
            print("***************************************************")
            print(f'Saque de R$ {valor_sacado:.2f} efetuado com sucesso!')
            print(f'O saldo atual é de R$ {saldo:.2f}')
            print("***************************************************")
        elif numero_saques < LIMITE_NUMERO_SAQUES:
            print("***************************************************")
            print("Numero limite de saques diários excedido!")
            print("***************************************************")
        elif valor_sacado > 500:
            print("***************************************************")
            print("Valor máximo de saque excedido, tente novamente")
            print("***************************************************")
        elif valor_sacado > saldo:
            print("***************************************************")
            print("Não é possivel sacar dinheiro, saldo insuficiente!")
            print("***************************************************")
        elif valor_sacado <= 0:
            print("***************************************************")
            print("Não é possível sacar valor negativo ou igual a zero")
            print("***************************************************")
        else:
            print("***************************************************")
            print("Operação não permitida, verificar dados inseridos.") 
            print("***************************************************")   
    elif opcao == "3":
        #funcão extrato
        if extrato:
            print("***************************************************")
            print("Extrato:")
            print("***************************************************")
            for operacao in extrato:
                print(f'Tipo: {operacao["tipo"]}, Valor: {operacao["valor"]}')
                print("***************************************************")
        else:
            print("***************************************************")
            print("O extrato está vazio.")
            print("***************************************************")
    elif opcao == "0":
        print("***************************************************")
        print("***************************************************")
        print("***************************************************")
        print("Operação encerrada, obrigado por usar nossos caixas")
        print("Verifique também nosso internet banking: dio.com.br")
        print("***************************************************")
        print("***************************************************")
        print("***************************************************")
        break  
else:
    print("Opção inválida! Por favor,selecione corretamente a opção desejada:")