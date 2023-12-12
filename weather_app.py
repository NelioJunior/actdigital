'''
exemplo de uso http://localhost:5000/previsao?cidade=bahia
'''

from flask import Flask,request, jsonify
import requests

app = Flask(__name__)

API_KEY = '11099dcc6bf337d99a6e478cbcd27994'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'


@app.route('/', methods=['GET'])
def root():
    return "<h1>utilize o endpoint /previsao juntamente como nome da cidade para saber sobre o clima do local desejado</h1>"


@app.route('/previsao', methods=['GET'])
def obter_previsao_tempo():
    cidade = request.args.get('cidade')

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

    return jsonify({'previsao': previsao})

if __name__ == '__main__':
   # app.run(debug=True)
   app.run(host='0.0.0.0', debug=True)
