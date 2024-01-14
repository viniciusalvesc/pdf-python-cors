"""
Nome do arquivo: main.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo principal da aplicação, responsável pela configuração e execução.
"""
from app.config.initialize import create_app

def main():
    return create_app()

if __name__ == '__main__':
    main()
