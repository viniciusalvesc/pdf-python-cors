"""
Nome do arquivo: helpers.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 18/01/2024
Descrição: Arquivo responsável por armazenar funções diversas para auxiliar no projeto.
"""
import bcrypt

async def password_check(password_request: str, password_db: str):
    return bcrypt.checkpw(password_request.encode('utf-8'), password_db.encode('utf-8'))
