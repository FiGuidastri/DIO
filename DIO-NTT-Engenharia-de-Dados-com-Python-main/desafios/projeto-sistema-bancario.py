from abc import ABC, abstractmethod

# Criando a classe cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

# Criando a classe conta
class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        
    def saldo(self):
        return self.saldo
            
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(f'Saque realizado de R$ {valor:.2f}')
            return True 
        return False
    
    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(f'Depósito realizado no valor de R$ {valor:.2f}')
    
    @classmethod
    def nova_conta(cls, cliente, numero, agencia):
        return cls(cliente, numero, agencia)

# Criando a classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []
        
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Criando a classe Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
        
# Criando a classe Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        
    def registrar(self, conta):
        conta.depositar(self.valor)

# Criando a classe Saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

# Criando a classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

# Criando a classe PessoaFisica
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Função para criar um novo cliente
def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
    endereco = input("Digite o endereço: ")
    return PessoaFisica(cpf, nome, data_nascimento, endereco)

# Função para criar uma nova conta
def criar_conta(cliente):
    numero = int(input("Digite o número da conta: "))
    agencia = input("Digite o número da agência: ")
    limite = float(input("Digite o limite da conta: "))
    limite_saques = int(input("Digite o limite de saques por dia: "))
    conta = ContaCorrente(cliente, numero, agencia, limite, limite_saques)
    cliente.adicionar_conta(conta)
    print(f"Conta {numero} criada com sucesso!")

# Função para exibir o menu de interação
def exibir_menu(clientes):
    while True:
        print("\n----- MENU -----")
        print("1. Criar novo cliente")
        print("2. Criar nova conta")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("5. Exibir saldo e histórico")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cliente = criar_cliente()
            clientes.append(cliente)
            print(f"Cliente {cliente.nome} criado com sucesso!")
            
        elif opcao == '2':
            if not clientes:
                print("Não há clientes disponíveis. Crie um cliente primeiro.")
            else:
                for i, cliente in enumerate(clientes):
                    print(f"{i + 1}. {cliente.nome}")
                indice_cliente = int(input("Escolha o cliente para criar a conta: ")) - 1
                cliente = clientes[indice_cliente]
                criar_conta(cliente)
                
        elif opcao == '3':
            if not clientes:
                print("Não há clientes disponíveis.")
            else:
                for i, cliente in enumerate(clientes):
                    print(f"{i + 1}. {cliente.nome}")
                indice_cliente = int(input("Escolha o cliente: ")) - 1
                cliente = clientes[indice_cliente]
                for i, conta in enumerate(cliente.contas):
                    print(f"{i + 1}. Conta {conta.numero} - Agência {conta.agencia}")
                indice_conta = int(input("Escolha a conta para depósito: ")) - 1
                conta = cliente.contas[indice_conta]
                valor = float(input("Digite o valor do depósito: "))
                deposito = Deposito(valor)
                cliente.realizar_transacao(conta, deposito)
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                
        elif opcao == '4':
            if not clientes:
                print("Não há clientes disponíveis.")
            else:
                for i, cliente in enumerate(clientes):
                    print(f"{i + 1}. {cliente.nome}")
                indice_cliente = int(input("Escolha o cliente: ")) - 1
                cliente = clientes[indice_cliente]
                for i, conta in enumerate(cliente.contas):
                    print(f"{i + 1}. Conta {conta.numero} - Agência {conta.agencia}")
                indice_conta = int(input("Escolha a conta para saque: ")) - 1
                conta = cliente.contas[indice_conta]
                valor = float(input("Digite o valor do saque: "))
                saque = Saque(valor)
                if cliente.realizar_transacao(conta, saque):
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente.")
                    
        elif opcao == '5':
            if not clientes:
                print("Não há clientes disponíveis.")
            else:
                for i, cliente in enumerate(clientes):
                    print(f"{i + 1}. {cliente.nome}")
                indice_cliente = int(input("Escolha o cliente: ")) - 1
                cliente = clientes[indice_cliente]
                for i, conta in enumerate(cliente.contas):
                    print(f"{i + 1}. Conta {conta.numero} - Agência {conta.agencia}")
                indice_conta = int(input("Escolha a conta para exibir saldo e histórico: ")) - 1
                conta = cliente.contas[indice_conta]
                print(f"Saldo: R$ {conta.saldo:.2f}")
                print("Histórico de transações:")
                for transacao in conta.historico.transacoes:
                    print(transacao)
                    
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Lista de clientes
clientes = []

# Executar o menu de interação
exibir_menu(clientes)
