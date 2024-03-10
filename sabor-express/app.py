import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False}, 
                {'nome': 'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('\n\nＳａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. alternar Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('𝙁𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙣𝙙𝙤 𝙤 𝘼𝙋𝙋')

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma telca para voltar ao menu principal\n')
    main()


def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    print('Opção Invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' *(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print() 

def cadastrar_novo_restaurante():

    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    
    exibir_subtitulo('Cadastro de Novos Restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da Categoria do Restaurante {nome_do_restaurante}: ')
    print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso!! \n')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
   
    voltar_ao_menu_principal()

def listar_restaurante():

    ''' Lista os restaurantes presentes no dicionario 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    
    exibir_subtitulo('Listando Restaurantes')
    
    print(f'{'Nome  do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def  alternar_estado_restaurante():

    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando Estado do Restaurante')
    
    nome_restaurante = input('Digite o nome do Restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def escolher_opcao():

    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    ''' 

    try:
        opcao_escolhida = int(input('Escolha uma Opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

