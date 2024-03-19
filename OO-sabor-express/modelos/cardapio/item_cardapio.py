from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, name, preco):
        self._name = name
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass