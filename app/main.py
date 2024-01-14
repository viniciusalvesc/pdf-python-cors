"""
Nome do arquivo: main.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo principal da aplicação, responsável pela configuração e execução.
"""
# from config.database import create_db_connection
from config.initialize import create_app
from utils.logger import logger
from decouple import config
import uvicorn
import asyncio

async def main():
    try:
        app = await create_app()
        
        await uvicorn.run(config('INIT_FILE_PATH'), 
            host="localhost", 
            port=3333, 
            reload=True
        )

    except Exception as e:
        logger.error(f'[__main__]: {e}')

if __name__ == '__main__':
    asyncio.run(main())