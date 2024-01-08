"""
Nome do arquivo: database.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pela conexão com o banco de dados.
"""
import mysql.connector
from decouple import config

def create_db_connection():
    try:
        conn = mysql.connector.connect(**{
            'user': config('DB_USER'),
            'password': config('DB_PASSWORD'),
            'host': config('DB_HOST'),
            'database': config('DB_DATABASE'),
            'raise_on_warnings': True,
        })
        return conn
    except mysql.connector.Error as e:
        print(f"[create_db_connection]: {e}")
        return None