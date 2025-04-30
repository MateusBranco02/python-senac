biblioteca = []

livro = {
    "titulo": '',
    "autor": '',
    "ano": ''
}

def cadastrar_livros():
    print('Testando a chamada da função dentro do math case!')

while True:
    opcao = input('Escolha uma das opções: ').upper()
    print('1 - Cadastrar livro(s)')
    print('2 - Listar todos os livro(s)')
    print('3 - Buscar livro(s) pelo autor')
    print('4 - Sair')
    match opcao:
        case '1':
           cadastrar_livros()
        case '4':
            break
        case _:
            print('Opção inválida!')
