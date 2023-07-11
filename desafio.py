from os import system
from datetime import datetime

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nO valor de R$ {valor:.2f} foi sacado de sua conta.")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nO valor de R$ {valor:.2f} foi depositado em sua conta.")

    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibe_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return

def cria_usuario():
    
    system('cls')
    print("-=-=-=-=-=-=-=- CRIAÇÃO DE USUÁRIO -=-=-=-=-=-=-=-")

    cpf = input("\nDigite seu CPF (somente os números)\n=> ")

    if cpf == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None

    if len(cpf) != 11:
        print("\nO CPF deve possuir 11 digitos. Confira o CPF digitado. Criação de usuário cancelada.")
        return None

    try:
        cpf = int(cpf)
    except ValueError:
        print("\nVocê digitou algum caractere inválido. Digite apenas os números do CPF. Criação de usuário cancelada.")
        return None
    except Exception as e:
        print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o problema gerado abaixo.\n")
        print("Erro:", e.__class__, e)
        print("\nCriação de usuário cancelada.")
        return None

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("\nCPF já cadastrado no sistema. Criação de usuário cancelada.")
            return None

    nome = input("\nDigite seu nome completo\n=> ").upper()

    if nome == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None
    
    data_de_nascimento = input("\nInsira sua data de nascimento (Formato: dd/mm/YYYY)\n=> ")

    if data_de_nascimento == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None

    try:
        datetime.strptime(data_de_nascimento, "%d/%m/%Y")
    except ValueError:
        print("\nVocê digitou a data num formato inválido. Por favor, digite no formato \"dd/mm/YYYY\". Criação de usuário cancelada.")
        return None
    except Exception as e:
        print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o problema gerado abaixo.\n")
        print("Erro:", e.__class__, e)
        print("\nCriação de usuário cancelada.")
        return None

    logradouro = input("\nDigite seu logradouro\n=> ").upper()

    if logradouro == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None
    
    nro = input("\nDigite o número de sua residência\n=> ")

    if nro == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None

    try:
        nro = int(nro)
    except ValueError:
        print("\nVocê digitou algum caractere inválido. Digite apenas o número de sua residência (Ex: 153). Criação de usuário cancelada.")
        return None
    except Exception as e:
        print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o problema gerado abaixo.\n")
        print("Erro:", e.__class__, e)
        print("\nCriação de usuário cancelada.")
        return None
    
    bairro = input("\nDigite o seu bairro\n=> ").upper()

    if bairro == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None
    
    cidade = input("\nDigite a sua cidade\n=> ").upper()

    if cidade == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None
    
    sigla_estado = input("\nDigite a sigla do seu estado\n=> ").upper()

    if sigla_estado == "":
        print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
        return None
    
    if len(sigla_estado) != 2:
        print("\nAs siglas dos estados brasileiros são compostos por duas letras. Verifique a sigla digitada. Criação de usuário cancelada.")
        return None

    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data de nascimento": data_de_nascimento,
        "endereço": f"{logradouro}, {nro} - {bairro} - {cidade}/{sigla_estado}"
    }

    while True:
        system('CLS')
        confirmar = input(f"""-=-=-=-=-=-=-=- CRIAÇÃO DE USUÁRIO -=-=-=-=-=-=-=-

-> Informações do usuário

CPF ...............: {usuario['cpf']}
NOME ..............: {usuario['nome']}
DATA DE NASCIMENTO : {usuario['data de nascimento']}
ENDEREÇO ..........: {usuario['endereço']}

Confirmar criação de usuário? [S/N]
=> """).upper()
        if confirmar == "N":
            print("\nCriação de usuário cancelada.")
            return None
        elif confirmar == "S":
            print("\nUsuário criado com sucesso.")
            return usuario
        else:
            print("\nOpção inválida. Por favor, digite uma opção válida.")
            input('Pressione "Enter" para continuar...')

