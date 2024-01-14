"""
Nome do arquivo: logger.py
Autor: Guilherme Zaramella
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pelas configurações de logs.
"""
import logging
import os

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
log_level = logging.INFO
logs_dir = "./logs"
os.makedirs(logs_dir, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(log_level)

handler = logging.FileHandler(os.path.join(logs_dir, "tax-backend.log"))
handler.setLevel(log_level)

console_handler = logging.StreamHandler()
console_handler.setLevel(log_level)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console_handler)