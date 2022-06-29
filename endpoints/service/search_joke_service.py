import logging
from integracao_util import get_search_limit_joke
from flask import Response

class SearchJokeService:
    def search_joke(self, palavra_chave, limite):
        """
        service responsavel por filtrar piadas por palavras chaves
        e limitar a busca
        """
        lista_piadas_filtradas = []

        logging.info("iniciando requisição de piadas filtradas por palavra chave")
        try:
            retorno = get_search_limit_joke(palavra_chave)
            logging.info("piadas localizadas com sucesso")
            lista_piadas = [piada.get('value') for piada in retorno]
            quantidade_de_piadas =  len(lista_piadas)

            if quantidade_de_piadas < limite:
                limite = quantidade_de_piadas

            for piada in range(limite):
                lista_piadas_filtradas.append(lista_piadas[piada])

            return lista_piadas_filtradas

        except TypeError:
            logging.error("erro ao pesqusar piadas")           
            return Response(
                    "A requisição não foi corretamente executada, tente novamente ou contacte o suporte",
                    status=404,    
            )
