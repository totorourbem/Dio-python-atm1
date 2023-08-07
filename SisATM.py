from datetime import datetime
import time #para inserir pausas nos textos longos

saldo = 0
limite_saque_especie= 500
extrato = [] #aqui o professor sugere que seja 1uma string, mas coloquei uma lista, me parece mais funcional
contas = []
cooperados = []
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3
AGENCIA = "0001"

def quadro_mensagem(mensagem):
    print("*" * 51)
    print(mensagem)
    print("*" * 51)
    time.sleep(0.5)
     
def mostrar_saldo():
    quadro_mensagem(f"  *          O saldo atual é de R$ {saldo:.2f}         *")
    quadro_mensagem(f"*O limite de valor para cada saque é de R$ {limite_saque_especie:.2f}*")
    quadro_mensagem(f"* O limite de operações de saques diários é de {LIMITE_NUMERO_SAQUES}! *")
    quadro_mensagem(f"*           Você já fez {numero_saques} saques hoje.            *")

def filtrar_cooperados(cpf, cooperados):
    cooperados_filtrados = [cooperado for cooperado in cooperados if cooperado["cpf"] == cpf] #cria uma lista e nela percorre cada cooperado na lista cooperados, verificando se achave cpf é gual ao cpf digitado
    return cooperados_filtrados[0] if cooperados_filtrados else None #se a lista filtrados não estiver vaiza, retorna oprimeiro dicionario, do contrartio, retorna "None"
    
def menu_inicial():
    
    quadro_mensagem("*   Bem vindo ao Caixa Eletrônico do Banco Dio!   *")
    quadro_mensagem("*          Selecione a Operação desejada          *")
    quadro_mensagem("[1] - Depósitos\n[2] - Saques\n[3] - Extratos\n[4] - Saldo em Tela\n[5] - Listar contas\n[6] - Cadastrar novo Cooperado\n[7] - Já é cooperado? Abra sua Conta\n[0] - Sair")
    quadro_mensagem("IMPORTANTE: Os valores decimais devem ser indicados\ncom ponto, e não vírgula.")
    quadro_mensagem("NUNCA peça ajudas de estranhos, caso tenha dúvidas,\ncontate um de nossos ajudantes, devidamente identi-\nficados ou nossas centrais telefonicas.")
    quadro_mensagem(f"Limite de Saque desse terminal {limite_saque_especie:.2f} por operação.")
    quadro_mensagem("*        Este caixa trabalha com notas de:        *")
    quadro_mensagem("--- R$ 2 --- R$ 5 --- R$ 10 --- R$ 20 --- R$ 50 ---")
    print("Operação nº→→")
    
def depositar(saldo, valor_depositado, extrato, /): #valores posicionais definidos, conforme desafio
    quadro_mensagem("Função Depósito")
    if valor_depositado > 0: #condiicional para impedir deposito negativo, o input saiu da função porque daria pau com os argumentos declarados
        saldo += valor_depositado
        data_hora_atual = datetime.now() #cria variável, com uma função que registra o exato tempo e data da operação
        extrato.append({
            "data": data_hora_atual.strftime("%d/%m/%Y"), # grava no valor a data, em formato de string conforme formatação em parenteses
            "hora": data_hora_atual.strftime("%H:%M"), # grava no valor a hora, em formato de string conforme formatação em parenteses  
            "tipo": "depósito", 
            "valor": f'R${valor_depositado:.2f}'}) #regista operação na variável extrato para consulta posterior
        time.sleep(1)
        quadro_mensagem("Operação realizada com sucesso")
    else:    
        quadro_mensagem("Por favor, digite um valor de deposito válido")
    return saldo, extrato

