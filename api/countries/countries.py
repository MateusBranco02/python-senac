import requests

def consultar_codigo_pais():
    cod = input('Digite o código do país: ').upper()
    url = f'https://restcountries.com/v3.1/alpha/{cod}'
    response = requests.get(url).json()
    for pais in response:
        nome_pais = pais['name']['common']
        populacao = pais['population']
        capital = pais['capital']
        for i in capital:
            posi = i
        print(f"País: {nome_pais}")
        print(f"Capital: {posi}")
        print(f"População: {populacao}")

consultar_codigo_pais()
