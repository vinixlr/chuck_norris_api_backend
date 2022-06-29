from flask_restful import Resource
from endpoints.service.category_joke_service import CategoryJokeService

class CategoryJokeResource(Resource):
    def get(self, categoria):
        """
        Resource responsavel por gerar piadas com categorias especificas
        """
        retorno = CategoryJokeService().category_joke(categoria)        
        return retorno