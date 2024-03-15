from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    """Representa um restaurante e suas características."""
    restautantes = []
   
    def __init__(self,  name, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._name = name.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restautantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._name} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliação'.ljust(25)}| {'Status'}')
        for restaurante in cls.restautantes:
            print(f'{restaurante._name.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
    
    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✅' if self._ativo else '❎'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente,nota):

        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """

        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidades_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidades_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item ):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do Restaurante {self._name}\n')
        for i,item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._name} | Preço: R${item._preco} | Descriçao: {item.descricao}'
                print(mensagem_prato)
            else:
               mensagem_bebida = f'{i}. Nome:{item._name} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
               print(mensagem_bebida) 
