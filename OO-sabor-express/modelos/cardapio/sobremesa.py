from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, name, preco, descricao, tipo, tamanho):
        super().__init__(name,preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho
    
    def __str__(self):
        return self._name
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)