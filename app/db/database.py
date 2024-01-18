"""
Nome do arquivo: sqlalchemy.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 14/01/2024
Descrição: Arquivo responsável por conectar e inicializar o banco de dados.
"""
from sqlalchemy import create_engine
from decouple import config
from databases import Database
from sqlalchemy.orm import sessionmaker
from app.api.utils.logger import logger

try: 
    database = Database(config('SQLALCHEMY_DATABASE_URI'))
    engine = create_engine(config('SQLALCHEMY_DATABASE_URI'))

    logger.info('[TAX Backend] estabelecida conexão com mariaDB')

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
        logger.error(f'[__main__]: {e}')
