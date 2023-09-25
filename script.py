import subprocess

# Opção do menu que você deseja testar (substitua pelo número desejado)
opcao = "1"

# Entrada para o script
entrada = """6
12345678900
José das Couves
01-01-2000
Rua A nº 10 - COHAB nova
7
12345678900
5
1
5000
2
600
2
500
2
-100
3
0
"""

opcao = "6"

# Caminho para o seu script principal
script_principal = "/home/shisuii/Dio-python-atm1/app.py"  

# Comando para executar o script com a entrada específica
comando = ["python", script_principal]

# Execute o script com a entrada fornecida
process = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
saida, erro = process.communicate(input=entrada)

# Verifique se houve algum erro durante a execução
if erro:
    print("Erro durante a execução:")
    print(erro)