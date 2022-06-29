# API FEITA EM FLASK POR VINICIUS INZAURRALDE

Esse projeto é resultado de um test code.


Principais bibliotecas usadas:
1. Flask.
2. Flask-RESTful.

Estrutura do projeto:
```
.
├── README.md
├── app.py
├── config
│   ├── urls.py
├── endpoints
│   ├── __init__.py
│   ├── resource
│   │   ├── category_joke_resource.py
│   │   └── randon_joke_resource.py
│   │   └── search_joke_resource.py
│   └── service
│       ├── category_joke_service.py
│       └── randon_joke_service.py
│       └── search_joke_service.py
├── integracao_util.py
├── requirements.txt
```

* endpoints - todos os endpoints disponiveis na aplicação ( recursos )
* app.py - Aplicação Flask configuração para inicialização
* integracao_util.py - modulo gerenciador de todas as integrações externas da API
* config.py - armazena as URLs de requisição externa da aplicação

## Iniciando a API

1. Clone o repositório ou extraia o arquivo.
2. pip install -r requirements.txt
3. insira o seguinte comando no console:
    1. python app.py
4. Espere a inicialização do servidor

## Usando a API

BASE_URL http://127.0.0.1:5000/

REQUEST
GET {{BASE_URL}}/api/jokes/random

RESPONSE
string "Chuck Norris is the reason why you don't see Total Gyms being sold in garage sales")


REQUEST
GET {{BASE_URL}}/api/jokes/category/<animal>

RESPONSE
string "Chuck Norris can skeletize a cow in two minutes."


REQUEST
GET {{BASE_URL}}/api/jokes/filter?search=car&limit=3

RESPONSE
List [
	"Chuck Norris won the daytona 500 in a flintstone car",
	"Chuck Norris doesn't beat people up he looks at them they get scared and fight their self to the death",
	"Chuck Norris scares leftovers into being fresh with one bite"
]