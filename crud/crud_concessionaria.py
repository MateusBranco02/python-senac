estoque_veiculos = []

def cadastrar_veiculos(marca, modelo, ano, preco):
    estoque_veiculos.append({ 'marca': marca, 'modelo': modelo, 'ano': ano, 'preco': preco })


def lista_veiculos():
    for veiculo in estoque_veiculos:
        if not veiculo: print('Nenhum veículo em estoque no momento!')
        print(veiculo)


def atualizar_veiculo(index, marca, modelo, ano, preco):
    estoque_veiculos[index]['marca'] = marca
    estoque_veiculos[index]['modelo'] = modelo
    estoque_veiculos[index]['ano'] = ano
    estoque_veiculos[index]['preco'] = preco


def deletar_veiculo(index):
    estoque_veiculos.pop(index)
    print(f'O veículo do índice "{index}" foi removido com sucesso!')


cadastrar_veiculos('VW', 'Gol', 2021, 55000)
lista_veiculos()

atualizar_veiculo(0, 'VW', 'Gol', 2021, 60000)
lista_veiculos()

deletar_veiculo(0)
lista_veiculos()