import logging
from integracao_util import get_randon_joke
import requests

class RandonJokeService:
    def randon_joke(self):
        """
        service responsavel por gerar as piadas aleatórias
        """
        logging.info("iniciando requisição da piada aleatória")

        try:
            retorno = get_randon_joke()
            logging.info("piada aleatória requisitada com sucesso")
            return retorno

        except requests.exceptions.RequestException as e:
            logging.error("erro ao solicitar piada")            
            return e