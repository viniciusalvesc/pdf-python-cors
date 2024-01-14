"""
Nome do arquivo: initialize.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo gerador da aplicação Flask com as respectivas configurações.
"""
from api.routers import router
from fastapi import FastAPI

async def create_app():
    app = FastAPI()
    app.include_router(router)

    return app