def sacar(*, saldo, valor_sacado, extrato, limite_saque_especie, numero_saques, LIMITE_NUMERO_SAQUES): #valores nomeados definidos, conforme desafio
    quadro_mensagem("Função Saque.")
    if numero_saques >= LIMITE_NUMERO_SAQUES:
        quadro_mensagem("Numero limite de saques diários excedido!")
    elif valor_sacado > 500:
        print("Valor máximo de saque excedido, tente novamente")
    elif valor_sacado > saldo:
        print("Não é possivel sacar dinheiro, saldo insuficiente!")
    elif valor_sacado <= 0:
        print("Não é possível sacar valor negativo ou igual a zero")
    elif valor_sacado > 0:
        saldo -= valor_sacado
        numero_saques += 1
        data_hora_atual = datetime.now()
        extrato.append({
            "data": data_hora_atual.strftime("%d/%m/%Y"), 
            "hora": data_hora_atual.strftime("%H:%M"),   
            "tipo": "saque", 
            "valor": f'R${valor_sacado:.2f}'}) 
        quadro_mensagem(f'Saque de R$ {valor_sacado:.2f} efetuado com sucesso!') 
    else: 
        print("Operação não permitida, verificar dados inseridos.") 
    mostrar_saldo()
    return saldo, extrato, numero_saques

def exibir_extrato (saldo, /, *, extrato):#valores posicionais e nomeados definidos, conforme desafio
    if extrato:
        quadro_mensagem("Extrato:")
        for operacao in extrato:
            quadro_mensagem((f'{operacao["data"]},-{operacao["hora"]}, Tipo: {operacao["tipo"]}, Valor: {operacao["valor"]}')) #Aqui o compilador exigiu o uso difernciado de aspas
    else:
        quadro_mensagem("O extrato está vazio")

def novo_cooperado(cooperados):
    cpf = int(input("Insira seu CPF, apenas numeros:")) #força o input a ser somente numero do CPF
    cooperado = filtrar_cooperados(cpf, cooperados)
    
    if cooperado:
        quadro_mensagem("*  Já existe um usuário com este CPF cadastrado!  *") #retorna erro caso já exista cadastro
        return
    
    nome = str(input("Informe o nome completo:")) #inserçao de dados, forçando formato correto
    data_nascimento = str(input("Informe a data de nascimento (dd-mm-aaaa):"))
    endereco = str(input("Informe o enderço completo:"))
    
    cooperados.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco}) #adição do usuário
    
    quadro_mensagem("*           Usuário criado com sucesso!           *")
       
def criar_conta(agencia, numero_conta, cooperados):
    cpf = int(input("Insira seu CPF, apenas numeros:")) 
    cooperado = filtrar_cooperados(cpf, cooperados) 
    
    if cooperado:
        quadro_mensagem("*             Conta criada com sucesso!           *") #Se cooperado já existir, cria conta
        return {"agencia":agencia, "numero_conta":numero_conta, "cooperado":cooperado}
    
    quadro_mensagem("Coooperado não encontrado, favor inserir o cadastro\nna opção 6 do menu inicial")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta["agencia"]}
        C/C: {conta["numero_conta"]}
        Titular: {conta["cooperado"]["nome"]}
        """
        quadro_mensagem(linha) 
        
while True:
    opcao = input(menu_inicial())   
     
    if opcao == "1":
        valor_depositado = float(input("Favor digitar o valor a ser depositado:")) #aqui chama a entraada de dados pra função, forçando o valor depositado a ser float, pra representar os centavos
        saldo, extrato  =  depositar(saldo, valor_depositado, extrato) #chama a função com os argumentos, para que se verifique o if dentro da função, e que cumpra a necessidade de argumentos da mesma
        time.sleep(0.5) #break pra legibilidade
    elif opcao == "2":
        valor_sacado = float(input("Favor digitar o valor a ser sacado:")) 
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques, valor_sacado=valor_sacado, limite_saque_especie=limite_saque_especie, LIMITE_NUMERO_SAQUES=LIMITE_NUMERO_SAQUES)#trecho condizclearente com cartateres nomeados, conforme desafio
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "4":
        mostrar_saldo()
    elif opcao == "5":
        listar_contas(contas)
    elif opcao == "6":
        novo_cooperado(cooperados)
    elif opcao == "7":
        numero_conta = len(contas) +1
        conta = criar_conta(AGENCIA, numero_conta, cooperados)
        
        if conta:
            contas.append(conta)
           
    elif opcao == "0":
        quadro_mensagem("Operação encerrada, obrigado por usar nossos caixas\nVerifique também nosso internet banking: dio.com.br")
        break  
    else:
        quadro_mensagem("Opção incorreta! Favor selecionar a opção desejada:")
    