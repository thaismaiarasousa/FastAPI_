"""
- Aqui ficam as definições de rotas (controllers) da aplicação.
- Usa o roteador rotas_router para agrupar as rotas relacionadas.
- Importa a função obter_dados_da_outra_api do serviço para processar a lógica de negócios relacionada à rota.

"""

from fastapi import APIRouter, HTTPException 
from app.servicos.item_servico import obter_dados_da_outra_api  # Importa a função do serviço

# Cria uma instância de APIRouter
rotas_router = APIRouter()

@rotas_router.get("/dados-da-outra-api")
def obter_dados():
    return obter_dados_da_outra_api()
