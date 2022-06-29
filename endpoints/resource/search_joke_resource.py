from flask_restful import Resource
from flask import request
from endpoints.service.search_joke_service import SearchJokeService

class SearchJokeResource(Resource):
    def get(self):
        """
        Resource responsavel por pesquisar piadas com palavras chaves e limitar a busca
        """
        palavra_chave = request.args.get('search')
        limite = int(request.args.get('limit'))

        retorno = SearchJokeService().search_joke(palavra_chave, limite)       
        return retorno