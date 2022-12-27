# Python Testes
O repositório **"python-testes"** é um projeto que contém exemplos de testes em Python utilizando a biblioteca **"unittest"**.

Como usar
Para utilizar este projeto, é necessário ter o Python instalado em sua máquina. Além disso, é recomendado utilizar um gerenciador de pacotes como o **"pip"** para instalar as dependências do projeto.

1. Clone o repositório em sua máquina:

```git clone https://github.com/rafaelmachadobr/python-testes.git```

2. Acesse o diretório do projeto:

```cd python-testes```

3. Crie um ambiente virtual (opcional, mas recomendado):

```python -m venv .venv```

4. Ative o ambiente virtual:

```source .venv/bin/activate```

5. Instale as dependências do projeto:

```pip install -r requirements.txt```

6. Execute os testes:

```python -m unittest discover```

## Estrutura do projeto

O projeto possui a seguinte estrutura de pastas:

```
python-testes/
├── README.md
├── requirements.txt
└── tests/
    ├── test_calculadora.py
    └── test_jokenpo.py
```

- O arquivo requirements.txt contém a lista de dependências do projeto.
- A pasta tests/ contém os arquivos de teste. Cada arquivo de teste deve começar com test_ e possuir a extensão .py.

## Exemplos de testes
O projeto possui dois exemplos de testes:

- **"test_calculadora.py"**: Contém testes para a classe **"Calculadora"**, que possui métodos para realizar operações básicas de adição, subtração, multiplicação e divisão.
- **"test_jokenpo.py"**: Contém testes para a classe **"Jokenpo"**, que simula o jogo Jokenpo (Pedra, Papel e Tesoura).

Cada teste é definido como um método dentro de uma classe que herda de **"unittest.TestCase"**. Para executar os testes, basta usar o comando ```python -m unittest discover``` na raiz do projeto.
