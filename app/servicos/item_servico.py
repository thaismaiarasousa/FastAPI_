"""
- Contém a lógica de negócios relacionada aos itens.
- Define a função obter_dados_da_outra_api, que realiza uma solicitação à API externa e trata possíveis erros.
"""

import requests
from fastapi import HTTPException

def obter_dados_da_outra_api():
    url_da_outra_api = "https://www.el-tiempo.net/api/json/v2/provincias/01"

    try:
        response = requests.get(url_da_outra_api)
        response.raise_for_status()
        dados = response.json()
        return {"dados": dados}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter dados da outra API: {str(e)}")
