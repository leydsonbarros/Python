from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, name, preco, descricao):
        super().__init__(name,preco)
        self.descricao = descricao
    
    def __str__(self):
        return self._name
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)