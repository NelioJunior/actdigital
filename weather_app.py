'''
exemplo de uso http://localhost:5000/previsao?cidade=bahia
'''

from flask import Flask,request, jsonify
import requests
import os 

app = Flask(__name__)

API_KEY = os.environ["OPENWEATHER_API_KEY"]
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

@app.route('/', methods=['GET'])
def root():
    return "<h1>utilize o endpoint /previsao juntamente como nome da cidade para saber sobre o clima do local desejado</h1>"

@app.route('/previsao', methods=['POST'])
def obter_previsao_tempo():
    new_data = request.get_json() 
    cidade  = new_data["cidade"]

    params = {
        'q': cidade,  
        'appid': API_KEY,
        'lang' : 'pt_br' 
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': 'Erro ao obter dados da API'}), response.status_code

    previsao = [{'data': item['dt_txt'], 'temperatura': item['main']['temp']} for item in data['list']]
    converter_para_celsius = lambda temp_kelvin: round(temp_kelvin - 273.15)
    previsao_em_celsius = [{"data": entrada["data"], "temperatura": converter_para_celsius(entrada["temperatura"])} for entrada in previsao]

    return jsonify(previsao_em_celsius)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)