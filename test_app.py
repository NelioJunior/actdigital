import unittest
from flask import Flask
from weather_app import obter_previsao_tempo, historico

class TestPrevisaoTempo(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False

    def test_obter_previsao_tempo(self):
        with self.app.test_request_context('/previsao', method='POST', json={'cidade': 'Sao Paulo'}):
            response = obter_previsao_tempo()
            self.assertEqual(response.status_code, 200)
            # Adicione mais asserções conforme necessário

    def test_historico(self):
        with self.app.test_request_context('/historico', method='GET'):
            response = historico()
            self.assertEqual(response.status_code, 200)
            # Adicione mais asserções conforme necessário

if __name__ == '__main__':
    unittest.main()
