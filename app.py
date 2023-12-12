from flask import Flask, request, jsonify
import requests
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

API_KEY = '11099dcc6bf337d99a6e478cbcd27994'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

client = MongoClient('localhost', 27017)
db = client['previsoes']
collection = db['previsoes_regioes']

def obter_previsao_api(regiao):
    params = {
        'q': regiao,
        'appid': API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        previsao = [{'data': item['dt_txt'], 'temperatura': item['main']['temp']} for item in data['list']]
        return previsao
    else:
        return None

@app.route('/limpar_banco', methods=['GET'])
def limpar_banco():
    try:
        collection.delete_many({})
        return jsonify({'message': 'Banco de dados limpo com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/inserir_ficticios', methods=['GET'])
def inserir_registros_ficticios():
	regioes = ['Lisbon', 'Berlin', 'Paris', 'New York', 'Tokyo', 'Sydney', 'Rio de Janeiro', 'Cape Town', 'Moscow', 'Beijing']

	collection.delete_many({})

	for regiao in regioes:
		previsao_data = obter_previsao_api(regiao)
		if previsao_data:
			registro = {
				'regiao': regiao,
				'previsao': previsao_data,
				'timestamp': datetime.now()
			}
			collection.insert_one(registro)

	print('Registros fictícios inseridos com sucesso!')



@app.route('/imprimir_dados', methods=['GET'])
def imprimir_dados_mongodb():
	for documento in collection.find():
		print(f"Região: {documento['regiao']}")
		print(f"Previsão: {documento['previsao']}")
		print(f"Timestamp: {documento['timestamp']}")
		print("\n")

	print('message','Dados impressos com sucesso!')


if __name__ == '__main__':

    inserir_registros_ficticios() 
    imprimir_dados_mongobd()

    # app.run(debug=True)
