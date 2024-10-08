import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f'''
            Agencia:\t{conta.agencia}
            C.C.:\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t{conta.saldo:.2f}   
        '''
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0
    
    def realizar_transacao(self, conta, transacao):
        #todo: validar o número de transações e invalidar a operação se for necessário
        #print('\n@@@ você execedeu o número de transações permitidas para hoje! @@@')
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\n@@@ Operação Falhou! Você não tem saldo suficiente. @@@')

        elif valor > 0:
            self._saldo -= valor
            print('\n=== Saque realizado com sucesso! ===')
            return True
    
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
            
        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n=== Depósito realizado com sucesso! ===')
        else:
            print('\n@@@ operação Falhou! O valor informado é inválido!')
            return False
        
        return True


class ContaCorrente:
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print('\n@@@ Operação Falhou! Você excedeu o seu limite! @@@')

        elif excedeu_saques:
            print('\n@@@ Operação Falhou! Você excedeu o número de saques permitido! @@@')

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''
        Agencia:\t{self.agencia}
        C.C.:\t{self.numero}
        Titular:\t{self.cliente.nome} {self.cliente.sobrenome}
    '''


class Historico:
    def __init__(self);
        self._transacoes
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': transacao.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao['tipo'].lower() == tipo_transacao.lower():
                yield transacao
    
    #TODO: filtrar todas as transacoes realizadas no dia
    def transacoes_do_dia(self):
        pass


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass
