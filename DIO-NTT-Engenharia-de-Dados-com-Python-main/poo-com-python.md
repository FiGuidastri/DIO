# Programação Orientada a Objetos com Python
## O que é POO?
É um paradigma de programação que organiza o código em torno de objetos e sua interações
 Em python POO é implementada através de classes e objetos.

- **Classe:**  Uma classe é uma estrutura que define as caracteristicas e comportamentos de um objeto. É como um molde ou uma planta que define como um objeto deve ser criado e como ele deve se comportar.

- **Objeto:** Um objeto é uma instância de uma calsse. É uma entidade que tem suas próprias características e comportamentos, definidos pela classe.

- **Atributos:** São caracteristicas de um obejto, como variáveis que armazenm valores. Em python os atributos são definidos dentro da classe e podem ser acessados e modificados através do objeto.

- **Métodos:** São funções que pertencem a uma classe e são usadas para realizar ações em um objeto. Em python, os métodos são definidos dentro da classe e podem ser chamados através do objeto.

- **Herança:** A herança é um mecanismo que permite que uma classe herde as caracteristicas e comportamentos de outra classe. Isso permite que você crie uma hierarquia de classes e reutilize código.

- **Polimorfismo:** É a capacidade de um objeto se comportar de diferentes maneiras dependendo do contexto. Em Python, isso é alcançado através de métodos que podem ser sobrescritos ou redefinidos em subclasses.

## Construtor (ou Inicializador)
O construtor é um método especial que é chamado quando um objeto é criado. Ele é responsável por inicializar os atributos do objeto com valores padrão ou valores passados com parâmetros.

Em python, o construtor é definido como um método chamado ```__init__```. Ele é chamado automaticamente quando um objeto é criado e recebe como parâmetros os valores que devem ser atribuídos aos atributos do objeto.

## Destrutor (ou Finalizador):
O destrutor é um método especial que é chamado quando um objeto é destruído ou removido da memória. O destrutor é responsável por liberar recursos, fechar conexões ou realizar outras ações necessárias para limpar o objeto antes de sua remoção.

Em Python, o destrutor é definido com um método chamado ```__del__```. Ele é chamado automaticamente quando um objeto é removido da memória, geralmente quando não há mais referências ao objeto.

## Herança
A herança é um mecanismo que permite que uma classe herde as características e comportamentos de outra classe, isso permite que você crie uma hierarquia de classes e reutilize código.

### Herança Simples
Uma classe (a subclasse) herda as caracteristicas e comportamentos de outra classe (a superclasse). A subclasse é uma especialização da superclasse e pode adicionar ou sobrescrever os métodos da superclasse.

```super()``` -> é um método especial em Python que permite acessar a classe pai que é usado para chamar métodos ou acessar atributos da classe pai.

### Herança Múltipla
Uma classe pode herdar de mais de uma classe. Isso permite que uma classe herde características e comportamentos de várias classes.

### Resolução de conflitos
Quando uma classe herda de mais de uma classe, pode haver conflitos entre os métodos e atributos das classes pai. Em Python o conflito é resolvido pela ordem de resolução de metodos.

A ordem de resolução de métodos é a ordem em que as classes são pesquisadas para encontrar um método. Em Python, a ordem de resolução de métodos é a seguinte:
1. A classe atual
2. As classes pai, em ordem de herança

## O que é encapsulamento?
É a ideia de ocultar a implementação interna de uma classe ou objeto e fornecer apenas uma interface externa para interagir com ele.

- **Recursos Publicos** Os atributos e métodos públicos são acessíveis a partir de qualquer parte do programa. Eles não possuem restrições de acesso e podem ser utilizados livremente.

- **Encapsulamento protegido** são indicados pelo uso do prefixo de sublinhado. Eles são acessíveis a partir de fora da classe, mas podem ser utilizados pelas subclasses.

- **Encapsulamento privado** são indicados pelo uso do prefixo de dois sublinhados. Eles não são acessíveis a partir de fora da classe e nem pelas subclasses.

O encapsulamento não é uma segurança forte, mas é uma boa prática para organizar o código e evitar erros.

## Propriedades
São características que descrevem uma seção transversal de um objeto ou estrutura. Elas são calculadas dinamicamente, em vez de serem armazenadas em memória.
Além disso propriedades em Python são utilizadas para controlar o acesso e a modificação de atributos de uma classe. Elas permitem que você defina getter, setters e deleters para controlar como os atributos são acessados e modificados.
```@property``` - é o decorador que permite que as propriedades sejam utilizadas, definindo um método com uma propriedade de uma classe, tornando-o acessível como um atributo.

## Polimorfismo
Também conhecido como Duck Typing se refere à capacidade de um objeto de assumir muitas formas. Em python, o polimorfismo é alcançado através da sobrecarga de métodos e operadores.

