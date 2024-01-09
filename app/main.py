"""
Nome do arquivo: main.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo principal da aplicação, responsável pela configuração e execução.
"""
from config.database import create_db_connection
from config.initialize import create_app
from utils.logger import logger
from decouple import config

def main():
    try:
        app = create_app()
        db_connection = create_db_connection()
        if db_connection:
            logger.info('[TAX Backend] estabelecida conexão com o database')
            app.run(host=config('HOST'), port=config('PORT'))
            db_connection.close()
        else: logger.warning('Não conectou ao database')
    except Exception as e:
        logger.error(f'[__main__]: {e}')

if __name__ == '__main__':
    main()