def cria_conta_corrente(agencia, n_contas, usuarios):
    
    system('cls')
    print("-=-=-=-=-=-=-=- CRIAÇÃO DE CONTA CORRENTE -=-=-=-=-=-=-=-")

    cpf = input("\nDigite seu CPF (somente os números)\n=> ")

    if cpf == "":
        print("\nVocê deixou o campo em branco. Criação de conta cancelada.")
        return None
    
    if len(cpf) != 11:
        print("\nO CPF deve possuir 11 digitos. Confira o CPF digitado. Criação de conta cancelada.")
        return None

    try:
        cpf = int(cpf)
    except ValueError:
        print("\nVocê digitou algum caractere inválido. Digite apenas os números do CPF. Criação de conta cancelada.")
        return None
    except Exception as e:
        print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o erro gerado abaixo.\n")
        print("Erro:", e.__class__, e)
        print("\nCriação de conta cancelada.")
        return None
    
    for usuario in usuarios:
        if cpf == usuario['cpf']:

            senha = input("\nInsira uma senha para sua nova conta (A senha deve ser 8 digitos numéricos).\n=> ")

            if senha == "":
                print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
                return None
    
            if len(senha) != 8:
                print("\nA senha deve conter 8 digitos numéricos. Criação de conta cancelada.")
                return None

            try:
                senha = int(senha)
            except ValueError:
                print("\nVocê digitou algum caractere inválido. Digite apenas números na senha. Criação de conta cancelada.")
                return None
            except Exception as e:
                print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o erro gerado abaixo.\n")
                print("Erro:", e.__class__, e)
                print("\nCriação de conta cancelada.")
                return None

            confirma_senha = input("\nInsira a sua senha novamente para confirmação.\n=> ")

            if confirma_senha == "":
                print("\nVocê deixou o campo em branco. Criação de usuário cancelada.")
                return None
    
            if str(senha) != confirma_senha:
                print("\nAs senhas não conferem. Criação de conta cancelada.")
                return None

            conta = {
                "agencia": agencia,
                "conta corrente": str(n_contas + 1),
                "senha": senha,
                "cpf": cpf,
                "saldo": 0,
                "limite": 500,
                "extrato": "",
                "numero_saques": 0,
            }

            while True:
                system('CLS')
                confirmar = input(f"""-=-=-=-=-=-=-=- CRIAÇÃO DE CONTA CORRENTE -=-=-=-=-=-=-=-

-> Informações da conta
                                  
AGENCIA ...........: {conta['agencia']}
CONTA CORRENTE ....: {conta['conta corrente']}
SENHA .............: ********
SALDO .............: {conta['saldo']}
LIMITE ............: {conta['limite']}

-> Proprietário da conta

CPF ...............: {usuario['cpf']}
NOME ..............: {usuario['nome']}
DATA DE NASCIMENTO : {usuario['data de nascimento']}
ENDEREÇO ..........: {usuario['endereço']}

Confirmar criação de conta? [S/N]
=> """).upper()
                if confirmar == "N":
                    print("\nCriação de conta cancelada.")
                    return None
                elif confirmar == "S":
                    print("\nConta criada com sucesso.")
                    return conta
                else:
                    print("\nOpção inválida. Por favor, digite uma opção válida.")
                    input('Pressione "Enter" para continuar...')

    print("\nCPF não cadastrado no banco de usuários. Criação de conta cancelada.")
    return None

def menu_de_operacoes(agencia, conta):

    menu_de_operacoes = f"""-=-=-=-=-=-=-=- MENU DE OPERAÇÕES -=-=-=-=-=-=-=-

Conta ativa: Agência {agencia} - Conta {conta}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Selecione uma opção
=> """

    return menu_de_operacoes

def menu_principal ():
    menu_principal = """-=-=-=-=-=-=-=- SISTEMA BANCÁRIO V2 - CAIYTHON -=-=-=-=-=-=-=-

[e] Entrar
[u] Criar usuario
[c] Criar conta corrente
[q] Sair

[lu] Listar usuários
[lc] Listar contas

Selecione uma opção
=> """

    return menu_principal

def entrar(contas):
    system('cls')
    print('-=-=-=-=-=-=-=- ENTRAR NA CONTA CORRENTE -=-=-=-=-=-=-=-')
    agencia = input("\nDigite o número da agência (Ex: 0001).\n=> ")
    conta_corrente = input("\nDigite o número da conta corrente.\n=> ")
    senha = input("\nDigite a senha de 8 dígitos da conta.\n=> ")
    
    for i, conta in enumerate(contas):
        if (conta["agencia"] == agencia) and (conta["conta corrente"] == conta_corrente) and (str(conta["senha"]) == senha):
            print("\nAcesso realizado com sucesso.")
            return i
    
    print("\nConta inválida. Por favor, verifique os dados informados e tente novamente")
    return None

def listar_contas(contas):
    system('cls')
    print('-=-=-=-=-=-=-=- LISTA DE CONTAS -=-=-=-=-=-=-=-\n')

    if len(contas) == 0:
        print("Nenhuma conta criada até o momento.")
    else:
        for i in range(len(contas)):
            conta = f"""-> INDICE {i}
AGÊNCIA ............: {contas[i]["agencia"]}
CONTA ..............: {contas[i]["conta corrente"]}
SENHA ..............: {contas[i]["senha"]}
CPF DO PROPRIETÁRIO : {contas[i]["cpf"]}
SALDO ..............: R$ {contas[i]["saldo"]:.2f}
LIMITE DE SAQUE ....: R$ {contas[i]["limite"]:.2f}
NUMERO DE SAQUES ...: {contas[i]["numero_saques"]}
"""
            print(conta)
    return 1

