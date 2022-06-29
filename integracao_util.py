from flask import Response
import requests
import json

from config.urls import (
    URL_API_RANDON_JOKE,
    URL_API_CATEGORY_JOKE,
    URL_API_SEARCH_JOKE
)


def get_randon_joke():
    """
    integração externa GET para requisição de piadas aleatórias
    """
    retorno = requests.get(URL_API_RANDON_JOKE)
    if retorno.status_code in [200, 201]:
        response = json.loads(retorno.content)
        return response.get('value')

def get_category_joke(categoria):
    """
    integração externa GET para requisição de piadas definidas por categoria
    """
    retorno = requests.get(f"{URL_API_CATEGORY_JOKE}{categoria}")
    if retorno.status_code in [200, 201]:
        response = json.loads(retorno.content)
        return response.get('value')   
    else:
        return Response(
            "A categoria escolhida não existe, por favor tente outra categoria, ou contact o suporte",
            status=404,
        )

def get_search_limit_joke(palavra_chave):
    """
    integração externa GET para requisição de piadas encontradas por categoria
    """
    retorno = requests.get(f"{URL_API_SEARCH_JOKE}{palavra_chave}")
    if retorno.status_code in [200, 201]:
        response = json.loads(retorno.content)
        if len(response.get('result')) > 1:
            return response.get('result')
    else:
        return Response(
            "Houve um problema na requisição",
            status=404,
        )

