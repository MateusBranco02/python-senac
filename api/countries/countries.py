import requests

def consultar_pais_sigla():
    sigla = input('Digite a sigla do país (BR, US): ').upper()

    url = f'https://restcountries.com/v3.1/alpha/{sigla}'
    response = requests.get(url).json()

    for pais in response:
        nome_pais = pais['name']['common']
        populacao = pais['population']
        capitais = ', '.join(pais['capital'])
        print(f"País: {nome_pais}")
        print(f"Capital: {capitais}")
        print(f"População: {populacao}")


consultar_pais_sigla()
