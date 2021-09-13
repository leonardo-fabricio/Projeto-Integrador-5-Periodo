import requests
import json
import re

def aaa(url):
    print(url)

url = 'http://localhost:8080/api-evento/' # trocar para 8080, pois 1010 não funcionava
event_data = {
    'titulo': 'Outra coisa', 
    'descricao': 'outra coisa', 
    'qtdPessoas': 100, 
    'dataEvento': '22/08/2024', 
    'horaInicial': '14:00', 
    'horaFinal': '23:00', 
    'local': 'sdfsdf', 
}

# request = requests.delete('http://localhost:1010/api-evento/10/')
request = requests.get(url)
# test = re.findall(f'[0-9]*[0-9]', url)
# print(test[-1])
#print(vet[-1])

# request = requests.post(url = url, json = event_data)
# # request = requests.get(url)

# print(request.status_code)
# print(request.reason)
dados = json.loads(request.content)
# print(dados)
# for x in dados:
#     print(type(x['url']))
#     aaa(x['url'])
    
    




