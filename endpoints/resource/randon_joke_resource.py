from flask_restful import Resource
from endpoints.service.randon_joke_service import RandonJokeService

class RandonJokeResource(Resource):
    def get(self):
        """
        Resource responsavel por gerar piadas aleatórias
        """
        retorno = RandonJokeService().randon_joke()        
        return retorno