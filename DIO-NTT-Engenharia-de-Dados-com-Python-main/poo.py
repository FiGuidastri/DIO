# %%
# Exemplo de classe
class Carro:
    def __init__(self, marca, modelo, ano): # esse é o construtor da classe "Carro"
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

meu_carro = Carro('Ford', 'Focus', 2015)
print(meu_carro.marca) # Ford
meu_carro.acelerar()
print(meu_carro.velocidade) # 10
meu_carro.frear()
print(meu_carro.velocidade) # 0
# %%
# Exemplo de classe com destrutor
class ConexaoDB:
    def __init__(self, host, usuario, senha): # construtor de classe
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.conexao = self.estabelecer_conexao()
    
    def estabelecer_conexao(self):
        # código para estabelecer conexão com o banco de dados
        pass

    def __del__(self): # destrutor
        self.fechar_conexao()

    def fechar_conexao(self):
        # código para fechar conexão com o banco de dados
        pass

conexao = ConexaoDB('localhost', 'usuario', 'senha')
# uso da conexão
del conexao # ou conexao = None
# %%
# Exemplo herança simples
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f'{self.nome} está comendo')

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome) # permite acessar a classe pai
        self.raca = raca

    def latir(self):
        print(f'{self.nome} está latindo')

meu_cachorro = Cachorro('Buddy', 'Poodle')
meu_cachorro.comer()
meu_cachorro.latir()
# %%
# exemplo de herança multipla
class Animal:
    def __init__(self, nome): #construtor
        self.nome = nome
    
    def comer(self):
        print(f'{self.nome} está comendo')
    
class Mamifero:
    def __init__(self, nome, cor_pelagem):
        self.cor_pelagem = cor_pelagem

    def amamentar(self):
        print(f'{self.nome} está amamentando')

class Cachorro(Animal, Mamifero): # uma classe pode receber como parametro outras classes
    def __init__(self, nome, raca, cor_pelagem):
        Animal.__init__(self, nome) # chama o construtor da classe pai
        Mamifero.__init__(self, nome, cor_pelagem) # chama o constr
        self.raca = raca

    def latir(self):
        print(f'{self.nome} está latindo!')

meu_cachorro = Cachorro('Buddy', 'Poodle', 'Branco')
meu_cachorro.comer()
meu_cachorro.latir()
meu_cachorro.amamentar()


# %%
# Exemplo de encapsulamento
class A:
    a = 1 # atributo público
    _b = 2 # atributo protegido
    __c = 3 # atributo privado

class B(A):
    def __init__(self):
        print(self.a) # imprime 1
        print(self._b) # imprime 2
        print(self.__c) # erro pois __c é privado

a = A()
print(a.a) # imprime 1
print(a._b) # imprime 2
print(a.__c) # erro, pois __c é privado

b = B()
# %%
# exemplo de propriedades
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    @property
    def area(self):
        return self.largura * self.altura
    
retangulo = Retangulo(5, 3)
print(retangulo.area) # imprime 15
# %%
# Exemplo de polimorfismo com herança
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

class Heroi(Personagem):
    def __init__(self, nome, vida, habilidade):
        super().__init__(nome, vida) # herda os atributos da classe pai "personagem"
        self.habilidade = habilidade

class Vilao(Personagem):
    def __init__(self, nome, vida, poder):
        super().__init__(nome, vida) # herda os atributos da classe pai "personagem"
        self.poder = poder
    
def atacar(personagem):
        print(f"{personagem.nome} está atacando!")

heroi1 = Heroi('Superman', 100, 'Voo')
vilao1 = Vilao('Lex Luthor', 80, 'Inteligencia')

atacar(heroi1)
atacar(vilao1)
# %%
# exemplo duck typing
class Pato:
    def grasna(self):
        print("Quack!")
    
class Ganso:
    def grasna(self):
        print("Quack!")

if __name__ == '__main__':
    pato = Pato()
    print(pato.grasna())

    ganso = Ganso()
    print(ganso.grasna())
# %%
# Exemplo de variável de classe
class MyClass:
    class_variable = 'Este é uma variável de classe'

print(MyClass.class_variable)
# %%
# Exemplo de Variável de Instância
class MyClass:
    def __init__(self, name):
        self.instance_variable = name

obj1 = MyClass('Objeto 1')
obj2 = MyClass('Objeto 2')

print(obj1.instance_variable)
print(obj2.instance_variable)
# %%
# Exemplo de metodo de classe
class MinhaClasse:
    @classmethod
    def meu_metodo_de_classe(cls, arg1, arg2):
        # faça alg com cls e arg1 e arg2
        pass

# para chamar um método de classe é utilizada a seguinte sintaxe
MinhaClasse.meu_metodo_de_classe('arg1', 'arg2')
# %%
# Exemplo prático de métodos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pessoa(cls, nome, idade):
        return cls(nome, idade)
    
    @staticmethod
    def calcular_idade(anos):
        return anos * 365
    
pessoa = Pessoa.criar_pessoa('Filipe', 27)
print(pessoa.nome)
print(pessoa.idade)

dias = Pessoa.calcular_idade(30)
print(dias)
# %%
# exemplo de interface
from abc import ABC, abstractmethod

class IPrintable(ABC):
    @abstractmethod
    def print(self):
        pass

class Documento(IPrintable):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def print(self):
        print(self.conteudo)


class Imagem(IPrintable):
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def print(self):
        print(f'Imagem: {self.arquivo}')
    
documento = Documento('Olá, Mundo!')
imagem = Imagem('imagem.jpg')

def imprimir(obj: IPrintable):
    obj.print()

imprimir(documento)
imprimir(imagem)
    
# %%
# exemplo de classe abstrata
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_barulho(self):
        pass

    def comer(self):
        print("Comendo...")

class Cachorro(Animal):
    def fazer_barulho(self):
        print("Latindo!")

class Gato(Animal):
    def fazer_barulho(self):
        print("Miando!")

# animal = Animal()  # Erro! Não é possível instanciar uma classe abstrata
cachorro = Cachorro()
gato = Gato()

cachorro.fazer_barulho()  # imprime "Latindo!"
gato.fazer_barulho()  # imprime "Miando!"
cachorro.comer()  # imprime "Comendo..."
gato.comer()  # imprime "Comendo..."

# %%
