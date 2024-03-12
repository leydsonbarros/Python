class Restaurante:
    restautantes = []
    def __init__(self,  name, categoria):
        self._name = name.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restautantes.append(self)
    
    def __str__(self):
        return f'{self._name} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restautantes:
            print(f'{restaurante._name.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    
    def alternar_estado(self):
        self._ativo = not self._ativo




restaurante_praca = Restaurante('Preça','Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express','Italiano')
Restaurante.listar_restaurantes()