def listar_usuarios(usuarios):
    system('cls')
    print('-=-=-=-=-=-=-=- LISTA DE USUÁRIOS -=-=-=-=-=-=-=-\n')
    if len(usuarios) == 0:
        print("Nenhum usuário criado até o momento.")
    else:
        for i in range(len(usuarios)):
            usuario = f"""-> INDICE {i}
NOME ..............: {usuarios[i]["cpf"]}
CPF ...............: {usuarios[i]["nome"]}
DATA DE NASCIMENTO : {usuarios[i]["data de nascimento"]}
ENDEREÇO ..........: {usuarios[i]["endereço"]}
"""
            print(usuario)
    return 1

# Variáveis Globais
LIMITE_SAQUES = 3
AGENCIA = "0001"

# Vetores
usuarios = []
contas = []

# Indice da Conta ativa
i = None

# Limpa a tela para iniciar o sistema
system('cls')

while True:
    opcao = input(menu_principal()).lower()

    if opcao == "e":
        i = entrar(contas)

    elif opcao == "u":
        novo_usuario = cria_usuario()
        if novo_usuario is not None:
            usuarios.append(novo_usuario)

    elif opcao == "c":
        nova_conta = cria_conta_corrente(AGENCIA, len(contas), usuarios)
        if nova_conta is not None:
            contas.append(nova_conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "lu":
        listar_usuarios(usuarios)

    elif opcao == "q":
        print("\nVocê saiu do sistema.")
        input('Pressione "Enter" para continuar...')
        break
    
    else:
        print("\nOpção inválida, por favor selecione novamente a opção desejada.")
    
    input('Pressione "Enter" para continuar...')
    system('cls')
    
    while i is not None:
        opcao = input(menu_de_operacoes(contas[i]["agencia"], contas[i]["conta corrente"])).lower()

        if opcao == "d":
            system('cls')
            print("-=-=-=-=-=-=-=- OPERAÇÃO: DEPÓSITO BANCÁRIO -=-=-=-=-=-=-=-")
            print(f"\nConta ativa: Agência {contas[i]['agencia']} - Conta {contas[i]['conta corrente']}")
            valor = input("\nInforme o valor do depósito (Ex: 100,00)\n=> ")

            try:
                valor = float(valor.replace(',', '.'))
                contas[i]["saldo"], contas[i]["extrato"] = deposito(contas[i]["saldo"], valor, contas[i]["extrato"])
            except ValueError:
                print("\nVocê digitou algum caractere inválido. Digite o valor no formato correto (Ex: 10,00 para dez reais). Operação de depósito cancelada.")
            except Exception as e:
                print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o erro gerado abaixo.\n")
                print("Erro:", e.__class__, e)
                print("\nOperação de depósito cancelada.")

        elif opcao == "s":

            system('cls')
            print("-=-=-=-=-=-=-=- OPERAÇÃO: SAQUE BANCÁRIO -=-=-=-=-=-=-=-")
            print(f"\nConta ativa: Agência {contas[i]['agencia']} - Conta {contas[i]['conta corrente']}")
            valor = input("\nInforme o valor do saque (Ex: 100,00)\n=> ")

            try:
                valor = float(valor.replace(',', '.'))
                contas[i]["saldo"], contas[i]["extrato"], contas[i]["numero_saques"] = saque(saldo=contas[i]["saldo"],
                                                                                             valor=valor,
                                                                                             extrato=contas[i]["extrato"],
                                                                                             limite=contas[i]["limite"],
                                                                                             numero_saques = contas[i]["numero_saques"],
                                                                                             limite_saques=LIMITE_SAQUES)
            except ValueError:
                print("\nVocê digitou algum caractere inválido. Digite o valor no formato correto (Ex: 10,00 para dez reais). Operação de saque cancelada.")
            except Exception as e:
                print("\nHouve algum erro inesperado. Por favor, contate o desenvolvedor do sistema e informe o erro gerado abaixo.\n")
                print("Erro:", e.__class__, e)
                print("\nOperação de saque cancelado.")     

        elif opcao == "e":
            system('cls')
            exibe_extrato(contas[i]["saldo"], extrato=contas[i]["extrato"])
            print('')

        elif opcao == "q":
            print("\nVocê saiu de sua conta.")
            i = None

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

        input('Pressione "Enter" para continuar...')
        system('cls')
