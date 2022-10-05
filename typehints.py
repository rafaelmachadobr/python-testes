from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 15
flutuante: float = 18.5
booleano: bool = True
string: str = 'Rafael Machado'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Rafael']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Rafael')

# Dicionários e conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Rafael', 'sobrenome': 'Machado', 'idade': 18}
pessoa2: MeuDict = {'nome': 'Rafael',
                    'sobrenome': 'Machado', 'idade': 18}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(842893942)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(14, 16))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x*2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar2([1, 2, 3]))
