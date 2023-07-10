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

Em desenvolvimento...