**Polimorfismo com Herança:** quando uma classe herda de outra, ela pode sobrescrever os métodos da classe pai. Isso permite que a classe filha tenha seu próprio comportamento, mesmo que ela compartilhe a mesma interface que a classe pai.

# Interfaces e Classes Abstratas com Python
## Variáveis de Classe e Variáveis de instância
Em Python, quando se definie uma classe, podemos criar variáveis que pertencem à própria classe ou às instâncias da classe. Essas variáveis são conhecidas como variáveis de classe e variáveis de instância.

**Variáveis de Classe:** São compartilhadas por todas as instancias da classe. Elas são definidas dentro da definição da classe, mas fora de qualquer método. Essa variáveis são acessíveis por meio da classe em si e não por meio de um ainstância especifica.

**Variáveis de Instância:** São criadas quando uma instância da classe é criada. Cada instância tem sua própria cópia da variável, que pode ter um valor diferente da variável de classe.

**Diferenças:** A principal diferença entre variáveis de classe e de instância é que as variáveis de classe são compartilhadas por todas as instâncias, enquanto as variáveis de instância são exclusivas de cada instância.

Além disso as vairáveis de classe são inicializadas apenas uma vez, quando a classe é definida, enquanto as variáveis de instância são inicializadas a cada vez que uma instância é criada.

## Métodos de classe
Na programação orientada a objetos (POO), um método de classe é um método que está vinculado a uma classe pode ser chamado sem criar uma instância da classe. Isso significa que um método de classe pode ser chamado sem criar uma instância da classe. Os métodos de classe são frequentemente usados para realizar ações que estão relacionadas à classe como um todo, em vez de a uma instância específica da classe.

Em Python, um método de classe é definido usando o decorador ```@classmethod```. O primeiro parâmetro de um método de classe é sempre a classe em si, que é referida como 'cls'.

## Métodos Estáticos
É um método que pertence a uma classe, mas não tem acesso às variáveis da classe ou da instância. Os métodos estáticos são essencialmente funções que são definidas dentro de uma classe, mas não têm nenhuma conexão especial com a classe.

Em python um método estático é definido usando o decorador ```@staticmethod```

**A sintaxe dos dois métodos é identica apenas alterando o metodo que será chamado**

## Diferenças entre Métodos de Classe e Métodos Estáticos
A principal diferença entre métodos de classe e métodos estáticos é que os métodos de classe têm acesso à classe em si, enquanto os métodos estáticos não. Isso significa que os métodos de classe podem ser usados para realizar ações que dependem da classe, enquanto os métodos estáticos são mais adequados para realizar ações que não dependem da classe.

Além disso, os métodos de classe podem ser usado para criar instâncias da classe, enquanto os métodos estáticos não.

# Interfaces
Em programação orientada a objetos, uma interface é um contrato que define um conjunto de métodos que uma classe deve implementar, ela define uma estrutura de métodos que uma classe deve ter, mas não define como esses métodos devem ser implementados.

Em python as interfaces não são explicitamente definidas como em linguagens como Java ou C#. No entanto, o conceito de interface é implementado usando classes abstratas.

### Caracteristicas de uma interface
- **Define um contrato:** uma interface define um conjunto de métodos que uma classe deve implementar.
- **Não define a implementação:** uma interface não define como os métodos devem ser implementados
- **Pode ser herdada:** uma classe pode herdar de uma interface e implementar seus métodos.
- **Pode ser usada para polimorfismo:** pode ser usada como um tipo de dados para uma variável ou parâmetro, permitindo que classes diferentes sejam tratadas como se fossem da mesma classe.

# Classe abstrata

## O que são classes abstratas?

Em programação orientada a objetos (POO), uma classe abstrata é uma classe que não pode ser instanciada diretamente e serve como uma base para outras classes. Uma classe abstrata define um conjunto de métodos e propriedades que devem ser implementados pelas classes que herdam dela.

Uma classe abstrata é como um modelo ou um template que define a estrutura e o comportamento de uma classe, mas não fornece uma implementação completa. As classes que herdam de uma classe abstrata devem implementar os métodos e propriedades definidos na classe abstrata.

## Características de uma classe abstrata

Uma classe abstrata tem as seguintes características:

Não pode ser instanciada: Uma classe abstrata não pode ser instanciada diretamente, ou seja, não é possível criar um objeto a partir de uma classe abstrata.
Define um contrato: Uma classe abstrata define um conjunto de métodos e propriedades que devem ser implementados pelas classes que herdam dela.
Pode ter implementação parcial: Uma classe abstrata pode ter implementação parcial, ou seja, pode ter métodos e propriedades que são implementados, mas também pode ter métodos abstratos que devem ser implementados pelas classes que herdam dela.
Pode ser herdada: Uma classe abstrata pode ser herdada por outras classes, que devem implementar os métodos e propriedades definidos na classe abstrata.