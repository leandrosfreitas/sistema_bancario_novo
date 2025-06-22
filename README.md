# 💰 Sistema Bancário com Python e Programação Orientada a Objetos

Este projeto é uma simulação de um sistema bancário simples, desenvolvido em Python, utilizando os princípios da **Programação Orientada a Objetos (POO)**. O sistema permite **criar clientes, contas, realizar depósitos, saques e consultar extratos**.

---

## ⚙️ Funcionalidades

- Criar clientes com CPF, nome, data de nascimento e endereço
- Criar contas bancárias (Conta Corrente com limite de saque e quantidade de saques diários)
- Realizar **depósitos** e **saques**, com validações
- Gerar e exibir **extratos de transações**
- Listar contas criadas
- Menu interativo em modo texto

---

## 🧱 Arquitetura do Projeto

- `Cliente` (classe base)
- `PessoaFisica` (herda de `Cliente`)
- `Conta` (classe base com métodos de saque e depósito)
- `ContaCorrente` (herda de `Conta`, com regras específicas)
- `Historico` (registro de transações)
- `Transacao` (classe abstrata)
  - `Saque` e `Deposito` (herdam de `Transacao`)

---

## 🧠 Conceitos Aplicados

- Encapsulamento e herança
- Métodos e propriedades
- Classes abstratas e polimorfismo
- Validação de dados do usuário
- Registro e histórico de operações

---

## ▶️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
