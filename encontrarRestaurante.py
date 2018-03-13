from geolocalizar import GeoLocalizar
import json
import httplib2

import sys
import codecs

#Código padrão do python 3 para permitir acentos nas Strings
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

''' Siga os passos em https://developer.foursquare.com/docs/api/getting-started
E cole aqui seus IDs, lembre-se, tem que criar um app, pode colocar uma url 
 que não existe!
'''
foursquare_client_id = "Cole aqui seu ID Cliente"
foursquare_client_secret = "Cole aqui seu ID SECRET"


def encontrarRestaurante(tipoComida,localidade):
	# Usando o geolocalizar para pegar latitude e longitude do Google Maps!
    # Lembre-se que para importar o arquivo precisa estar na mesma pasta que este aqui!!!!
	latitude, longitude = GeoLocalizar(localidade)
	# Usando a API do foursquare para encontrar o restaurante mais próximo com as strings latitude, longitude e tipo de comida.
	# Lendo a documentação, o formato da url é nesse estilo https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    # então...
    url = ('https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20130815&ll={},{}&query={}'.format(foursquare_client_id, foursquare_client_secret,latitude,longitude,tipoComida))
	
    #1. Faça você a requisição, lembre-se dos comandos padrões
    h = # preencha aqui
	result = # preencha aqui

	print(result)
    # Seguindo a documentação da foursquare 'venues' são os locais
	if result['response']['venues']:

		#2.  Achando o primeiro restaurante - FAÇA VOCÊ
		restaurante = #analise a variável result e pegue o primeiro dado
		
        # Armazenando o nome e endereço
		NomeRestaurante = restaurante['name']
		EnderecoRestaurante = restaurante['location']['formattedAddress']

        # Formatando o Endereço
		endereco = ""
		for i in EnderecoRestaurante:
			endereco += i + " "
		EnderecoRestaurante = endereco
		DadosRestaurante = {'name':NomeRestaurante, 'address':EnderecoRestaurante}
        # Mostrando os resultados
		print("Nome do Restaurante: {}".format(DadosRestaurante['name']))
		print("Endereço do Restaurante: {}".format(DadosRestaurante['address']))
		return DadosRestaurante
	else:
		print("Não foram encontrados restaurantes na localização: {}".format(localidade))
		return "Nenhum restaurante encontrado"

if __name__ == '__main__':
    #3. Rode aqui a função, mude o tipo de comida e a localização para testar
	encontrarRestaurante("Pizza", "porto velho, brasil")
