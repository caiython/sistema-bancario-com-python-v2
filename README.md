# Sistema Bancário V2 - Caiython

<p style="font-size: 12px">Repositório dedicado à entrega do desafio "Otimizando o Sistema Bancário com Funções Python" do Bootcamp de Data Science da DIO em parceria com a Potência Tech do iFood.</p>

## Proposta 

Otimizar a versão 1 do sistema bancário através da criação de funções para as operações do sistema já existentes e adicionar duas novas funções para criação de usuários e de contas.

## Regras de Criação para as Funções das Operações Já Existentes na Primeira Versão do Sistema
|Função|Argumentos|Retorno|Regras|
|------|----------|-------|------|
|Depósito|Saldo, Valor e Extrato|Saldo e Extrato|Argumentos Positional Only|
|Saque|Saldo, Valor, Extrato, Valor Limite de Saque, Numero de Saques e Limite de Quantidade de Saques|Saldo e Extrato|Argumentos Keyword Only|
|Extrato|Saldo e Extrato|N/A|Saldo Positional e Extrato Keyword|

## Novas Funções

### Criar Usuário
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

### Criar Conta Corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

# Solução
Como solução, na versão 2 do sistema, além de todos os requisitos propostos pelo desafio, eu desenvolvi o sistema voltado à experiência do usuário, inserindo quebras de linhas estratégicas, que melhoram a visualização, e atribuindo condições específicas nos inputs do usuário para mante-los limpos, além de exibir mensagens de erros específicas para cada caso. O código do sistema totalizou 468 linhas, 10 funções e cerca de 5 horas de pesquisa e desenvolvimento.

## Funções Criadas
### Saque, Depósito e Extrato

```saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques)```

```deposito(saldo, valor, extrato, /)```

```exibe_extrato(saldo, *, extrato)```

A função das operações contidas na versão 1 do sistema são um copy/paste do que já estava desenvolvido para dentro da função.O diferencial é o de que, agora, dentro de suas respectivas funções, os argumentos estão de acordo com a proposta do desafio.

### Função Criar Usuário

```cria_usuario()```

A função de criar usuária é extensa e complexa. Ela faz a coleta dos dados do usuário onde, cada dado, possui suas regras de entrada. Os inputs são dados dentro da própria função. Ao final da criação, é exibida uma tela com todos os dados para o usuário confirmá-los.

#### Inputs

|Dado|Regras de Entrada|
|----|-----------------|
|CPF|NOT NULL + tamanho igual a 11 + convertível para int.|
|Nome|NOT NULL.|
|Data de Nascimento|NOT NULL + convertível para um objeto datetime.|
|Logradouro|NOT NULL.|
|Número|NOT NULL + convertível para int.|
|Bairro|NOT NULL|
|Cidade|NOT NULL|
|Sigla do Estado|NOT NULL + tamanho igual a 2|

#### Retorno
```
{
    "cpf": cpf,
    "nome": nome,
    "data de nascimento": data_de_nascimento,
    "endereço": f"{logradouro}, {nro} - {bairro} - {cidade}/{sigla_estado}"
}
```

### Função Criar Conta Corrente

```cria_conta_corrente(agencia, n_contas, usuarios)```

A criação de conta é feita atribuindo-a a um usuário. A função recebe o número da agência (variável global), o número de contas para definir o número da nova conta, e a lista de usuários para verificar a qual usuário a nova conta deve ser atribuida. Ao final da função são exibidos os dados inseridos e os dados gerados pelo sistema para que o usuário confirme.

#### Inputs

|Dado|Regras de Entrada|
|----|-----------------|
|CPF|NOT NULL + tamanho igual a 11 + convertível para int.|
|Senha|NOT NULL + tamanho igual a 8 + convertível para int.|
|Confirma Senha|NOT NULL + igual a Senha|

#### Retorno

```
{
    "agencia": agencia,
    "conta corrente": str(n_contas + 1),
    "senha": senha,
    "cpf": cpf,
    "saldo": 0,
    "limite": 500,
    "extrato": "",
    "numero_saques": 0,
}
```

