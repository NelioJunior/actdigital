from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = '11099dcc6bf337d99a6e478cbcd27994'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

@app.route('/previsao', methods=['GET'])
def obter_previsao_tempo():
    try:
        params = {
            'q': 'SuaCidade',  # Substitua por sua cidade
            'appid': API_KEY,
        }

        # Fazer a chamada à API do OpenWeatherMap
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Verificar se a resposta foi bem-sucedida
        if response.status_code != 200:
            return jsonify({'error': 'Erro ao obter dados da API'}), response.status_code

        # Extrair informações relevantes da resposta
        previsao = [{'data': item['dt_txt'], 'temperatura': item['main']['temp']} for item in data['list']]

        return jsonify({'previsao': previsao})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
   # app.run(debug=True)
   app.run(host='0.0.0.0', port=5000, debug=True)
