"""
- Este é o ponto de entrada principal da API.
- Responsável por inicializar a aplicação FastAPI (app) e incluir as rotas definidas no módulo de rotas (rotas_router).
- Em um aplicativo real, este arquivo pode conter configurações iniciais, inicializações de banco de dados, etc.

"""

from fastapi import FastAPI
from app.rotas.rotas import rotas_router  # Importa o roteador de rotas do módulo de rotas

app = FastAPI()

# Inclui as rotas definidas no módulo de rotas
app.include_router(rotas_router)
