from flask import Flask
from flask_restful import Api

from endpoints.resource.randon_joke_resource import RandonJokeResource
from endpoints.resource.category_joke_resource import CategoryJokeResource
from endpoints.resource.search_joke_resource import SearchJokeResource


app = Flask(__name__)
api = Api(app)
api.prefix = '/api/jokes'

# -------------------------------------------------------------------------------
# END POINT PARA GERAÇÃO DE PIADA ALEATÓRIA
# -------------------------------------------------------------------------------
api.add_resource(RandonJokeResource, '/random', methods=['GET'], endpoint='/random_get')
# -------------------------------------------------------------------------------
# END POINT PARA GERAÇÃO DE PIADA COM CATEGORIA
# -------------------------------------------------------------------------------
api.add_resource(CategoryJokeResource, '/category/<categoria>', methods=['GET'], endpoint='/category_get')
# -------------------------------------------------------------------------------
# END POINT PARA GERAÇÃO DE PIADAS ALEATÓRIAS COM FILTRO DE PALAVRA E LIMITE DE PIADAS DEFINIDO
# -------------------------------------------------------------------------------
api.add_resource(SearchJokeResource, '/filter', methods=['GET'], endpoint='/search_joke_get')



if __name__ == '__main__':
    app.run(debug=True)