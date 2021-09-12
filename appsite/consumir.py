import requests
import json

url = 'http://localhost:1010/api-evento/'
event_data = {
    'titulo': 'Outra coisa', 
    'descricao': 'outra coisa', 
    'qtdPessoas': 100, 
    'dataEvento': '22/08/2024', 
    'horaInicial': '14:00', 
    'horaFinal': '23:00', 
    'local': 'sdfsdf', 
}

request = requests.delete('http://localhost:1010/api-evento/10/')
# request = requests.post(url = url, json = event_data)
# # request = requests.get(url)

# print(request.status_code)
# print(request.reason)
# dados = json.loads(request.content)
# print(dados)
# # for x in dados:
# #     print(x['titulo'])



