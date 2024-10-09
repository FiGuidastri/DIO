# Gerenciamento de pacotes, Convenções e Boas Práticas em Python

## O que são pacotes e o uso do pip
### O que são pacotes em Python?
Pacotes são módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você utilize código que foi escrito por outras pessoas, economizando tempo e esforço.

### O papel do Pip
Pip é o gerenciador de pacotes do Python. Ele nos permite instalar, atualizar e remover pacotes facilmente. Ele se comunica  com o PyPI (Python Package Index), que é onde a maioria dos pacotes Python são armazenados.

### Uso de ambientes virtuais
Ambientes virtuais, como os criados por venvs, nos permitem manter as dependências de diferentes projetos. Isso é importante para evitar conflitos entre versões de pacotes.

### Comandos do PIP
Como programador que está aprendendo Python e deseja gerenciar os pacotes do projeto, é importante conhecer alguns dos principais comandos do pip.

- Instalar pacote ```pip install nome_do_pacote```
- Desinstalar pacote ```pip uninstall nome_do_pacote```
- Atualizar pacote ```pip install --upgrade nome_do_pacote```
- Listar pacotes intalados ```pip list```
- procurar pacotes ```pip search termo_de_busca```

## Gerenciando dependencias com Pip Env
### Introdução ao pipenv
Pipenv é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile conforme você instala e  desinstala pacotes.
