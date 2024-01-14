"""
Nome do arquivo: sqlalchemy.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 14/01/2024
Descrição: Arquivo responsável por manter a sessão do banco de dados.
"""
from app.db.database import SessionLocal
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()