### Função Menu Principal e Menu de Operações

```menu_principal()```

```menu_de_operacoes(agencia, conta)```

As funções de menu principal e menu de operações são funções de exibição dos menus de opções. O menu de operações recebe como argumento a agencia e a conta ativa para melhorar a experiência do usuário.

#### Exibição Menu Principal
```
-=-=-=-=-=-=-=- SISTEMA BANCÁRIO V2 - CAIYTHON -=-=-=-=-=-=-=-

[e] Entrar
[u] Criar usuario
[c] Criar conta corrente
[q] Sair

[lu] Listar usuários
[lc] Listar contas

Selecione uma opção
=> 
```

#### Exibição Menu de Operações
```
-=-=-=-=-=-=-=- MENU DE OPERAÇÕES -=-=-=-=-=-=-=-

Conta ativa: Agência {agencia} - Conta {conta}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Selecione uma opção
=> 
```

### Função Entrar

```entrar(contas)```

A função entrar serve para que o usuário acesse a sua conta, saindo do menu principal para o menu de operações em sua conta. A função recebe como argumento o array contendo as contas criadas. Dentro da própria função, o usuário dá input na agência, conta e senha criada, então o sistema procura os dados informados no array de contas, dando acesso caso a mesma seja encontrada. O acesso é dado através do retorno do índice da conta encontrada.

#### Algoritmo
```
agencia = input("\nDigite o número da agência (Ex: 0001).\n=> ")
conta_corrente = input("\nDigite o número da conta corrente.\n=> ")
senha = input("\nDigite a senha de 8 dígitos da conta.\n=> ")

for i, conta in enumerate(contas):
    if (conta["agencia"] == agencia) and (conta["conta corrente"] == conta_corrente) and (str(conta["senha"]) == senha):
        print("\nAcesso realizado com sucesso.")
        return i
```

### Função Listar Usuários e Listar Contas

```listar_usuarios(usuarios)```

```listar_contas(contas)```

Por fim, as funções de listar contas e listar usuários são funções administrativas, responsáveis por exibir para o operador os usuários ou as contas cadastradas no sistema.

#### Exemplo de Exibição de Lista de Usuários

```
-=-=-=-=-=-=-=- LISTA DE USUÁRIOS -=-=-=-=-=-=-=-
-> INDICE 0
NOME ..............: JOSÉ DA SILVA PEREIRA
CPF ...............: 12345678910
DATA DE NASCIMENTO : 01/02/2003
ENDEREÇO ..........: Rua São Paulo, 56 - Vila Paulista - São Paulo/SP

-> INDICE 1
NOME ..............: ROSELI ANDRADE CAMARGO
CPF ...............: 10987654321
DATA DE NASCIMENTO : 03/04/2005
ENDEREÇO ..........: Rua dos Anjos, 17 - Vila Belmiro - Santos/SP
```

#### Exemplo de Exibição de Lista de Contas

```
-=-=-=-=-=-=-=- LISTA DE CONTAS -=-=-=-=-=-=-=-
-> INDICE 0
AGÊNCIA ............: 0001
CONTA ..............: 1
SENHA ..............: 87654321
CPF DO PROPRIETÁRIO : 12345678910
SALDO ..............: R$ 3200,00
LIMITE DE SAQUE ....: R$ 500,00
NUMERO DE SAQUES ...: 2

-> INDICE 1
AGÊNCIA ............: 0001
CONTA ..............: 2
SENHA ..............: 12345678
CPF DO PROPRIETÁRIO : 10987654321
SALDO ..............: R$ 1000,00
LIMITE DE SAQUE ....: R$ 500,00
NUMERO DE SAQUES ...: 0
```

## Considerações Finais

Com certeza existem diversos pontos do código que podem ser melhorados, mas, apesar disso, com a finalização da versão 2, o resultado cumpriu com o seu principal objetivo e a experiência do usuário ficou satisfatória.

O código está disponível para visualização de todos. Sou totalmente mente aberta e críticas construtivas são bem-vindas.
