"""
Nome do arquivo: sqlalchemy.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 14/01/2024
Descrição: Arquivo responsável por validar os dados recebidos na rota auth.
"""
from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    email: str
    password: str
    session: str = Field(..., alias='_session')
