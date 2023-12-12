from flask import Flask, request, jsonify
from itertools import groupby
from operator import itemgetter
from pymongo import MongoClient
import requests
import os

app = Flask(__name__)

API_KEY = os.environ["OPENWEATHER_API_KEY"]
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

client = MongoClient('localhost', 27017)  
db = client['previsao_tempo']
collection = db['previsao_dias']

@app.route('/', methods=['GET'])
def root():
    return "<h1>Utilize o endpoint /previsao juntamente com o nome da cidade para saber sobre o clima do local desejado</h1>"

@app.route('/previsao', methods=['POST'])
def obter_previsao_tempo():
    new_data = request.get_json()
    cidade = new_data["cidade"]

    params = {
        'q': cidade,
        'appid': API_KEY,
        'lang': 'pt_br'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': 'Erro ao obter dados da API'}), response.status_code

    previsao = [{'data': item['dt_txt'], 'temperatura': item['main']['temp']} for item in data['list']]
    converter_para_celsius = lambda temp_kelvin: round(temp_kelvin - 273.15)
    previsao_em_celsius = [{"data": entrada["data"], "temperatura": converter_para_celsius(entrada["temperatura"])} for entrada in previsao]
    previsao_por_dia = {dia: list(grupo) for dia, grupo in groupby(previsao_em_celsius, key=lambda x: x['data'][:10])}

    previsao_max_min = [{"data": dia, "temperatura": {"maxima": max(entradas, key=lambda x: x['temperatura'])['temperatura'], "minima": min(entradas, key=lambda x: x['temperatura'])['temperatura']}} for dia, entradas in previsao_por_dia.items()]

    for entrada in previsao_max_min:
        collection.insert_one({
            'cidade': cidade,
            'data': entrada['data'],
            'temperatura_maxima': entrada['temperatura']['maxima'],
            'temperatura_minima': entrada['temperatura']['minima']
        })

    return jsonify(previsao_max_min)

@app.route('/historico', methods=['GET'])
def historico():
    historico_dados = list(collection.find({}, {'_id': 0}))
    return jsonify(historico_dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
