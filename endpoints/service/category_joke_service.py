import logging
from integracao_util import get_category_joke
import requests

class CategoryJokeService:
    def category_joke(self, categoria):
        """
        service responsavel por gerar as piadas definidas por categorias
        """
        logging.info("iniciando requisição da piada por categoria")

        try:
            retorno = get_category_joke(categoria)
            logging.info("piada requisitada com sucesso")
            return retorno

        except requests.exceptions.RequestException as e:
            logging.error("erro ao solicitar piada")            
            return e